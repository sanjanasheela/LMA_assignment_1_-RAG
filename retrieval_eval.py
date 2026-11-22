"""Retrieval-only metrics (no LLM). Ground truth = the gold facts of questions_v2.json located in the counterfactual corpus:
a chunk is relevant to a question if it contains >=1 gold fact (string match); its gain = number of distinct gold facts it contains.
Ranked list = the chunks actually sent to the generator, in the order sent (reranked order for reranked variants).
Metrics: Hit@k, Recall@k (share of gold facts covered by top-k), Precision@k, MRR, nDCG@k (graded), FullRecall@k (all facts covered).
Pool metrics (from stored traces): recall of the candidate pool, and MRR before vs after cross-encoder re-ranking.
Usage: python retrieval_eval.py [results_v2.json] [out.md]"""
import json, sys
import numpy as np
import rag_lib as R

RES = sys.argv[1] if len(sys.argv) > 1 else "results_v2.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "review/retrieval_metrics.md"
runs = json.load(open(RES))["runs"]
qs = {q["id"]: q for q in json.load(open("questions_v2.json"))}
idx = R.Index("data_cf", "chroma_cf")
text_of = {c["id"][:12]: c["text"] for c in idx.chunks}
KS = [1, 3, 5, 8]
VORDER = ["v1_baseline", "v2_rerank", "v2b_rerank8", "v3_hier_rerank", "v4_hybrid", "v5_graph", "v6_agentic"]


def gold(qid):
    return qs[qid]["facts"]


def facts_in(text, facts):
    return {i for i, f in enumerate(facts) if R.has_fact(text, f)}


# corpus-wide gains for the ideal DCG
ideal = {}
for qid in qs:
    g = sorted((len(facts_in(c["text"], gold(qid))) for c in idx.chunks), reverse=True)
    ideal[qid] = [x for x in g if x > 0]


def dcg(gains):
    return sum(g / np.log2(i + 2) for i, g in enumerate(gains))


def metrics(chunks_text, qid):
    facts = gold(qid)
    sets = [facts_in(t, facts) for t in chunks_text]
    out = {}
    first = next((i for i, s in enumerate(sets) if s), None)
    out["mrr"] = 0.0 if first is None else 1.0 / (first + 1)
    for k in KS:
        top = sets[:k]
        cov = set().union(*top) if top else set()
        out[f"hit@{k}"] = float(any(top))
        out[f"recall@{k}"] = len(cov) / len(facts)
        out[f"prec@{k}"] = sum(bool(s) for s in top) / max(1, len(top))
        out[f"full@{k}"] = float(len(cov) == len(facts))
        gains = [len(s) for s in top]
        idl = dcg(ideal[qid][:k])
        out[f"ndcg@{k}"] = dcg(gains) / idl if idl else 0.0
    return out


rows = {}
for v in VORDER:
    ms = [metrics(r["context"], r["qid"]) for k, r in runs.items() if k.startswith(v + "|")]
    rows[v] = {m: float(np.mean([x[m] for x in ms])) for m in ms[0]} | {"n": len(ms), "k": float(np.mean([len(r["context"]) for k, r in runs.items() if k.startswith(v + "|")]))}

f = lambda x: f"{100 * x:5.1f}%"
cols = ["mrr"] + [f"{m}@{k}" for k in (3, 8) for m in ("hit", "recall", "prec", "ndcg")] + ["full@8"]
lines = ["Final-context retrieval metrics, 24 counterfactual questions (ranked list = chunks sent to the LLM; k beyond a variant's context size uses all of its chunks)", "",
         f"{'variant':16s} {'chunks':>6s} " + " ".join(f"{c:>9s}" for c in cols)]
for v in sorted(VORDER, key=lambda v: -rows[v]["ndcg@8"]):
    r = rows[v]
    lines.append(f"{v:16s} {r['k']:6.1f} " + " ".join(f"{(r[c] if c=='mrr' else 100*r[c]):9.3f}" if c == "mrr" else f"{f(r[c]):>9s}" for c in cols))

# pool metrics from traces
lines += ["", "Candidate-pool metrics from traces (cross-encoder pool; MRR measured on the pool order before vs after re-ranking)", "",
          f"{'variant':16s} {'pool':>5s} {'pool recall':>11s} {'MRR before':>10s} {'MRR after':>9s} {'nDCG@8 before':>13s} {'nDCG@8 after':>12s}"]
for v in VORDER:
    pr, mb, ma, nb, na, ps = [], [], [], [], [], []
    for k, r in runs.items():
        if not k.startswith(v + "|"):
            continue
        st = [s for s in r.get("trace", []) if s["stage"] == "rerank"]
        if not st:
            continue
        items = st[0]["items"]
        by_pre = [text_of.get(i["chunk_id"], i.get("text", "")) for i in sorted(items, key=lambda i: i["pre_rank"])]
        by_ce = [text_of.get(i["chunk_id"], i.get("text", "")) for i in sorted(items, key=lambda i: i["ce_rank"])]
        facts = gold(r["qid"])
        pr.append(len(set().union(*[facts_in(t, facts) for t in by_pre])) / len(facts)); ps.append(len(items))
        b, a = metrics(by_pre, r["qid"]), metrics(by_ce, r["qid"])
        mb.append(b["mrr"]); ma.append(a["mrr"]); nb.append(b["ndcg@8"]); na.append(a["ndcg@8"])
    if pr:
        lines.append(f"{v:16s} {np.mean(ps):5.0f} {f(np.mean(pr)):>11s} {np.mean(mb):10.3f} {np.mean(ma):9.3f} {f(np.mean(nb)):>13s} {f(np.mean(na)):>12s}")
txt = "\n".join(lines)
open(OUT, "w").write("```\n" + txt + "\n```\n")
json.dump(rows, open(OUT.replace(".md", ".json"), "w"), indent=1)
print(txt)
