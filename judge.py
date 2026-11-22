"""Semantic fact check: for each saved answer, Haiku (isolated claude -p) says which gold facts the answer states."""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor
import rag_lib as R

path = sys.argv[1] if len(sys.argv) > 1 else "results_v2.json"
store = json.load(open(path))
qs = {q["id"]: q for q in json.load(open("questions_v2.json"))}

PROMPT = """You are grading answers to a rules question. For each numbered fact below, decide whether the Answer states that fact.
Wording, ordering, list formatting and spacing may differ, but every number, die, dice expression, name and condition in the fact must be stated with the same value. A fact the answer contradicts or omits is false.

Question: {q}

Answer:
{a}

Facts:
{facts}

Output ONLY a JSON list of true/false values, one per fact, in order."""


def judge(item):
    k, r = item
    facts = r["facts"]
    out, _ = R.llm(PROMPT.format(q=qs[r["qid"]]["question"], a=r["answer"],
                                 facts="\n".join(f"{i+1}. {f}" for i, f in enumerate(facts))), "haiku")
    m = re.search(r"\[.*?\]", out, flags=re.S)
    try:
        v = json.loads(m.group(0)); assert len(v) == len(facts)
        return k, [bool(x) for x in v]
    except Exception:
        return k, None


todo = [(k, r) for k, r in store["runs"].items() if "judge_hit" not in r]
print(len(todo), "to judge", flush=True)
with ThreadPoolExecutor(6) as ex:
    for n, (k, v) in enumerate(ex.map(judge, todo), 1):
        r = store["runs"][k]
        if v is None:
            v = r["fact_hit"]; r["judge_failed"] = True
        r["judge_hit"] = v; r["judge_score"] = sum(v) / len(v); r["judge_full"] = all(v)
        if n % 20 == 0:
            json.dump(store, open(path, "w"), indent=1, ensure_ascii=False); print(n, flush=True)
json.dump(store, open(path, "w"), indent=1, ensure_ascii=False)
print("judge failures:", sum(1 for r in store["runs"].values() if r.get("judge_failed")))
