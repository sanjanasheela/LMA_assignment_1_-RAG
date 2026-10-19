# RAG assignment: baseline retrieval vs. cross-encoder re-ranking

## Setup

| Item | Choice |
|---|---|
| Document | D&D 5e SRD spell chapter (`data/spells.md`) |
| Chunking | RecursiveCharacterTextSplitter, 500 characters, 50 overlap, 873 chunks |
| Bi-encoder | `sentence-transformers/all-MiniLM-L6-v2`, normalised embeddings |
| Vector store | ChromaDB, cosine distance |
| Cross-encoder | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| LLM | Gemini, temperature 0, one shared prompt for both pipelines |
| Hardware | NVIDIA GeForce RTX 2050 (CUDA) |
| Questions | 20 spell questions in `questions.json`, each with a short gold answer. 19 were evaluated in the final run. |

| Pipeline | Steps |
|---|---|
| 1 (baseline) | Embed the query, take the top 10 chunks by cosine similarity, give the top 3 to the LLM (Answer 1). |
| 2 (re-ranking) | Take the same top 10, score all 10 (query, chunk) pairs with the cross-encoder, re-sort, give the new top 3 to the LLM (Answer 2). |

The top 10 is retrieved once per question and shared, so the two pipelines differ only in how they pick the final 3 chunks.

The gold answers are short strings with no gold passages, so I used two rough checks. A chunk counts as relevant if it contains the gold answer text. An answer counts as correct if it contains the gold answer or at least 75% of its content words. Both can be wrong in either direction, so the numbers below are indicative.

## 1. Architecture comparison

| | Bi-encoder | Cross-encoder |
|---|---|---|
| Input | Query and chunk are encoded separately | Query and chunk are encoded together as one sequence |
| Interaction | None until the final cosine similarity between two fixed vectors | Self-attention runs across the tokens of both texts |
| Precomputation | Chunk vectors are computed once and stored | Nothing can be stored, since the score depends on the query |
| Cost per query | One query encoding plus a nearest-neighbour search | One forward pass per (query, chunk) pair |
| Weakness | A whole chunk is squeezed into one vector, so details like a specific number, a negation or an exception can get lost | Too slow to run over a large collection |

## 2. Failure mode analysis and rank shifts

### Overall results (19 questions)

| Metric | Pipeline 1 | Pipeline 2 |
|---|---|---|
| LLM answer correct | 12 / 19 (63.2%) | 16 / 19 (84.2%) |
| Relevant chunk in the top 3 | 57.9% | 78.9% |
| MRR@10 | 0.733 | 0.944 |
| Chunks promoted into the top 3 | n/a | 4 |
| Chunks pushed out of the top 3 | n/a | 0 |

A relevant chunk was in the top 10 for 84.2% of questions, which is the most any re-ranker could reach from these candidates.

### Failure modes, one example each

| Failure mode | Query | Baseline rank | Re-ranked rank | Answer 1 | Answer 2 |
|---|---|---|---|---|---|
| Keyword trap / distractor | How much Fire damage does the Fire Bolt cantrip deal on a hit? (Q18) | 10 | 1 | Said the damage was not mentioned | 1d10 Fire damage |
| Exception / corner case | How much longer does the Ritual version of a spell take to cast? (Q5) | 5 | 1 | "Minutes or even hours" | 10 minutes longer |
| Negation / constraint | What is the base AC of a creature under the Mage Armor spell? (Q17) | not a failure | 1 | Correct | Correct |
| Buried chunk | What is the range of the Fireball spell? (Q14) | 9 | 1 | Said the range was not mentioned | 150 feet |

What happened in each case:

| Failure mode | What went wrong in the baseline | What re-ranking did |
|---|---|---|
| Keyword trap | Many spells share words like "damage" and "Fire", and the notebook analysis suggests these crowded the Fire Bolt chunk down to rank 10. The baseline context never held the answer. | The cross-encoder read the query and chunk together and moved the Fire Bolt chunk to rank 1. |
| Exception | The top ranks held general text about long casting times. The specific 10-minute Ritual rule sat at rank 5, so Answer 1 could only say "minutes or even hours". | The Ritual rule moved to rank 1 and Answer 2 stated it. |
| Negation | Mage Armor only works on a creature "who isn't wearing armor", which is a constraint a bi-encoder could blur. In this run the baseline still answered correctly, so the data shows no failure here. | Nothing to fix. The chunk was at rank 1 after re-ranking. |
| Buried chunk | Other fire-related chunks outranked the Fireball block, which sat at rank 9. Answer 1 said the range was missing. | The Fireball block moved to rank 1 and Answer 2 gave 150 feet. |

The negation row is the weak point of the analysis. I wrote no query that tests negation, and the Mage Armor result does not show a negation failure. I list it only because the assignment asks for the category. Showing the failure would need new queries such as "not allowed" or "prohibited" cases.

The explanations for why the baseline ranked these chunks badly (distractor wording, general casting-time text) come from the notebook's analysis. I could not check them against the saved results because the per-question output was overwritten. The ranks and the correct/incorrect results are from the notebook tables.

### All rank shifts

| Question | Baseline rank | Re-ranked rank | Answer 1 | Answer 2 |
|---|---|---|---|---|
| Which school of magic prevents or reverses harmful effects? (Q2) | 5 | 1 | Incorrect | Correct |
| How much longer does the Ritual version take? (Q5) | 5 | 1 | Incorrect | Correct |
| What is the range of the Fireball spell? (Q14) | 9 | 1 | Incorrect | Correct |
| How much Fire damage does Fire Bolt deal? (Q18) | 10 | 1 | Incorrect | Correct |

### Answer 1 vs. Answer 2

In all four promoted cases the baseline did not make anything up. Its top 3 lacked the deciding chunk, and the model said the context did not contain the answer. That is a missing clause, not a hallucination. Once the chunk reached the top 3, the same model with the same prompt answered correctly.

### Where re-ranking did not help

| Question | Answer 1 | Answer 2 |
|---|---|---|
| Magic Missile damage per dart | Incorrect | Incorrect |
| Misty Step teleport distance | Incorrect | Incorrect |
| Healing Word casting time | Incorrect | Incorrect |

A relevant chunk was in the top 10 for 16 of 19 questions, so at most three questions had none. Re-ranking only reorders the 10 candidates and cannot bring back a chunk the bi-encoder missed. Chunking probably plays a part: a spell can be split over several 500-character pieces, and the piece holding the damage or the casting time may not rank well. The 75% word-overlap check may also have marked some correct but differently worded answers as wrong. I did not check which of these applies to each question.

### Limitations

| Limitation | Detail |
|---|---|
| Negation | No query was designed for it, so there is no measured example. |
| Failure-query section | The hand-written failure queries in the notebook were never run. The analysis above comes from the main question set. |
| Correctness check | It is a keyword proxy. |
| Sample | 19 spell questions, so a difference of one or two questions means little. |
| Missing question | The twentieth question (Cure Wounds) is not in the final results. |
| Scope | Only `spells.md` is indexed, not the whole SRD. |

## 3. Latency profiling

Measured over 19 queries on a CUDA GPU, in milliseconds.

| Stage | Mean | Median | Max |
|---|---|---|---|
| Pipeline 1 retrieval (embed query + top-10 search) | 18.5 | 10.2 | 125.8 |
| Cross-encoder re-ranking of 10 chunks | 22.4 | 23.4 | 28.6 |
| Pipeline 2 retrieval total | 40.9 | 33.5 | 150.2 |
| LLM call, Pipeline 1 | 3920.4 | 3444.3 | 9743.4 |
| LLM call, Pipeline 2 | 3489.2 | 2914.8 | 13033.9 |
| End to end, Pipeline 1 | 3938.9 | 3462.4 | 9869.2 |
| End to end, Pipeline 2 | 3530.1 | 2947.0 | 13066.7 |

Re-ranking adds about 22 ms on average. At the median that takes retrieval from 10 ms to 34 ms, so retrieval is roughly three times slower. The LLM call takes seconds, so the extra 22 ms is small in the full pipeline.

Pipeline 2's end-to-end mean is lower than Pipeline 1's, but re-ranking did not cause that. Both pipelines call the same API, and response time varies from call to call. Only the retrieval rows show what re-ranking costs. The 125.8 ms maximum on the first row is probably GPU warm-up on the first query.

## 4. Scaling question

| Collection size | Cross-encoder pairs per query | Estimated time per query |
|---|---|---|
| Top 10 only (what I did) | 10 | about 22 ms (measured) |
| This corpus (873 chunks) | 873 | about 2 s (estimate) |
| 1 million chunks | 1,000,000 | about 2,000 s (estimate) |

The estimates assume roughly 2 ms per pair, taken from the 22 ms for 10 pairs. I did not run the cross-encoder over the whole collection.

A cross-encoder cannot precompute anything, because its score depends on the query and the chunk together. Each pair needs its own forward pass, so the cost grows linearly with the collection size. A bi-encoder embeds each chunk once, ahead of time. At query time it embeds only the query and runs a nearest-neighbour search, which stays fast for millions of chunks.

So the two stages split the work. The bi-encoder cuts the collection to a small candidate set, and the cross-encoder re-ranks only that set. The cost is that the first stage caps the result. If the right chunk is not in the top 10, re-ranking cannot recover it, which is what happened for the three questions both pipelines got wrong.

## Conclusion

On this question set, re-ranking raised correct answers from 12 to 16 of 19 and MRR@10 from 0.733 to 0.944. It added about 22 ms to retrieval and never pushed a relevant chunk out of the top 3. All four gains came from promoting a chunk from rank 5, 5, 9 or 10 into the top 3. It could not help when the bi-encoder had not retrieved the answer chunk at all.
