```
Final-context retrieval metrics, 24 counterfactual questions (ranked list = chunks sent to the LLM; k beyond a variant's context size uses all of its chunks)

variant          chunks       mrr     hit@3  recall@3    prec@3    ndcg@3     hit@8  recall@8    prec@8    ndcg@8    full@8
v5_graph            8.0     0.951    100.0%     70.7%     69.4%     65.8%    100.0%     87.3%     41.1%     53.9%     70.8%
v4_hybrid           8.0     0.881     91.7%     63.6%     65.3%     59.3%     95.8%     77.5%     43.8%     51.5%     58.3%
v2b_rerank8         8.0     0.910     95.8%     60.8%     65.3%     60.7%     95.8%     75.3%     41.1%     50.5%     62.5%
v6_agentic         11.5     0.776     79.2%     38.2%     36.1%     36.5%    100.0%     82.3%     41.1%     42.6%     62.5%
v3_hier_rerank      3.0     0.931     95.8%     60.8%     65.3%     61.7%     95.8%     60.8%     65.3%     42.1%     25.0%
v2_rerank           3.0     0.910     95.8%     60.8%     65.3%     60.7%     95.8%     60.8%     65.3%     41.6%     25.0%
v1_baseline         3.0     0.764     87.5%     59.9%     59.7%     52.3%     87.5%     59.9%     59.7%     36.2%     25.0%

Candidate-pool metrics from traces (cross-encoder pool; MRR measured on the pool order before vs after re-ranking)

variant           pool pool recall MRR before MRR after nDCG@8 before nDCG@8 after
```
