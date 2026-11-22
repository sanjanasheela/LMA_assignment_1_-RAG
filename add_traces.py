"""Adds the full retrieval trace (dense/BM25 ranks, cross-encoder scores, pool origins, selected chunks) to a results file
by replaying retrieval only (no LLM calls). Verifies the replayed final context equals the stored one.
Usage: python add_traces.py results_v2.json questions_v2.json data_cf [chroma_scratch_dir]
"""
import json, sys, shutil
import rag_lib as R

res_path, q_path, data_dir = sys.argv[1:4]
chroma = sys.argv[4] if len(sys.argv) > 4 else "/tmp/chroma_trace"
store = json.load(open(res_path))
shutil.copy(res_path, res_path + ".bak")
qs = {str(q["id"]) if not str(q["id"]).startswith("o") else q["id"]: q for q in json.load(open(q_path))}
idx = R.Index(data_dir, chroma)
mism = n = 0
for key, r in store["runs"].items():
    v, qid = key.split("|")
    if v == "v0_closed_book":
        r["trace"] = []; continue
    q = qs[qid]["question"]
    idx.tl.trace = []
    if v == "v6_agentic":
        ids, _ = R.v6_agentic(idx, q, replay=(r["extra"]["subqueries"], r["extra"].get("followups") or []))
    else:
        ids, _ = R.VARIANTS[v](idx, q)
    r["trace"] = idx.pack_trace(idx.tl.trace, ids)
    same = [idx.chunks[i]["text"] for i in ids] == r["context"]
    n += 1; mism += (not same)
    r["trace_matches_stored_context"] = same
    if not same:
        print("MISMATCH", key, flush=True)
json.dump(store, open(res_path, "w"), indent=1, ensure_ascii=False)
print(f"traces added to {n} runs; {mism} replayed contexts differ from the stored ones")
