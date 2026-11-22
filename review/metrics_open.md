```
variant            n  correct faithful  relev.  compl. ctx prec entity hit abst@unans  abst@ans calls   sec
v0_closed_book    41    84.6%      -    100.0%   91.5%      -          -         0.0%      2.7%   1.0   9.7
v5_graph          41    69.2%    95.1%   98.8%   52.4%    41.8%      76.8%     100.0%     51.4%   1.0   6.6
v2b_rerank8       41    65.4%    92.6%  100.0%   48.8%    42.4%      67.9%     100.0%     59.5%   1.0   7.5
v4_hybrid         41    65.4%    94.2%  100.0%   54.9%    47.0%      71.4%     100.0%     56.8%   1.0   8.7
v6_agentic        41    61.5%    95.7%  100.0%   56.1%    41.6%      71.4%     100.0%     64.9%   3.0  18.5
v2_rerank         41    53.8%    97.6%   98.8%   40.2%    61.0%      50.0%     100.0%     70.3%   1.0   5.8
v1_baseline       41    50.0%    95.0%   98.8%   37.8%    56.9%      51.8%     100.0%     62.2%   1.0   5.5
v3_hier_rerank    41    50.0%    95.6%   98.8%   36.6%    60.2%      50.0%     100.0%     73.0%   1.0   5.4

correctness vs oracle reference, by category
variant           Character      Class  Equipment    Monster      Spell
v0_closed_book        83.3%     100.0%     100.0%     100.0%      75.0%
v1_baseline           66.7%       0.0%       0.0%       0.0%      75.0%
v2_rerank             66.7%     100.0%       0.0%      50.0%      50.0%
v2b_rerank8           66.7%     100.0%      50.0%      50.0%      66.7%
v3_hier_rerank        50.0%     100.0%       0.0%      50.0%      50.0%
v4_hybrid             66.7%     100.0%       0.0%      50.0%      75.0%
v5_graph              66.7%     100.0%       0.0%     100.0%      66.7%
v6_agentic            66.7%      50.0%       0.0%      50.0%      75.0%
```
