"""Exports stored LLM outputs for manual checking.

review/<name>.csv : one row per (question, variant): answer, retrieved sections, auto signals, EMPTY manual-grade columns
review/<name>.md  : question by question, all variants side by side, with the re-ranking table and full retrieved context in <details>
review/<name>_candidates.csv : every candidate chunk at every retrieval stage (dense rank, BM25 rank, graph-pool origin,
                               cross-encoder pre-rank / re-rank / score, whether it reached the LLM)
"""
import csv, json, os, sys

VORDER = ["v0_closed_book", "v1_baseline", "v2_rerank", "v2b_rerank8", "v3_hier_rerank", "v4_hybrid", "v5_graph", "v6_agentic"]
os.makedirs("review", exist_ok=True)


def export(results_path, questions_path, name, kind):
    runs = json.load(open(results_path))["runs"]
    qs = json.load(open(questions_path))
    qid = (lambda q: f"q{q['id']}") if kind == "cf" else (lambda q: q["id"])
    cols = ["qid", "type_or_category", "question", "variant", "answer", "n_ctx_chunks", "ctx_chars", "llm_calls", "seconds",
            "retrieved_sections", "agentic_subqueries"]
    cols += (["gold_facts", "facts_found_judge", "facts_found_strict", "facts_in_context"] if kind == "cf"
             else ["answerable_from_srd", "abstained_auto"])
    cols += ["MANUAL_correct_0_1_2", "MANUAL_complete_0_1_2", "MANUAL_faithful_Y_N", "MANUAL_notes"]
    md = [f"# Manual review: {name}\n",
          "Grade each answer against the SRD text. Suggested scale: correct 0 = wrong/missing, 1 = partly right, 2 = fully right; "
          "complete 0/1/2 = share of the question's parts answered; faithful Y/N = every claim is supported by the retrieved context.\n"]
    cand_fh = open(f"review/{name}_candidates.csv", "w", newline="", encoding="utf-8-sig")
    cw = csv.writer(cand_fh)
    cw.writerow(["qid", "variant", "stage", "stage_query", "section", "source", "chunk_id", "rank", "cosine_dist", "bm25", "origin",
                 "pre_rank", "ce_rank", "ce_score", "selected_for_llm", "text"])
    with open(f"review/{name}.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh); w.writerow(cols)
        for q in qs:
            md.append(f"\n---\n\n## {qid(q)} ({q.get('type') or q.get('category')}) {q['question']}\n")
            if kind == "cf":
                md.append("**Gold facts (counterfactual data):** " + "; ".join(q["facts"] + q["derived_facts"]) + "\n")
            else:
                md.append(f"**Answerable from the SRD:** {q['answerable']}\n")
            for v in VORDER:
                r = runs.get(f"{v}|{q['id']}")
                if not r:
                    continue
                secs = r.get("context_sources") or [it["section"] for st in r.get("trace", []) for it in st["items"] if it["selected_for_llm"] and st["stage"] == "rerank"][:len(r["context"])]
                sub = r.get("extra", {}).get("subqueries", [])
                row = [qid(q), q.get("type") or q.get("category"), q["question"], v, r["answer"], len(r["context"]), sum(map(len, r["context"])),
                       r["llm_calls"], round(r["total_s"], 1), " | ".join(secs), " | ".join(sub)]
                if kind == "cf":
                    row += ["; ".join(r["facts"]), "; ".join(f for f, h in zip(r["facts"], r["judge_hit"]) if h),
                            "; ".join(f for f, h in zip(r["facts"], r["fact_hit"]) if h),
                            "; ".join(f for f, h in zip(r["facts"], r["ctx_hit"]) if h)]
                else:
                    row += [q["answerable"], r["abstained"]]
                w.writerow(row + ["", "", "", ""])
                for st in r.get("trace", []):
                    for it in st["items"]:
                        cw.writerow([qid(q), v, st["stage"], st.get("query", ""), it["section"], it["source"], it["chunk_id"], it.get("rank", ""),
                                     it.get("cosine_dist", ""), it.get("bm25", ""), it.get("origin", ""), it.get("pre_rank", ""),
                                     it.get("ce_rank", ""), it.get("ce_score", ""), it["selected_for_llm"], it.get("text", "")])
                md.append(f"\n### {v}  ({len(r['context'])} chunks, {r['llm_calls']} LLM call(s))\n")
                md.append(r["answer"] + "\n")
                if kind == "cf":
                    md.append(f"*facts found (judge): {sum(r['judge_hit'])}/{len(r['facts'])}; missing: " +
                              ("; ".join(f for f, h in zip(r['facts'], r['judge_hit']) if not h) or "none") + "*\n")
                if sub:
                    md.append("*agentic sub-queries:* " + " / ".join(sub) + "\n")
                if r.get("trace_note"):
                    md.append("*note:* " + r["trace_note"] + "\n")
                for st in r.get("trace", []):
                    if st["stage"] != "rerank":
                        continue
                    md.append(f"\n*re-ranking* (query: `{st['query'][:80]}`): candidate pool of {len(st['items'])}, ordered by cross-encoder score\n")
                    md.append("| CE rank | before-rerank rank | CE score | to LLM | section |\n|---|---|---|---|---|")
                    for it in st["items"][:20]:
                        md.append(f"| {it['ce_rank']} | {it['pre_rank']} | {it['ce_score']:.2f} | {'yes' if it['selected_for_llm'] else ''} | {it['section']} |")
                    md.append("")
                if secs:
                    md.append("*retrieved sections:* " + " | ".join(dict.fromkeys(secs)) + "\n")
                    ctx = "\n\n---\n\n".join(r["context"])
                    md.append(f"<details><summary>full retrieved context</summary>\n\n```\n{ctx}\n```\n</details>\n")
    cand_fh.close()
    open(f"review/{name}.md", "w", encoding="utf-8").write("\n".join(md))
    print(f"review/{name}.csv, review/{name}.md  ({len(qs)} questions)")


if __name__ == "__main__":
    which = sys.argv[1:] or ["cf", "open", "cf_qwen", "open_qwen"]
    if "cf" in which:
        export("results_v2.json", "questions_v2.json", "counterfactual_24q", "cf")
    if "open" in which:
        export("results_open.json", "questions_open.json", "open_41q", "open")
    if "cf_qwen" in which:
        export("results_v2_qwen.json", "questions_v2.json", "counterfactual_24q_qwen", "cf")
    if "open_qwen" in which:
        export("results_open_qwen.json", "questions_open.json", "open_41q_qwen", "open")
