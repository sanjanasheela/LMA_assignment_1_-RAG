"""Ranks the RAG variants from results_v2.json."""
import json, sys
from collections import defaultdict
import numpy as np

path = sys.argv[1] if len(sys.argv) > 1 else "results_v2.json"
runs = json.load(open(path))["runs"]
by_v = defaultdict(list)
for k, r in runs.items():
    if not r["answer"].startswith("ERROR"):
        by_v[k.split("|")[0]].append(r)


KEY = "judge_hit" if len(sys.argv) < 3 or sys.argv[2] != "strict" else "fact_hit"
SC = "judge_score" if KEY == "judge_hit" else "score"
FU = "judge_full" if KEY == "judge_hit" else "full"


def facts_acc(rs, changed):
    h = [x for r in rs for x, c in zip(r[KEY], r["fact_changed"]) if c == changed]
    return (sum(h) / len(h)) if h else float("nan"), len(h)


rows = []
for v, rs in by_v.items():
    ctx = [x for r in rs for x in r["ctx_hit"] if x is not None]
    rows.append({
        "variant": v, "n": len(rs),
        "fact_acc": np.mean([r[SC] for r in rs]),
        "full": np.mean([r[FU] for r in rs]),
        "chg_acc": facts_acc(rs, True)[0], "unchg_acc": facts_acc(rs, False)[0],
        "ctx_recall": (sum(ctx) / len(ctx)) if ctx else float("nan"),
        "ctx_chars": np.mean([r["ctx_chars"] for r in rs]),
        "calls": np.mean([r["llm_calls"] for r in rs]), "secs": np.mean([r["total_s"] for r in rs]),
    })
rows.sort(key=lambda r: -r["fact_acc"])
print("metric:", KEY)
print(f"{'rank':4s} {'variant':16s} {'n':>3s} {'fact acc':>8s} {'full ans':>8s} {'changed':>8s} {'unchngd':>8s} {'ctx rec':>8s} {'ctx chr':>7s} {'calls':>5s} {'sec/q':>6s}")
for i, r in enumerate(rows, 1):
    print(f"{i:<4d} {r['variant']:16s} {r['n']:3d} {r['fact_acc']:8.1%} {r['full']:8.1%} {r['chg_acc']:8.1%} {r['unchg_acc']:8.1%} "
          f"{r['ctx_recall']:8.1%} {r['ctx_chars']:7.0f} {r['calls']:5.1f} {r['secs']:6.1f}")

print("\nfact accuracy by question type")
types = sorted({r["type"] for rs in by_v.values() for r in rs})
print(f"{'variant':16s} " + " ".join(f"{t:>11s}" for t in types))
for row in rows:
    v = row["variant"]
    cells = []
    for t in types:
        s = [r[SC] for r in by_v[v] if r["type"] == t]
        cells.append(f"{np.mean(s):11.1%}" if s else f"{'-':>11s}")
    print(f"{v:16s} " + " ".join(cells))
