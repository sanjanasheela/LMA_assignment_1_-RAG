```
Final-context retrieval metrics, 24 counterfactual questions (ranked list = chunks sent to the LLM; k beyond a variant's context size uses all of its chunks)

variant          chunks       mrr     hit@3  recall@3    prec@3    ndcg@3     hit@8  recall@8    prec@8    ndcg@8    full@8
v5_graph            8.0     0.931    100.0%     70.3%     73.6%     66.3%    100.0%     88.3%     47.4%     56.1%     70.8%
v4_hybrid           8.0     0.931    100.0%     64.9%     65.3%     62.0%    100.0%     80.5%     43.2%     52.0%     58.3%
v2b_rerank8         8.0     0.917     91.7%     61.3%     65.3%     61.8%     91.7%     75.8%     40.6%     50.8%     62.5%
v6_agentic         11.3     0.842     91.7%     41.5%     40.3%     40.7%    100.0%     85.0%     41.5%     45.4%     62.5%
v3_hier_rerank      3.0     0.917     91.7%     61.3%     65.3%     62.1%     91.7%     61.3%     65.3%     42.3%     25.0%
v2_rerank           3.0     0.917     91.7%     61.3%     65.3%     61.8%     91.7%     61.3%     65.3%     42.1%     25.0%
v1_baseline         3.0     0.750     83.3%     58.6%     58.3%     51.3%     83.3%     58.6%     58.3%     35.7%     25.0%

Candidate-pool metrics from traces (cross-encoder pool; MRR measured on the pool order before vs after re-ranking)

variant           pool pool recall MRR before MRR after nDCG@8 before nDCG@8 after
v2_rerank           10       74.5%      0.764     0.917         44.5%        50.1%
v2b_rerank8         10       74.5%      0.764     0.917         44.5%        50.1%
v3_hier_rerank      10       74.5%      0.777     0.917         45.0%        50.7%
v4_hybrid           30       86.6%      0.859     0.931         51.2%        52.4%
v5_graph            20       94.3%      0.859     0.931         51.2%        55.8%
v6_agentic          20       57.7%      0.695     0.826         29.2%        33.5%
```
