"""Runs every variant on every question with Haiku (isolated claude -p), scores fact coverage, resumable.
Usage: python run_eval.py [--model haiku] [--workers 4] [--variants v0_closed_book,v1_baseline,...]
"""
import argparse, glob, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
import rag_lib as R

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="haiku")
ap.add_argument("--workers", type=int, default=4)
ap.add_argument("--variants", default="v0_closed_book,v1_baseline,v2_rerank,v2b_rerank8,v3_hier_rerank,v4_hybrid,v5_graph,v6_agentic")
ap.add_argument("--out", default="results_v2.json")
args = ap.parse_args()

qs = json.load(open("questions_v2.json"))
orig = R.norm(" ".join(open(f, encoding="utf-8-sig").read() for f in glob.glob("data/*.md")))
changed = lambda fact: f" {R.norm(fact)} " not in f" {orig} "   # fact does not exist in the real SRD text

store = json.load(open(args.out)) if os.path.exists(args.out) else {"model": args.model, "runs": {}}
store["model"] = args.model
idx = R.Index("data_cf", "chroma_cf")
print("index ready:", len(idx.chunks), "chunks", flush=True)

tasks = [(v, q) for v in args.variants.split(",") for q in qs
         if f"{v}|{q['id']}" not in store["runs"] or store["runs"][f"{v}|{q['id']}"]["answer"].startswith("ERROR")]
print(len(tasks), "tasks to run", flush=True)


def score(res, q):
    facts = q["facts"] + q["derived_facts"]
    hit = [R.has_fact(res["answer"], f) for f in facts]
    ctx = " ".join(res["context"])
    res.update(qid=q["id"], type=q["type"], facts=facts, fact_hit=hit,
               fact_changed=[changed(f) for f in q["facts"]] + [True] * len(q["derived_facts"]),
               ctx_hit=[R.has_fact(ctx, f) for f in q["facts"]] + [None] * len(q["derived_facts"]),
               score=sum(hit) / len(facts), full=all(hit), ctx_chars=len(ctx))
    return res


def work(v, q):
    return v, q, score(R.answer(idx, v, q["question"], args.model), q)


done = 0
with ThreadPoolExecutor(args.workers) as ex:
    futs = [ex.submit(work, v, q) for v, q in tasks]
    for f in as_completed(futs):
        v, q, res = f.result()
        store["runs"][f"{v}|{q['id']}"] = res
        done += 1
        json.dump(store, open(args.out, "w"), indent=1, ensure_ascii=False)
        print(f"[{done}/{len(tasks)}] {v:15s} q{q['id']:<2d} score {res['score']:.2f}  llm_calls {res['llm_calls']}", flush=True)
print("done", flush=True)
