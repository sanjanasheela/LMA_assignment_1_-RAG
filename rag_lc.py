"""The same RAG variants rebuilt with LangChain (retrievers, compressors, LCEL chains) and LangGraph (agentic loop).

Every variant is a Runnable: `chain.invoke(question) -> {"question", "docs", "answer"}`; `chain.batch(questions)` runs them in parallel.
Compare with rag_lib.py, which implements the same pipelines by hand.
"""
import os, re, json, glob, time, shutil, hashlib, subprocess, tempfile
from collections import Counter
from typing import Any, TypedDict

os.environ.setdefault("HF_HUB_OFFLINE", "1")
import numpy as np
from langchain_chroma import Chroma
from langchain_classic.retrievers import ContextualCompressionRetriever, EnsembleRetriever
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker, DocumentCompressorPipeline
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_community.document_transformers import EmbeddingsRedundantFilter
from langchain_community.retrievers import BM25Retriever
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.documents import BaseDocumentTransformer, Document
from langchain_core.language_models.llms import LLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from langgraph.graph import END, START, StateGraph

HEADERS = [("#", "h1"), ("##", "h2"), ("###", "h3"), ("####", "h4")]
toks = lambda t: re.findall(r"[a-z0-9]+", t.lower())
norm = lambda t: " ".join(re.findall(r"[a-z0-9+]+", t.lower().replace("−", "-")))


# ----------------------------------------------------------------------------- LLM: isolated `claude -p` as a LangChain LLM
class ClaudeCLI(LLM):
    """Text-only Claude call: no tools, files, skills, MCP or settings; runs in an empty temp dir."""
    model: str = "haiku"

    @property
    def _llm_type(self):
        return "claude-cli"

    def _call(self, prompt, stop=None, run_manager=None, **kw):
        with tempfile.TemporaryDirectory() as empty:
            for a in range(3):
                try:
                    return subprocess.run(
                        ["claude", "-p", "--model", self.model, "--tools", "", "--no-session-persistence", "--setting-sources", "",
                         "--disable-slash-commands", "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                         "--system-prompt", "You are a text-only assistant. You have no tools and cannot read files."],
                        input=prompt, capture_output=True, text=True, check=True, cwd=empty, timeout=240).stdout.strip()
                except Exception:
                    time.sleep(5 * (a + 1))
        return "ERROR: claude call failed"


ANSWER = PromptTemplate.from_template(
    "You are a Dungeons & Dragons rules assistant. Answer the question using ONLY the text in the Context below. Do not use any outside "
    "knowledge or memory of D&D; the Context may differ from the official rules and the Context is always right. If the Context lacks part "
    "of the answer, say which part is missing. Answer every part of the question, concisely.\n\nContext:\n{context}\n\nQuestion: {question}\nAnswer:")
PLAN = PromptTemplate.from_template(
    "You plan searches over a Dungeons & Dragons rules corpus. Break the question into the smallest set of independent search queries "
    "(max 6). Each query must be short, keyword-style and name ONE specific spell, monster, item, feat, class, condition or rule. "
    "Output only a JSON list of strings.\n\nQuestion: {question}")
CHECK = PromptTemplate.from_template(
    "Question: {question}\n\nRetrieved context:\n{context}\n\nWhich facts needed to answer EVERY part of the question are still missing "
    "from the context? Output only a JSON list of short keyword search queries for the missing facts, or [] if nothing is missing.")


def json_list(text):
    m = re.search(r"\[.*\]", text, flags=re.S)
    try:
        return [s for s in json.loads(m.group(0)) if isinstance(s, str)][:6] if m else []
    except Exception:
        return []


fmt = lambda docs: "\n\n---\n\n".join(d.page_content for d in docs)


class TopK(BaseDocumentTransformer):
    def __init__(self, k):
        self.k = k

    def transform_documents(self, documents, **kw):
        return list(documents)[:self.k]


class RoutedDense(BaseRetriever):
    """Coarse-to-fine routing: file centroids -> section centroids -> dense search restricted to those sections."""
    stack: Any
    k: int = 50

    def _get_relevant_documents(self, query, *, run_manager=None):
        s = self.stack
        q = np.array(s.emb.embed_query(query))
        keep = {s.files[i] for i in np.argsort(-(s.fC @ q))[:int(np.ceil(0.5 * len(s.files)))]}
        cand = np.where(np.isin(s.s_file, list(keep)))[0]
        keys = [s.skeys[i] for i in cand[np.argsort(-(s.sC[cand] @ q))[:150]]]
        return s.vs.similarity_search(query, k=self.k, filter={"skey": {"$in": keys}})


class EntityGraphRetriever(BaseRetriever):
    """Entity graph without an LLM: seed chunks + chunks of entities named in the query + entities mentioned in the seeds."""
    stack: Any
    seeds: Any

    def _get_relevant_documents(self, query, *, run_manager=None, per_ent=2, n_expand=6):
        s = self.stack
        q = np.array(s.emb.embed_query(query))
        seeds = [s.docs[s.pos[d.page_content]] for d in self.seeds.invoke(query)]   # fresh Documents: the filter leaves private state on its output
        pool = list(seeds)
        def top(e, n):                              # the n chunks of entity e most similar to the query
            ids = s.ent_chunks[e]
            return [s.docs[ids[j]] for j in np.argsort(-(s.E[ids] @ q))[:n]]

        qents = [e for e in dict.fromkeys(s.find(query)) if e not in s.hubs]
        for e in qents:
            pool += top(e, per_ent + 1)
        cnt = Counter(m for d in seeds[:5] for m in s.mentions[s.pos[d.page_content]] if m not in s.hubs and m not in qents)
        for e, _ in cnt.most_common(n_expand):
            pool += top(e, per_ent)
        return list({d.page_content: d for d in pool}.values())


class Stack:
    """Index + every variant as a Runnable."""

    def __init__(self, data_dir, chroma_dir, model="haiku"):
        self.llm = ClaudeCLI(model=model)
        self.emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", encode_kwargs={"normalize_embeddings": True})
        self.ce = HuggingFaceCrossEncoder(model_name="cross-encoder/ms-marco-MiniLM-L-6-v2")
        self._load(data_dir)
        if os.path.exists(chroma_dir):
            shutil.rmtree(chroma_dir)
        self.vs = Chroma.from_documents(self.docs, self.emb, ids=[d.id for d in self.docs], collection_name="srd", persist_directory=chroma_dir,
                                        collection_metadata={"hnsw:space": "cosine"})
        self._layers()
        self._entities()
        self.variants = self._variants()

    def _load(self, data_dir):                      # header-aware split + exact dedup (id = hash of section + text)
        hs, rs = MarkdownHeaderTextSplitter(HEADERS, strip_headers=False), RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        seen, docs = set(), []
        for p in sorted(glob.glob(os.path.join(data_dir, "*.md"))):
            src = os.path.basename(p)
            for sec in hs.split_text(open(p, encoding="utf-8-sig").read()):
                h = [sec.metadata[k] for _, k in HEADERS if k in sec.metadata]
                section = " > ".join(dict.fromkeys([h[0], h[-1]])) if h else ""
                entity = re.sub(r"\s*\[.*?\]", "", h[-1]).strip().lower() if h else ""
                for c in rs.split_documents([sec]):
                    text = f"[{section}]\n{c.page_content}" if section else c.page_content
                    cid = hashlib.sha1(norm(text).encode()).hexdigest()
                    if cid not in seen:
                        seen.add(cid)
                        docs.append(Document(id=cid, page_content=text, metadata={"source": src, "section": section, "skey": f"{src}|{section}", "entity": entity}))
        self.docs = docs
        self.pos = {d.page_content: i for i, d in enumerate(docs)}   # chunk text -> index (unique after dedup)

    def _layers(self):
        got = self.vs.get(include=["embeddings"])
        pos = {i: n for n, i in enumerate(got["ids"])}
        self.E = np.array([got["embeddings"][pos[d.id]] for d in self.docs])
        def centroids(key):
            groups = {}
            for i, d in enumerate(self.docs):
                groups.setdefault(d.metadata[key], []).append(i)
            keys = sorted(groups)
            c = np.stack([self.E[groups[k]].mean(0) for k in keys])
            return keys, c / (np.linalg.norm(c, axis=1, keepdims=True) + 1e-12)

        self.files, self.fC = centroids("source")
        self.skeys, self.sC = centroids("skey")
        self.s_file = np.array([k.split("|")[0] for k in self.skeys])

    def _entities(self, max_hub=120):
        self.ent_chunks = {}
        for i, d in enumerate(self.docs):
            if len(d.metadata["entity"]) >= 4:
                self.ent_chunks.setdefault(d.metadata["entity"], []).append(i)
        self.names = {tuple(toks(e)): e for e in self.ent_chunks if toks(e)}
        self.mentions = [self.find(d.page_content.split("\n", 1)[-1], exclude=d.metadata["entity"]) for d in self.docs]
        count = Counter(m for ms in self.mentions for m in set(ms))
        self.hubs = {e for e, n in count.items() if n > max_hub}

    def find(self, text, exclude="", max_n=4):      # longest-match entity linking
        t, out, i = toks(text), [], 0
        while i < len(t):
            n = next((n for n in range(max_n, 0, -1) if tuple(t[i:i + n]) in self.names), 0)
            if n:
                e = self.names[tuple(t[i:i + n])]
                out += [e] if e != exclude else []
            i += n or 1
        return out

    def refine(self, base, pool, n, rerank=True):   # near-duplicate filter -> candidate pool -> cross-encoder -> top n
        steps = [EmbeddingsRedundantFilter(embeddings=self.emb, similarity_threshold=0.95), TopK(pool)]
        steps.append(CrossEncoderReranker(model=self.ce, top_n=n) if rerank else TopK(n))
        return ContextualCompressionRetriever(base_retriever=base, base_compressor=DocumentCompressorPipeline(transformers=steps))

    def with_answer(self, retriever):               # retriever -> {"question", "docs", "answer"}
        gen = RunnableLambda(lambda x: {"context": fmt(x["docs"]), "question": x["question"]}) | ANSWER | self.llm | StrOutputParser()
        return RunnableParallel(docs=retriever, question=RunnablePassthrough()).assign(answer=gen)

    def _variants(self):
        dense = self.vs.as_retriever(search_kwargs={"k": 50})
        hybrid = EnsembleRetriever(retrievers=[RoutedDense(stack=self), BM25Retriever.from_documents(self.docs, k=50, preprocess_func=toks)], weights=[.5, .5])
        graph = EntityGraphRetriever(stack=self, seeds=self.refine(hybrid, 10, 10, rerank=False))
        v = {"v1_baseline": self.refine(dense, 3, 3, rerank=False),
             "v2_rerank": self.refine(dense, 10, 3),
             "v2b_rerank8": self.refine(dense, 10, 8),
             "v3_hier_rerank": self.refine(RoutedDense(stack=self), 10, 3),
             "v4_hybrid": self.refine(hybrid, 30, 8),
             "v5_graph": self.refine(graph, 100, 8)}
        self.retrievers = v
        out = {k: self.with_answer(r) for k, r in v.items()}
        out["v6_agentic"] = self._agent(self.refine(hybrid, 20, 3))
        return out

    # ------------------------------------------------------------------ LangGraph: plan -> retrieve -> check -> (follow-up) -> answer
    def _agent(self, fetcher):
        class State(TypedDict, total=False):
            question: str
            subqueries: list
            followups: list
            docs: list
            answer: str

        fetch = lambda qs: list({d.page_content: d for ds in fetcher.batch(qs) for d in ds}.values())
        plan_chain = PLAN | self.llm | RunnableLambda(json_list)
        check_chain = CHECK | self.llm | RunnableLambda(json_list)
        answer_chain = ANSWER | self.llm | StrOutputParser()

        def plan(s):
            subs = plan_chain.invoke(s) or [s["question"]]
            return {"subqueries": subs, "docs": fetch(subs)}

        def check(s):
            return {"followups": check_chain.invoke({"question": s["question"], "context": fmt(s["docs"])})}

        def follow_up(s):
            return {"docs": list({d.page_content: d for d in s["docs"] + fetch(s["followups"])}.values())}

        def respond(s):
            docs = s["docs"][:16]
            return {"docs": docs, "answer": answer_chain.invoke({"context": fmt(docs), "question": s["question"]})}

        g = StateGraph(State)
        for name, fn in [("plan", plan), ("check", check), ("follow_up", follow_up), ("respond", respond)]:
            g.add_node(name, fn)
        g.add_edge(START, "plan"); g.add_edge("plan", "check")
        g.add_conditional_edges("check", lambda s: "follow_up" if s["followups"] else "respond", {"follow_up": "follow_up", "respond": "respond"})
        g.add_edge("follow_up", "respond"); g.add_edge("respond", END)
        return RunnableLambda(lambda q: q if isinstance(q, dict) else {"question": q}) | g.compile()


class CallStats(BaseCallbackHandler):
    """Counts LLM calls and wall time of one run via LangChain callbacks."""

    def __init__(self):
        self.calls, self.secs, self._t0 = 0, 0.0, None

    def on_llm_start(self, *a, **k):
        self.calls += 1

    def on_chain_start(self, *a, parent_run_id=None, **k):
        if parent_run_id is None:
            self._t0 = time.perf_counter()

    def on_chain_end(self, *a, parent_run_id=None, **k):
        if parent_run_id is None:
            self.secs = time.perf_counter() - self._t0
