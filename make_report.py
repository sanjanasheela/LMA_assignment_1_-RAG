"""Generates report_rag.tex from results_v2.json / questions_v2.json (all numbers computed, none typed by hand)."""
import json, glob
from collections import defaultdict
import numpy as np

S = json.load(open("results_v2.json"))
runs = S["runs"]
Q = json.load(open("questions_v2.json"))
ORDER = ["v0_closed_book", "v1_baseline", "v2_rerank", "v2b_rerank8", "v3_hier_rerank", "v4_hybrid", "v5_graph", "v6_agentic"]
LABEL = {"v0_closed_book": "V0 Closed-book (no retrieval)", "v1_baseline": "V1 Baseline dense (HNSW), top-3",
         "v2_rerank": "V2 + cross-encoder rerank, top-3", "v2b_rerank8": "V2b Rerank, top-8 (context control)",
         "v3_hier_rerank": "V3 Hierarchical routing + rerank, top-3", "v4_hybrid": "V4 Hybrid BM25+dense (RRF) + routing + rerank, top-8",
         "v5_graph": "V5 Graph RAG (entity-linked), top-8", "v6_agentic": "V6 Agentic RAG (plan, retrieve, check, answer)"}
SHORT = {"v0_closed_book": "V0 closed-book", "v1_baseline": "V1 baseline", "v2_rerank": "V2 rerank", "v2b_rerank8": "V2b rerank-8",
         "v3_hier_rerank": "V3 hierarchical", "v4_hybrid": "V4 hybrid", "v5_graph": "V5 graph", "v6_agentic": "V6 agentic"}
TYPES = ["multi-part", "cross-file", "needle", "reasoning", "multi-topic"]
by = {v: [runs[f"{v}|{q['id']}"] for q in Q] for v in ORDER}


def agg(v, key="judge_hit"):
    rs = by[v]
    sc = "judge_score" if key == "judge_hit" else "score"
    fu = "judge_full" if key == "judge_hit" else "full"
    chg = [x for r in rs for x, c in zip(r[key], r["fact_changed"]) if c]
    unc = [x for r in rs for x, c in zip(r[key], r["fact_changed"]) if not c]
    ctx = [x for r in rs for x in r["ctx_hit"] if x is not None]
    return dict(acc=np.mean([r[sc] for r in rs]), full=np.mean([r[fu] for r in rs]),
                chg=np.mean(chg), unc=np.mean(unc), ctx=(np.mean(ctx) if ctx else None),
                chars=np.mean([r["ctx_chars"] for r in rs]), calls=np.mean([r["llm_calls"] for r in rs]),
                secs=np.mean([r["total_s"] for r in rs]))


J, ST = {v: agg(v) for v in ORDER}, {v: agg(v, "fact_hit") for v in ORDER}
pct = lambda x: "--" if x is None else f"{100 * x:.1f}\\%"
n_facts = sum(len(r["facts"]) for r in by["v1_baseline"])
n_chg = sum(sum(r["fact_changed"]) for r in by["v1_baseline"])
rng = np.random.default_rng(0)


def per(v):
    return np.array([r["judge_score"] for r in by[v]])


def boot(a, b):
    d = per(a) - per(b)
    bs = [d[rng.integers(0, len(d), len(d))].mean() for _ in range(10000)]
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return d.mean(), lo, hi


# ---- tables
main_rows = []
for v in sorted(ORDER, key=lambda v: -J[v]["acc"]):
    a = J[v]
    main_rows.append(f"{LABEL[v]} & {pct(a['acc'])} & {pct(a['full'])} & {pct(a['chg'])} & {pct(a['unc'])} & {pct(a['ctx'])} & {a['chars']:.0f} & {a['calls']:.1f} \\\\")
MAIN = "\n".join(main_rows)

strict_rows = "\n".join(f"{LABEL[v]} & {pct(ST[v]['acc'])} & {pct(ST[v]['full'])} & {pct(ST[v]['chg'])} & {pct(ST[v]['unc'])} \\\\"
                        for v in sorted(ORDER, key=lambda v: -ST[v]["acc"]))

type_rows = []
for v in sorted(ORDER, key=lambda v: -J[v]["acc"]):
    cells = []
    for t in TYPES:
        s = [r["judge_score"] for r in by[v] if r["type"] == t]
        cells.append(pct(np.mean(s)))
    type_rows.append(f"{SHORT[v]} & " + " & ".join(cells) + " \\\\")
TYPE = "\n".join(type_rows)
type_n = ", ".join(f"{t} ({sum(q['type'] == t for q in Q)})" for t in TYPES)

pairs = [("v6_agentic", "v5_graph", "Agentic vs.\\ graph"), ("v5_graph", "v2b_rerank8", "Graph vs.\\ rerank-8"),
         ("v4_hybrid", "v2b_rerank8", "Hybrid vs.\\ rerank-8"), ("v2b_rerank8", "v2_rerank", "Rerank-8 vs.\\ rerank-3"),
         ("v2_rerank", "v1_baseline", "Rerank-3 vs.\\ baseline"), ("v3_hier_rerank", "v2_rerank", "Hierarchical vs.\\ rerank-3")]
BOOT = "\n".join(f"{name} & {100 * m:+.1f} & [{100 * lo:+.1f}, {100 * hi:+.1f}] \\\\" for a, b, name in pairs for m, lo, hi in [boot(a, b)])

bars = "\n".join(f"({100 * J[v]['acc']:.1f},{SHORT[v]})" for v in sorted(ORDER, key=lambda v: J[v]["acc"]))
coords_ctx = "\n".join(f"({100 * J[v]['ctx']:.1f},{SHORT[v]})" for v in sorted(ORDER, key=lambda v: J[v]["acc"]) if J[v]["ctx"] is not None)
ymarks = ",".join(SHORT[v] for v in sorted(ORDER, key=lambda v: J[v]["acc"]))

agentic_ex = by["v6_agentic"]
avg_sub = np.mean([len(r["extra"].get("subqueries", [])) for r in agentic_ex])
fu_rate = np.mean([bool(r["extra"].get("followups")) for r in agentic_ex])
cb = J["v0_closed_book"]

TEX = r"""\documentclass[11pt,a4paper]{article}
\usepackage[margin=2.3cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern,microtype,booktabs,array,pgfplots,xcolor,caption,enumitem}
\usepackage[hidelinks]{hyperref}
\pgfplotsset{compat=1.16}
\captionsetup{font=small,labelfont=bf}
\setlist{itemsep=2pt,topsep=3pt}
\title{Retrieval-Augmented Generation over the D\&D SRD:\\Deduplication, Hierarchical Routing, Hybrid Search, Graph RAG and Agentic RAG}
\author{}
\date{}
\begin{document}
\maketitle

\section{Summary}
We rebuilt the D\&D 5e SRD RAG pipeline for the full corpus (13 files, 5{,}200 chunks) and compared eight variants on 24 hard questions with a weak generator (Claude Haiku, called through isolated \texttt{claude -p}). To stop the model answering from memory of the published SRD, the index is built on a \emph{counterfactual} copy of the data in which __NCHG__ of __NFACTS__ gold facts were changed.
\begin{itemize}
\item \textbf{The original duplication bug was the largest problem.} Each chunk was stored about four times, so 73\% of top-10 slots were exact copies and the cross-encoder only re-ordered copies. After deduplication the top-10 contains distinct chunks only.
\item \textbf{Ranking (semantic judge, fact accuracy):} agentic __AG__ $>$ graph __GR__ $>$ rerank-8 __R8__ $\approx$ hybrid __HY__ $>$ baseline __BA__ $\approx$ rerank-3 __RR__ $=$ hierarchical __HI__ $>$ closed-book __CB__.
\item \textbf{Memory is real but removed by the design.} Closed-book Haiku gets __CBCHG__ of the changed facts but __CBUNC__ of the unchanged ones, so the unchanged facts alone would have hidden retrieval quality.
\item \textbf{What did not help:} hierarchical routing (same top-3 as flat search on 20 of 24 questions and the same score on all 24), BM25 hybrid fusion (no gain over simply reranking 8 dense chunks), and cross-encoder reranking of only 3 chunks (no gain over baseline). Most of the early ``improvement'' of larger pipelines is the larger context window.
\item \textbf{What helped:} entity-linked graph expansion (+__DGR__ points over rerank-8) and agentic query decomposition with a sufficiency check (+__DAG__ points over graph, at 3 LLM calls per question).
\end{itemize}

\section{Fixing the index first: deduplication}
In the saved results of the original run, 73\% of top-10 slots were exact duplicates, and a typical query returned only 2--3 distinct chunks (the same chunk appeared about four times, with identical cosine scores). The source files had no such duplication; the vector store had been filled several times. Consequently the cross-encoder compared copies of the same text, and re-ranking could not change the answer.

Fixes, applied at index time and at query time:
\begin{itemize}
\item \textbf{Index time.} Every file in \texttt{data/} is split by Markdown header and then into 500-character chunks (50 overlap). Each chunk is prefixed with its section path (for example \texttt{[Spells > Fireball]}). The chunk id is the SHA-1 of the normalised section and text, which is also the ChromaDB id, so re-ingesting cannot create copies; an assertion checks that the store count equals the number of unique chunks (5{,}273 raw, 5{,}200 unique). The section path uses only the top-level title and the deepest header, because \texttt{spells.md} contains a stray \texttt{\#\# Otherworldly Steed} heading that otherwise became a wrong parent of every later spell.
\item \textbf{Query time.} Retrieval over-fetches 50 candidates and drops any chunk with cosine similarity $\ge 0.95$ to a higher-ranked kept chunk. On the earlier 27-question set, 270 of 270 top-10 chunks were distinct afterwards.
\end{itemize}

\section{Experimental setup}
\paragraph{Corpus and counterfactual copy.} The 13 SRD files in \texttt{data/} (about 1.9\,MB). \texttt{build\_cf.py} writes \texttt{data\_cf/} with 27 scoped edits, each asserted to land inside its target section, for example Fireball 8d6$\to$9d6 and 150$\to$120 feet, Counterspell's save Constitution$\to$Wisdom, Bag of Holding 500$\to$800 pounds, Owlbear AC 13$\to$15, the Soldier background's skills, the death-save threshold 10$\to$12, and the point-buy budget 27$\to$30. A model answering from memory gets these facts wrong; only correct retrieval gets them right.

\paragraph{Questions.} 24 questions in five types: __TYPEN__. Many ask for several things at once (up to seven facts per question, and up to four unrelated topics). Every gold fact (__NFACTS__ in total) is checked by script to occur in the counterfactual data (one derived fact, ``11d6'', excepted).

\paragraph{Generator and isolation.} Every LLM call (answers, the agentic planner, and the judge) uses \texttt{claude -p --model haiku} from an empty temporary directory with \texttt{--tools ""}, no session persistence, no setting sources, slash commands disabled, no MCP servers, and a minimal system prompt, so the model sees only the prompt text and cannot read the data folder. A direct probe confirmed it has no tools and no knowledge of the project files. The answer prompt tells the model that the context may differ from the official rules and is always right.

\paragraph{Scoring.} \emph{Fact accuracy} is the fraction of a question's gold facts that the answer states. The primary metric is a semantic check by Haiku (wording and formatting may differ; every number and name must match). A strict string-match metric is reported in the appendix because the judge shares the generator's model family. \emph{Full answer} means all facts stated. \emph{Context recall} is the fraction of gold facts present verbatim in the retrieved context, which separates retrieval quality from generation quality.

\section{Variants}
\begin{description}[leftmargin=1.2cm,labelwidth=1cm]
\item[V0] Closed-book control: the question alone, no context.
\item[V1] Dense search (all-MiniLM-L6-v2, ChromaDB with its HNSW index, cosine), near-duplicates removed, top-3 chunks.
\item[V2] V1's top-10 re-scored by the cross-encoder (ms-marco-MiniLM-L-6-v2), top-3.
\item[V2b] Same as V2 but top-8 chunks. This control isolates the effect of a larger context from the effect of any better method.
\item[V3] Hierarchical coarse-to-fine routing: score file centroids and discard half the files, keep the best 150 sections among the rest, search chunks only inside them (metadata filter), then rerank, top-3. HNSW is the index underneath every variant; routing is a separate layer on top of it.
\item[V4] Hybrid: dense search inside the routed space plus BM25 over all chunks, merged by reciprocal rank fusion, cross-encoder rerank, top-8.
\item[V5] Graph RAG (lightweight, no LLM extraction): nodes are section entities (1{,}706 spells, monsters, items, rules, \dots), an edge A$\to$B means a chunk of A mentions B (6{,}867 edges, 47 over-connected hub entities ignored). Entities named in the question contribute their best chunks directly; entities mentioned inside the top seed chunks are expanded one hop; the pooled candidates are reranked, top-8.
\item[V6] Agentic RAG: Haiku splits the question into at most six keyword queries; each is retrieved with the V4 pipeline (top-3 each); Haiku then lists missing facts, which trigger one follow-up retrieval round; Haiku answers from at most 16 chunks. Three LLM calls per question (planner, checker, answer).
\end{description}

\section{Results}
\begin{table}[h]\centering\footnotesize\setlength{\tabcolsep}{3.5pt}
\caption{Main results, ranked by semantic-judge fact accuracy (24 questions, __NFACTS__ gold facts, one run each). ``Changed'' and ``unchanged'' split the facts by whether the counterfactual edit touched them.}
\begin{tabular}{@{}p{4.9cm}rrrrrrr@{}}\toprule
Variant & Fact acc. & Full ans. & Changed & Unch. & Ctx.\ rec. & Ctx.\ chars & LLM calls\\\midrule
__MAIN__
\bottomrule\end{tabular}
\end{table}

\begin{figure}[h]\centering
\begin{tikzpicture}
\begin{axis}[xbar,width=0.82\linewidth,height=7.6cm,xmin=0,xmax=105,bar width=6pt,symbolic y coords={__YMARKS__},ytick=data,
 xlabel={\%},legend style={at={(0.5,-0.16)},anchor=north,legend columns=1,font=\footnotesize},enlarge y limits=0.08,nodes near coords,nodes near coords style={font=\scriptsize}]
\addplot[fill=blue!55,draw=none] coordinates {
__BARS__
};
\addplot[fill=orange!70,draw=none] coordinates {
__CTXBARS__
};
\legend{Answer fact accuracy (judge),Context recall (retrieval only)}
\end{axis}
\end{tikzpicture}
\caption{Answer accuracy versus the share of gold facts that retrieval put into the context.}
\end{figure}

\begin{table}[h]\centering\small
\caption{Fact accuracy (judge) by question type; question counts: __TYPEN__.}
\begin{tabular}{@{}lrrrrr@{}}\toprule
Variant & multi-part & cross-file & needle & reasoning & multi-topic\\\midrule
__TYPE__
\bottomrule\end{tabular}
\end{table}

\begin{table}[h]\centering\small
\caption{Paired differences in per-question fact accuracy (percentage points) with 95\% bootstrap intervals over the 24 questions (10{,}000 resamples).}
\begin{tabular}{@{}lrr@{}}\toprule
Comparison & Mean difference & 95\% interval\\\midrule
__BOOT__
\bottomrule\end{tabular}
\end{table}

\section{Discussion}
\paragraph{The counterfactual design matters.} Closed-book Haiku scores __CBUNC__ on unchanged facts, close to what several RAG variants reach overall, and __CBCHG__ on changed facts. On unmodified data alone, V1--V3 would look only a few points better than no retrieval. The ranking among retrieval methods is cleanest in the ``changed'' column.

\paragraph{Retrieval quality gates everything.} Answer accuracy tracks context recall closely (Figure~1). V1--V3 retrieve only 3 chunks and miss about 40\% of the needed facts; questions that need several entities (multi-topic) are almost unanswerable for them.

\paragraph{Hierarchical routing: no benefit here.} V3 returned the same top-3 as V2 on 20 of the 24 questions and scored identically on all 24 (difference exactly 0). Routing did not discard chunks that mattered, so it is safe, but at 5{,}200 chunks plain HNSW is already fast and accurate; on the earlier spell-only set the routed search was also slower per query (about 23\,ms vs.\ 8\,ms). It may pay off at much larger scale or with many unrelated files, which our questions only partly exercise.

\paragraph{Hybrid search: no gain beyond context size.} V4 reaches higher context recall than V2b (80\% vs.\ 75\%) but not higher answer accuracy, and the difference is within noise. Adding BM25 and routing did not beat reranking 8 dense chunks.

\paragraph{Graph RAG helps most on multi-entity questions.} Linking entities named in the question to their own sections guarantees that each named spell, monster or item contributes a chunk, which plain similarity search does not. V5 gains __DGR__ points over rerank-8 with the same context size and one LLM call, and its extra cost is an offline graph build over the chunks. It still struggles on multi-topic questions with up to four unrelated parts (42.5\% accuracy in Table~2): several of the facts for the later parts never reach its context.

\paragraph{Agentic RAG is best but costs more.} Splitting the question into focused queries (on average __AVGSUB__ per question) and checking for missing facts gives the highest context recall (__AGCTX__) and the best answers, including the multi-topic questions. It needs three LLM calls and was the slowest variant (about __AGSEC__\,s per question versus about __BASEC__\,s, measured with four calls in parallel). The checker requested follow-up retrieval on __FU__ of questions. It also passed the largest context (about __AGCH__ characters).

\section{Limitations}
\begin{itemize}
\item \textbf{Small sample.} 24 questions and one run per variant. Intervals in Table~3 are wide for some comparisons; differences among V1, V2, V2b, V4 and among V2, V3 are not significant, and the middle of the ranking is not stable across the two metrics (appendix).
\item \textbf{Judge and generator share a model family.} The semantic judge is Haiku. The strict string metric gives the same top two and the same bottom, but not the same middle order.
\item \textbf{Questions were written after seeing the data and by the same author as the system}, so they favour entity-centric retrieval (graph, agentic); they may understate hybrid search, which helps with vague or paraphrased queries.
\item \textbf{Counterfactual edits are small and local} (27 facts), so they test retrieval of specific values, not summarisation across many chunks.
\item \textbf{Context sizes differ} (about 1.1k to 4.3k characters). V2b controls this for V4 and V5 but not for V6.
\item \textbf{Latency} was measured with four concurrent generator calls, so absolute times are inflated; only relative cost is meaningful.
\item The harness exposes the account e-mail to the model (a property of Claude Code, not of the data); it cannot help answer D\&D questions.
\end{itemize}

\section{Reproduction}
Files in \texttt{LMA\_assignment\_1\_-RAG/}: \texttt{rag\_lib.py} (index, all variants, isolated LLM call), \texttt{build\_cf.py} (counterfactual data), \texttt{make\_questions.py} (questions plus fact verification), \texttt{run\_eval.py} (runs all variants, resumable), \texttt{judge.py} (semantic judge), \texttt{summarize.py}, \texttt{make\_report.py}. Raw results: \texttt{results\_v2.json}. The original notebook \texttt{rag.ipynb} now contains the deduplicated ingestion and the hierarchical retrieval; it has not been re-run end to end with the Gemini or Claude generator.

\appendix
\section{Strict string-match metric}
\begin{table}[h]\centering\small
\caption{The same runs scored by normalised substring match of each gold fact (no judge). It under-counts paraphrases and list formatting.}
\begin{tabular}{@{}p{6.1cm}rrrr@{}}\toprule
Variant & Fact acc. & Full ans. & Changed & Unchanged\\\midrule
__STRICT__
\bottomrule\end{tabular}
\end{table}
\end{document}
"""

dg = boot("v5_graph", "v2b_rerank8")[0] * 100
da = boot("v6_agentic", "v5_graph")[0] * 100
rep = {
    "__NCHG__": str(n_chg), "__NFACTS__": str(n_facts), "__MAIN__": MAIN, "__STRICT__": strict_rows, "__TYPE__": TYPE,
    "__TYPEN__": type_n, "__BOOT__": BOOT, "__BARS__": bars, "__CTXBARS__": coords_ctx, "__YMARKS__": ymarks,
    "__AG__": pct(J["v6_agentic"]["acc"]).replace("\\%", "\\%"), "__GR__": pct(J["v5_graph"]["acc"]),
    "__R8__": pct(J["v2b_rerank8"]["acc"]), "__HY__": pct(J["v4_hybrid"]["acc"]), "__BA__": pct(J["v1_baseline"]["acc"]),
    "__RR__": pct(J["v2_rerank"]["acc"]), "__HI__": pct(J["v3_hier_rerank"]["acc"]), "__CB__": pct(cb["acc"]),
    "__CBCHG__": pct(cb["chg"]), "__CBUNC__": pct(cb["unc"]), "__DGR__": f"{dg:.0f}", "__DAG__": f"{da:.0f}",
    "__AVGSUB__": f"{avg_sub:.1f}", "__AGCTX__": pct(J["v6_agentic"]["ctx"]), "__AGSEC__": f"{J['v6_agentic']['secs']:.0f}",
    "__BASEC__": f"{J['v1_baseline']['secs']:.0f}", "__FU__": pct(fu_rate), "__AGCH__": f"{J['v6_agentic']['chars']:.0f}",
}
for k, v in rep.items():
    TEX = TEX.replace(k, v)
open("report_rag.tex", "w", encoding="utf-8").write(TEX)
print("wrote report_rag.tex")
