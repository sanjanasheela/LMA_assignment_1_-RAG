"""Multi-metric evaluation of results_open.json (open-ended questions, no gold answers).

Automatic (no LLM):  entity_hit, abstained, ctx size, LLM calls, seconds
Judged by isolated Haiku (claude -p):
  faithfulness     share of the answer's claims supported by the retrieved context (not for closed-book)
  relevance, completeness   0-2 each, from question + answer only
  ctx_precision    share of retrieved chunks relevant to the question
  correctness      0-2 vs an ORACLE REFERENCE answer written from the full sections of the entities named in the question
Writes eval_open.json (all judgements, resumable) and review/metrics_open.md
"""
import json, os, re, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import rag_lib as R

RES = sys.argv[1] if len(sys.argv) > 1 else "results_open.json"
OUT = sys.argv[2] if len(sys.argv) > 2 else "eval_open.json"
METRICS_MD = sys.argv[3] if len(sys.argv) > 3 else "review/metrics_open.md"
runs = json.load(open(RES))["runs"]
qs = {q["id"]: q for q in json.load(open("questions_open.json"))}
ev = json.load(open(OUT)) if os.path.exists(OUT) else {"ref": {}, "judge": {}}
idx = R.Index("data", "chroma_orig")


def jparse(text, kind):
    m = re.search(r"\{.*\}" if kind == "obj" else r"\[.*\]", text, flags=re.S)
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


# ---- oracle references from full entity sections
def make_ref(qid):
    q = qs[qid]
    ents = idx.query_entities(q["question"])
    if not ents:
        return qid, None
    text, used = "", []
    for e in ents[:3]:
        t = "\n".join(idx.chunks[i]["text"] for i in idx.ent_chunks[e])
        if len(text) + len(t) > 9000:
            t = t[:max(0, 9000 - len(text))]
        text += f"\n\n### {e}\n{t}"; used.append(e)
    out, _ = R.llm("Answer the question using ONLY the source text below. Be complete and precise. If the text does not answer the "
                   "question, output exactly NOT ANSWERABLE.\n\nSource text:" + text + "\n\nQuestion: " + q["question"] + "\nAnswer:")
    return qid, {"entities": used, "answer": out}


todo = [q for q in qs if q not in ev["ref"]]
with ThreadPoolExecutor(6) as ex:
    for qid, ref in ex.map(make_ref, todo):
        ev["ref"][qid] = ref
json.dump(ev, open(OUT, "w"), indent=1, ensure_ascii=False)
print("references:", sum(1 for v in ev["ref"].values() if v and "NOT ANSWERABLE" not in v["answer"]), "usable /", len(qs), flush=True)


# ---- judges
def judge_run(item):
    key, r = item
    q = qs[r["qid"]]["question"]; a = r["answer"]; res = {}
    if r["context"]:
        out, _ = R.llm("Context:\n" + "\n\n---\n\n".join(r["context"]) + f"\n\nAnswer:\n{a}\n\nList the factual claims made in the Answer. "
                       "Count how many are directly supported by the Context. Statements like 'the context does not say X' are not claims. "
                       'Output ONLY JSON: {"claims": N, "supported": M}')
        j = jparse(out, "obj")
        if j and j.get("claims") is not None:
            res["faith"] = None if j["claims"] == 0 else min(1.0, j["supported"] / j["claims"]); res["claims"] = j["claims"]
        out, _ = R.llm(f"Question: {q}\n\nNumbered passages:\n" + "\n".join(f"[{i+1}] {c[:700]}" for i, c in enumerate(r["context"])) +
                       "\n\nFor each passage, is it relevant to answering the question (contains information that helps answer it)? "
                       "Output ONLY a JSON list of true/false in order.")
        j = jparse(out, "list")
        if j and len(j) == len(r["context"]):
            res["ctx_precision"] = sum(bool(x) for x in j) / len(j)
    out, _ = R.llm(f"Question: {q}\n\nAnswer:\n{a}\n\nRate the answer WITHOUT outside reference. relevance: 0 = off-topic, 1 = partly on topic, "
                   "2 = directly addresses the question. completeness: 0 = answers little/nothing, 1 = some parts, 2 = answers all parts the "
                   "question asks for (saying the information is unavailable counts as 0 completeness). "
                   'Output ONLY JSON: {"relevance": 0-2, "completeness": 0-2}')
    j = jparse(out, "obj")
    if j:
        res["relevance"], res["completeness"] = j.get("relevance"), j.get("completeness")
    ref = ev["ref"].get(r["qid"])
    if ref and "NOT ANSWERABLE" not in ref["answer"]:
        out, _ = R.llm(f"Question: {q}\n\nReference answer (from the full source text):\n{ref['answer']}\n\nCandidate answer:\n{a}\n\n"
                       "Is the candidate correct compared with the reference? 0 = wrong, contradicts it, or says the information is missing; "
                       "1 = partly correct or missing key parts; 2 = correct and covers the key content (extra detail is fine). "
                       'Output ONLY JSON: {"correct": 0-2}')
        j = jparse(out, "obj")
        if j:
            res["correct"] = j.get("correct")
    return key, res


todo = [(k, r) for k, r in runs.items() if k not in ev["judge"] and not r["answer"].startswith("ERROR")]
print(len(todo), "runs to judge", flush=True)
with ThreadPoolExecutor(6) as ex:
    for n, (k, res) in enumerate(ex.map(judge_run, todo), 1):
        ev["judge"][k] = res
        if n % 25 == 0:
            json.dump(ev, open(OUT, "w"), indent=1, ensure_ascii=False); print(n, flush=True)
json.dump(ev, open(OUT, "w"), indent=1, ensure_ascii=False)

# ---- aggregate
VORDER = ["v0_closed_book", "v1_baseline", "v2_rerank", "v2b_rerank8", "v3_hier_rerank", "v4_hybrid", "v5_graph", "v6_agentic"]


def entity_hit(r):
    ents = idx.query_entities(qs[r["qid"]]["question"])
    if not ents or not r.get("context_sources"):
        return None
    secs = " ".join(r["context_sources"]).lower()
    return float(np.mean([e in secs for e in ents]))


rows = []
for v in VORDER:
    rs = [(k, r) for k, r in runs.items() if k.startswith(v + "|")]
    g = lambda f: [ev["judge"][k][f] for k, _ in rs if ev["judge"].get(k, {}).get(f) is not None]
    mean = lambda x: float(np.mean(x)) if x else float("nan")
    eh = [x for x in (entity_hit(r) for _, r in rs) if x is not None]
    unans = [r for _, r in rs if r["answerable"] == "no"]
    ans = [r for _, r in rs if r["answerable"] == "yes"]
    rows.append(dict(v=v, n=len(rs), correct=mean(g("correct")) / 2, nc=len(g("correct")), faith=mean(g("faith")), rel=mean(g("relevance")) / 2,
                     comp=mean(g("completeness")) / 2, prec=mean(g("ctx_precision")), ent=mean(eh),
                     abst_ok=mean([r["abstained"] for r in unans]), abst_bad=mean([r["abstained"] for r in ans]),
                     calls=mean([r["llm_calls"] for _, r in rs]), secs=mean([r["total_s"] for _, r in rs])))
f = lambda x: "  -  " if x != x else f"{100 * x:5.1f}%"
hdr = f"{'variant':16s} {'n':>3s} {'correct':>8s} {'faithful':>8s} {'relev.':>7s} {'compl.':>7s} {'ctx prec':>8s} {'entity hit':>10s} {'abst@unans':>10s} {'abst@ans':>9s} {'calls':>5s} {'sec':>5s}"
lines = [hdr]
for r in sorted(rows, key=lambda r: -(r["correct"] if r["correct"] == r["correct"] else 0)):
    lines.append(f"{r['v']:16s} {r['n']:3d} {f(r['correct']):>8s} {f(r['faith']):>8s} {f(r['rel']):>7s} {f(r['comp']):>7s} {f(r['prec']):>8s} {f(r['ent']):>10s} "
                 f"{f(r['abst_ok']):>10s} {f(r['abst_bad']):>9s} {r['calls']:5.1f} {r['secs']:5.1f}")
table = "\n".join(lines)
cats = sorted({q["category"] for q in qs.values()})
bycat = ["correctness vs oracle reference, by category"] + [f"{'variant':16s} " + " ".join(f"{c:>10s}" for c in cats)]
for v in VORDER:
    cells = []
    for c in cats:
        x = [ev["judge"][k]["correct"] / 2 for k, r in runs.items() if k.startswith(v + "|") and r["category"] == c and ev["judge"].get(k, {}).get("correct") is not None]
        cells.append(f"{100 * np.mean(x):9.1f}%" if x else f"{'-':>10s}")
    bycat.append(f"{v:16s} " + " ".join(cells))
os.makedirs("review", exist_ok=True)
open(METRICS_MD, "w").write("```\n" + table + "\n\n" + "\n".join(bycat) + "\n```\n")
print(table); print(); print("\n".join(bycat))
