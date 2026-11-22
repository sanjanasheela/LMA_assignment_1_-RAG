"""RAG variants over the D&D SRD: baseline, rerank, hierarchical, hybrid, graph, agentic (+ closed-book control).

All LLM calls go through `llm()`, which runs `claude -p` in an empty temp dir with every tool, skill, MCP server
and setting source disabled, so the model can only see the prompt text (never the data files).
"""
import os, re, json, glob, time, shutil, hashlib, subprocess, tempfile, threading
from collections import defaultdict, Counter

os.environ.setdefault("HF_HUB_OFFLINE", "1")
import numpy as np, torch, chromadb
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer, CrossEncoder
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

BI_ENCODER = "sentence-transformers/all-MiniLM-L6-v2"
CROSS_ENCODER = "cross-encoder/ms-marco-MiniLM-L-6-v2"
HEADERS = [("#", "h1"), ("##", "h2"), ("###", "h3"), ("####", "h4")]
device = "cuda" if torch.cuda.is_available() else "cpu"
GPU_LOCK = threading.Lock()


# ----------------------------------------------------------------------------- text utils
def toks(t):
    return re.findall(r"[a-z0-9]+", t.lower())


def norm(t):
    return " ".join(re.findall(r"[a-z0-9+]+", t.lower().replace("−", "-")))


def has_fact(text, fact):
    return f" {norm(fact)} " in f" {norm(text)} "


# ----------------------------------------------------------------------------- LLM (isolated claude -p)
def llm(prompt, model="haiku", retries=3, timeout=240):
    """Returns (text, seconds). No tools, no files, no skills/MCP/settings; cwd is an empty temp dir."""
    if os.environ.get("LLM_BACKEND") == "qwen":          # local Qwen (Colab); same prompts, no tools
        import qwen_backend
        return qwen_backend.generate(prompt)
    with tempfile.TemporaryDirectory() as empty:
        for a in range(retries):
            try:
                t0 = time.perf_counter()
                r = subprocess.run(
                    ["claude", "-p", "--model", model, "--tools", "", "--no-session-persistence",
                     "--setting-sources", "", "--disable-slash-commands",
                     "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
                     "--system-prompt", "You are a text-only assistant. You have no tools and cannot read files."],
                    input=prompt, capture_output=True, text=True, check=True, cwd=empty, timeout=timeout)
                return r.stdout.strip(), time.perf_counter() - t0
            except Exception as e:
                time.sleep(5 * (a + 1))
    return "ERROR: claude call failed", 0.0


ANSWER_PROMPT = """You are a Dungeons & Dragons rules assistant. Answer the question using ONLY the text in the Context below. Do not use any outside knowledge or memory of D&D; the Context may differ from the official rules and the Context is always right. If the Context lacks part of the answer, say which part is missing. Answer every part of the question, concisely.

Context:
{context}

Question: {question}
Answer:"""

CLOSED_PROMPT = """You are a Dungeons & Dragons 5e (2024 SRD 5.2) rules assistant. Answer the question from your own knowledge, concisely, answering every part. If you are unsure of a detail, give your best answer.

Question: {question}
Answer:"""


# ----------------------------------------------------------------------------- index
class Index:
    def __init__(self, data_dir, chroma_dir, fetch_k=50, near_dup=0.95):
        self.fetch_k, self.near_dup = fetch_k, near_dup
        self.tl = threading.local()
        self.bi = SentenceTransformer(BI_ENCODER, device=device)
        self.ce = CrossEncoder(CROSS_ENCODER, device=device)
        self._load(data_dir)
        self._embed_and_store(chroma_dir)
        self._build_layers()
        self._build_bm25()
        self._build_graph()

    # --- chunking + exact dedup (id = hash of section + text)
    def _load(self, data_dir):
        hs = MarkdownHeaderTextSplitter(HEADERS, strip_headers=False)
        rs = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        seen, ch = set(), []
        for p in sorted(glob.glob(os.path.join(data_dir, "*.md"))):
            src = os.path.basename(p)
            for sec in hs.split_text(open(p, encoding="utf-8-sig").read()):
                h = [sec.metadata[k] for _, k in HEADERS if k in sec.metadata]
                section = " > ".join(dict.fromkeys([h[0], h[-1]])) if h else ""
                entity = re.sub(r"\s*\[.*?\]", "", h[-1]).strip().lower() if h else ""
                for c in rs.split_documents([sec]):
                    text = f"[{section}]\n{c.page_content}" if section else c.page_content
                    cid = hashlib.sha1(norm(text).encode()).hexdigest()
                    if cid in seen:
                        continue
                    seen.add(cid)
                    ch.append({"id": cid, "text": text, "source": src, "section": section,
                               "skey": f"{src}|{section}", "entity": entity})
        self.chunks = ch
        self.id2i = {c["id"]: i for i, c in enumerate(ch)}

    def _embed_and_store(self, chroma_dir):
        self.E = self.bi.encode([c["text"] for c in self.chunks], normalize_embeddings=True,
                                batch_size=128, show_progress_bar=False)
        if os.path.exists(chroma_dir):
            shutil.rmtree(chroma_dir)
        col = chromadb.PersistentClient(chroma_dir).create_collection("srd", metadata={"hnsw:space": "cosine"})
        for s in range(0, len(self.chunks), 2000):
            part = self.chunks[s:s + 2000]
            col.add(ids=[c["id"] for c in part], embeddings=self.E[s:s + 2000].tolist(),
                    documents=[c["text"] for c in part],
                    metadatas=[{"source": c["source"], "skey": c["skey"]} for c in part])
        self.col = col

    # --- layers for coarse-to-fine routing: file centroids -> section centroids
    def _build_layers(self):
        unit = lambda v: v / (np.linalg.norm(v) + 1e-12)
        by_f, by_s = defaultdict(list), defaultdict(list)
        for i, c in enumerate(self.chunks):
            by_f[c["source"]].append(i); by_s[c["skey"]].append(i)
        self.files = sorted(by_f); self.fC = np.stack([unit(self.E[by_f[f]].mean(0)) for f in self.files])
        self.skeys = sorted(by_s); self.sC = np.stack([unit(self.E[by_s[k]].mean(0)) for k in self.skeys])
        self.s_file = np.array([k.split("|")[0] for k in self.skeys])
        self.by_skey = by_s

    def route(self, q, file_keep=0.5, sec_keep=150):
        nf = max(1, int(np.ceil(file_keep * len(self.files))))
        keep = {self.files[i] for i in np.argsort(-(self.fC @ q))[:nf]}
        cand = np.where(np.isin(self.s_file, list(keep)))[0]
        top = cand[np.argsort(-(self.sC[cand] @ q))[:sec_keep]]
        return [self.skeys[i] for i in top]

    # --- BM25 (sparse)
    def _build_bm25(self, k1=1.5, b=0.75):
        self.cv = CountVectorizer(token_pattern=r"[a-z0-9]+", lowercase=True)
        tf = self.cv.fit_transform([c["text"] for c in self.chunks]).tocsc().astype(np.float32)
        N = tf.shape[0]
        df = np.diff(tf.indptr)
        self.idf = np.log(1 + (N - df + 0.5) / (df + 0.5)).astype(np.float32)
        dl = np.asarray(tf.sum(1)).ravel(); avg = dl.mean()
        tf = tf.tocoo()
        w = tf.data * (k1 + 1) / (tf.data + k1 * (1 - b + b * dl[tf.row] / avg))
        import scipy.sparse as sp
        self.W = sp.csc_matrix((w * self.idf[tf.col], (tf.row, tf.col)), shape=tf.shape)

    def bm25(self, query, k):
        v = self.cv.transform([query]).tocoo()
        if v.nnz == 0:
            return []
        s = np.asarray(self.W[:, v.col].sum(1)).ravel()
        top = np.argsort(-s)[:k]
        out = [int(i) for i in top if s[i] > 0]
        self._trace("bm25", items=[{"i": i, "rank": n + 1, "bm25": round(float(s[i]), 3)} for n, i in enumerate(out)])
        return out

    # --- entity graph: nodes = section entities, edges = "chunk of A mentions B"
    def _build_graph(self, max_hub=120, max_n=4):
        ent_chunks = defaultdict(list)
        for i, c in enumerate(self.chunks):
            if len(c["entity"]) >= 4:
                ent_chunks[c["entity"]].append(i)
        names = {tuple(toks(e)): e for e in ent_chunks if toks(e)}
        self.ent_chunks, self.names = ent_chunks, names
        mention_count = Counter()
        self.chunk_mentions = []
        for c in self.chunks:
            self.chunk_mentions.append(self._find(c["text"].split("\n", 1)[-1], exclude=c["entity"]))
            mention_count.update(set(self.chunk_mentions[-1]))
        self.hubs = {e for e, n in mention_count.items() if n > max_hub}
        import networkx as nx
        G = nx.DiGraph()
        for i, ms in enumerate(self.chunk_mentions):
            a = self.chunks[i]["entity"]
            for m in ms:
                if m in self.hubs or not a:
                    continue
                w = G[a][m]["w"] + 1 if G.has_edge(a, m) else 1
                G.add_edge(a, m, w=w)
        self.G = G

    def _find(self, text, exclude="", max_n=4):
        t = toks(text); out, i = [], 0
        while i < len(t):
            hit = None
            for n in range(max_n, 0, -1):
                key = tuple(t[i:i + n])
                if len(key) == n and key in self.names:
                    hit = (key, n); break
            if hit:
                e = self.names[hit[0]]
                if e != exclude:
                    out.append(e)
                i += hit[1]
            else:
                i += 1
        return out

    # ------------------------------------------------------------------ tracing (what was retrieved / re-ranked / selected)
    def _trace(self, stage, **kw):
        t = getattr(self.tl, "trace", None)
        if t is not None:
            t.append({"stage": stage, **kw})

    def pack_trace(self, trace, final_ids):
        """Makes the raw trace JSON-friendly: chunk indices -> chunk id/section, and mark which chunks reached the LLM."""
        final = set(final_ids)
        meta = lambda i: {"chunk_id": self.chunks[i]["id"][:12], "section": self.chunks[i]["section"], "source": self.chunks[i]["source"]}
        out = []
        for st in trace:
            st = dict(st)
            items = []
            for it in st.pop("items", []):
                d = {**meta(it["i"]), **{k: v for k, v in it.items() if k != "i"}, "selected_for_llm": it["i"] in final}
                if st["stage"] == "rerank":
                    d["text"] = self.chunks[it["i"]]["text"]
                items.append(d)
            out.append({**st, "items": items})
        return out

    # ------------------------------------------------------------------ retrieval primitives
    def qemb(self, q):
        with GPU_LOCK:
            return self.bi.encode([q], normalize_embeddings=True)[0]

    def dense(self, q, k, hier=False):
        where = {"skey": {"$in": self.route(q)}} if hier else None
        with GPU_LOCK:
            r = self.col.query(query_embeddings=[q.tolist()], n_results=k, where=where)
        ids = [self.id2i[i] for i in r["ids"][0]]
        self._trace("dense_routed" if hier else "dense", items=[{"i": i, "rank": n + 1, "cosine_dist": round(float(d), 4)}
                                                               for n, (i, d) in enumerate(zip(ids, r["distances"][0]))])
        return ids

    def uniq(self, idxs, k):
        kept = []
        for i in idxs:
            if all(float(self.E[i] @ self.E[j]) < self.near_dup for j in kept):
                kept.append(i)
            if len(kept) == k:
                break
        return kept

    def rerank(self, query, idxs):
        if not idxs:
            return []
        with GPU_LOCK:
            sc = self.ce.predict([[query, self.chunks[i]["text"]] for i in idxs], show_progress_bar=False)
        order = [i for _, i in sorted(zip(sc, idxs), key=lambda x: -x[0])]
        pre = {i: n + 1 for n, i in enumerate(idxs)}
        score = dict(zip(idxs, map(float, sc)))
        self._trace("rerank", query=query, items=[{"i": i, "pre_rank": pre[i], "ce_rank": n + 1, "ce_score": round(score[i], 4)}
                                                   for n, i in enumerate(order)])
        return order

    @staticmethod
    def rrf(lists, k=60):
        s = defaultdict(float)
        for L in lists:
            for r, i in enumerate(L):
                s[i] += 1 / (k + r + 1)
        return [i for i, _ in sorted(s.items(), key=lambda x: -x[1])]

    def hybrid(self, query, q, pool=30):
        d = self.dense(q, self.fetch_k, hier=True)
        b = self.bm25(query, self.fetch_k)
        return self.uniq(self.rrf([d, b]), pool)

    def query_entities(self, query):
        return [e for e in dict.fromkeys(self._find(query)) if e not in self.hubs]

    def graph_pool(self, query, q, seeds, per_ent=2, n_expand=6):
        pool = list(seeds)
        origin = {i: "seed" for i in seeds}
        # entities named in the query: pull their best chunks directly
        qents = self.query_entities(query)
        for e in qents:
            ids = self.ent_chunks[e]
            add = [ids[j] for j in np.argsort(-(self.E[ids] @ q))[:per_ent + 1]]
            pool += add; origin.update({i: origin.get(i, f"query_entity:{e}") for i in add})
        # entities mentioned inside the seed chunks (1-hop in the graph)
        cnt = Counter()
        for i in seeds[:5]:
            for m in self.chunk_mentions[i]:
                if m not in self.hubs and m not in qents:
                    cnt[m] += 1
        for e, _ in cnt.most_common(n_expand):
            ids = self.ent_chunks[e]
            add = [ids[j] for j in np.argsort(-(self.E[ids] @ q))[:per_ent]]
            pool += add; origin.update({i: origin.get(i, f"graph_expansion:{e}") for i in add})
        pool = list(dict.fromkeys(pool))
        self._trace("graph_pool", items=[{"i": i, "origin": origin[i]} for i in pool])
        return pool


# ----------------------------------------------------------------------------- variants
# Each returns (context_chunk_indices, extra_info). `idx` is an Index.
def v1_baseline(idx, query):
    q = idx.qemb(query)
    return idx.uniq(idx.dense(q, idx.fetch_k), 10)[:3], {}


def v2_rerank(idx, query, n=3):
    q = idx.qemb(query)
    return idx.rerank(query, idx.uniq(idx.dense(q, idx.fetch_k), 10))[:n], {}


def v2b_rerank8(idx, query):
    return v2_rerank(idx, query, n=8)


def v3_hier_rerank(idx, query):
    q = idx.qemb(query)
    return idx.rerank(query, idx.uniq(idx.dense(q, idx.fetch_k, hier=True), 10))[:3], {}


def v4_hybrid(idx, query, n=8):
    q = idx.qemb(query)
    return idx.rerank(query, idx.hybrid(query, q))[:n], {}


def v5_graph(idx, query, n=8):
    q = idx.qemb(query)
    seeds = idx.hybrid(query, q, pool=10)
    pool = idx.graph_pool(query, q, seeds)
    return idx.rerank(query, pool)[:n], {"query_entities": idx.query_entities(query)}


def _json_list(text):
    m = re.search(r"\[.*\]", text, flags=re.S)
    try:
        return [s for s in json.loads(m.group(0)) if isinstance(s, str)][:6] if m else []
    except Exception:
        return []


def _agentic_fetch(idx, qs):
    out = []
    for s in qs:
        q = idx.qemb(s)
        out += idx.rerank(s, idx.hybrid(s, q, pool=20))[:3]
    return out


def v6_agentic(idx, query, model="haiku", replay=None):
    """replay=(subqueries, followups) re-runs only the retrieval of an earlier run (no LLM calls)."""
    calls, secs = 0, 0.0
    if replay:
        subs, more = replay
        got = list(dict.fromkeys(_agentic_fetch(idx, subs)))
        if more:
            got = list(dict.fromkeys(got + _agentic_fetch(idx, more)))
        return got[:16], {"subqueries": subs, "followups": more}
    plan, t = llm(
        "You plan searches over a Dungeons & Dragons rules corpus. Break the question into the smallest set of independent "
        "search queries (max 6). Each query must be short, keyword-style and name ONE specific spell, monster, item, feat, "
        "class, condition or rule. Output only a JSON list of strings.\n\nQuestion: " + query, model)
    calls += 1; secs += t
    subs = _json_list(plan) or [query]

    fetch = lambda qs: _agentic_fetch(idx, qs)
    got = list(dict.fromkeys(fetch(subs)))
    ctx = "\n\n---\n\n".join(idx.chunks[i]["text"] for i in got)
    chk, t = llm(
        "Question: " + query + "\n\nRetrieved context:\n" + ctx + "\n\nWhich facts needed to answer EVERY part of the question "
        "are still missing from the context? Output only a JSON list of short keyword search queries for the missing "
        "facts, or [] if nothing is missing.", model)
    calls += 1; secs += t
    more = _json_list(chk)
    if more:
        got = list(dict.fromkeys(got + fetch(more)))
    return got[:16], {"subqueries": subs, "followups": more, "extra_llm_calls": calls, "extra_llm_s": secs}


VARIANTS = {
    "v1_baseline": v1_baseline,
    "v2_rerank": v2_rerank,
    "v2b_rerank8": v2b_rerank8,
    "v3_hier_rerank": v3_hier_rerank,
    "v4_hybrid": v4_hybrid,
    "v5_graph": v5_graph,
    "v6_agentic": v6_agentic,
}


def answer(idx, variant, question, model="haiku"):
    """Runs one variant on one question. variant 'v0_closed_book' uses no context."""
    t0 = time.perf_counter()
    if variant == "v0_closed_book":
        text, llm_s = llm(CLOSED_PROMPT.format(question=question), model)
        return {"answer": text, "context": [], "extra": {}, "llm_calls": 1, "total_s": time.perf_counter() - t0}
    idx.tl.trace = []
    ids, extra = VARIANTS[variant](idx, question)
    trace = idx.pack_trace(idx.tl.trace, ids)
    ctx = [idx.chunks[i]["text"] for i in ids]
    text, llm_s = llm(ANSWER_PROMPT.format(context="\n\n---\n\n".join(ctx), question=question), model)
    return {"answer": text, "context": ctx, "context_sources": [idx.chunks[i]["section"] for i in ids],
            "extra": extra, "trace": trace, "llm_calls": 1 + extra.get("extra_llm_calls", 0),
            "total_s": time.perf_counter() - t0}
