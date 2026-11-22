```
variant            n  correct faithful  relev.  compl. ctx prec entity hit abst@unans  abst@ans calls   sec
v2b_rerank8       41    61.5%    81.0%   95.1%   50.0%    42.7%      67.9%     100.0%     35.1%   1.0  29.8
v5_graph          41    61.5%    81.6%   95.1%   50.0%    44.8%      76.8%      50.0%     40.5%   1.0  30.1
v4_hybrid         41    53.8%    85.9%   96.3%   45.1%    45.4%      71.4%     100.0%     43.2%   1.0  39.9
v6_agentic        41    53.8%    84.3%   96.3%   40.2%    47.5%      57.1%     100.0%     48.6%   3.0  53.1
v1_baseline       41    50.0%    80.0%   92.7%   39.0%    59.3%      51.8%     100.0%     48.6%   1.0  13.9
v2_rerank         41    50.0%    83.1%   93.9%   35.4%    63.4%      50.0%     100.0%     45.9%   1.0  15.2
v3_hier_rerank    41    42.3%    86.9%   90.2%   41.5%    60.2%      50.0%     100.0%     43.2%   1.0  15.7
v0_closed_book    41    15.4%      -    100.0%   76.8%      -          -         0.0%      0.0%   1.0  48.5

correctness vs oracle reference, by category
variant           Character      Class  Equipment    Monster      Spell
v0_closed_book        16.7%      50.0%       0.0%       0.0%      16.7%
v1_baseline           50.0%       0.0%       0.0%       0.0%      83.3%
v2_rerank             66.7%      50.0%       0.0%      50.0%      50.0%
v2b_rerank8           33.3%      50.0%     100.0%      50.0%      75.0%
v3_hier_rerank        50.0%      50.0%       0.0%      50.0%      41.7%
v4_hybrid             50.0%     100.0%       0.0%      50.0%      58.3%
v5_graph              50.0%      50.0%       0.0%     100.0%      66.7%
v6_agentic            50.0%      50.0%       0.0%      50.0%      66.7%
```
