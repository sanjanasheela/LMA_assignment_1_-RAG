"""Runs all variants on the open-ended GPT questions over the ORIGINAL data/ and stores full outputs (answers, contexts) for manual review."""
import argparse, json, os, re
from concurrent.futures import ThreadPoolExecutor, as_completed
import rag_lib as R

ap = argparse.ArgumentParser()
ap.add_argument("--model", default="haiku"); ap.add_argument("--workers", type=int, default=5)
ap.add_argument("--out", default="results_open.json")
ap.add_argument("--variants", default="v0_closed_book,v1_baseline,v2_rerank,v2b_rerank8,v3_hier_rerank,v4_hybrid,v5_graph,v6_agentic")
a = ap.parse_args()
qs = json.load(open("questions_open.json"))
store = json.load(open(a.out)) if os.path.exists(a.out) else {"model": a.model, "data": "data (original SRD)", "runs": {}}
idx = R.Index("data", "chroma_orig")
print("index ready", len(idx.chunks), flush=True)
tasks = [(v, q) for v in a.variants.split(",") for q in qs
         if f"{v}|{q['id']}" not in store["runs"] or store["runs"][f"{v}|{q['id']}"]["answer"].startswith("ERROR")]
print(len(tasks), "tasks", flush=True)
ABSTAIN = re.compile(r"(does not|doesn't|do not|don't|not) (contain|include|provide|mention|specify|say|state|cover|describe)|no information|not (provided|included|mentioned|found)|missing", re.I)


def work(v, q):
    r = R.answer(idx, v, q["question"], a.model)
    r.update(qid=q["id"], category=q["category"], question=q["question"], answerable=q["answerable"],
             abstained=bool(ABSTAIN.search(r["answer"])), ctx_chars=sum(map(len, r["context"])), n_ctx=len(r["context"]))
    return v, q, r


n = 0
with ThreadPoolExecutor(a.workers) as ex:
    for f in as_completed([ex.submit(work, v, q) for v, q in tasks]):
        v, q, r = f.result(); n += 1
        store["runs"][f"{v}|{q['id']}"] = r
        json.dump(store, open(a.out, "w"), indent=1, ensure_ascii=False)
        print(f"[{n}/{len(tasks)}] {v:15s} {q['id']}", flush=True)
print("ALL DONE", flush=True)
