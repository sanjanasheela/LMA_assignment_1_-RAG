"""Runs the LangChain/LangGraph variants on questions_v2.json (counterfactual data) and stores results in the same schema as run_eval.py,
so judge.py, summarize.py and retrieval_eval.py work on the output unchanged.   Usage: python run_lc.py [--out results_lc.json] [--workers 4]"""
import argparse, glob, json, time
import rag_lc as L

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="results_lc.json"); ap.add_argument("--workers", type=int, default=4)
ap.add_argument("--variants", default="v1_baseline,v2_rerank,v2b_rerank8,v3_hier_rerank,v4_hybrid,v5_graph,v6_agentic")
args = ap.parse_args()

qs = json.load(open("questions_v2.json"))
orig = L.norm(" ".join(open(f, encoding="utf-8-sig").read() for f in glob.glob("data/*.md")))
has = lambda text, fact: f" {L.norm(fact)} " in f" {L.norm(text)} "
stack = L.Stack("data_cf", "chroma_lc")
print("index ready:", len(stack.docs), "chunks", flush=True)
store = {"model": "haiku", "framework": "langchain+langgraph", "runs": {}}
for v in args.variants.split(","):
    stats = [L.CallStats() for _ in qs]
    outs = stack.variants[v].batch([q["question"] for q in qs], config=[{"callbacks": [s], "max_concurrency": args.workers} for s in stats],
                                   )
    for q, o, st in zip(qs, outs, stats):
        facts = q["facts"] + q["derived_facts"]; ctx_docs = [d.page_content for d in o["docs"]]; ctx = " ".join(ctx_docs)
        hit = [has(o["answer"], f) for f in facts]
        store["runs"][f"{v}|{q['id']}"] = dict(
            answer=o["answer"], context=ctx_docs, context_sources=[d.metadata["section"] for d in o["docs"]], extra={}, llm_calls=st.calls,
            total_s=st.secs, qid=q["id"], type=q["type"], facts=facts, fact_hit=hit,
            fact_changed=[f" {L.norm(f)} " not in f" {orig} " for f in q["facts"]] + [True] * len(q["derived_facts"]),
            ctx_hit=[has(ctx, f) for f in q["facts"]] + [None] * len(q["derived_facts"]),
            score=sum(hit) / len(facts), full=all(hit), ctx_chars=len(ctx))
    json.dump(store, open(args.out, "w"), indent=1, ensure_ascii=False)
    print(v, "mean score", sum(r["score"] for k, r in store["runs"].items() if k.startswith(v + "|")) / len(qs), flush=True)
print("done")
