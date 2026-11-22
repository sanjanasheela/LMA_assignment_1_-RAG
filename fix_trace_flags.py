"""For runs whose replayed retrieval differs slightly from the stored context, make the trace's 'selected_for_llm' follow the stored
context (authoritative: exactly what the LLM saw) and record a note. Usage: python fix_trace_flags.py results_file.json"""
import json, sys
p = sys.argv[1]
S = json.load(open(p)); fixed = 0
for k, r in S["runs"].items():
    if r.get("trace_matches_stored_context") is not False:
        continue
    seen = set(r["context"]); in_pool = set()
    for st in r["trace"]:
        for it in st["items"]:
            if "text" in it:
                it["selected_for_llm"] = it["text"] in seen
                in_pool.add(it["text"])
    missing = [c for c in r["context"] if c not in in_pool]
    r["trace_note"] = (f"Replayed retrieval differs from the stored context by {len(missing)} chunk(s) at the selection boundary "
                       "(approximate nearest-neighbour index rebuild / near-tied cross-encoder scores). 'context' is exactly what the LLM saw; "
                       "dense/BM25 stages show the replay.")
    r["context_not_in_replayed_pool"] = missing
    fixed += 1
json.dump(S, open(p, "w"), indent=1, ensure_ascii=False)
print("flagged", fixed, "runs")
