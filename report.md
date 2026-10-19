# RAG assignment: baseline retrieval vs. cross-encoder re-ranking

NAME :sanjana sheela 
ROLLNo: 2023102027
Git link: [https://github.com/sanjanasheela/LMA_assignment_1_-RAG](https://github.com/sanjanasheela/LMA_assignment_1_-RAG)

## Setup

| Item | Choice |
|---|---|
| Document | D&D 5e SRD spell chapter (`data/spells.md`) |
| Chunking | RecursiveCharacterTextSplitter, 500 characters, 50 overlap, 873 chunks |
| Bi-encoder | `sentence-transformers/all-MiniLM-L6-v2`, normalised embeddings |
| Vector store | ChromaDB, cosine distance |
| Cross-encoder | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| LLM | Gemini Flash through the API |
| Prompt | Answer using the provided context |
| Hardware | NVIDIA GeForce RTX 2050 (CUDA) |
| Questions | 19 spell questions in `questions.json`, each with a short gold answer |

| Pipeline | Steps |
|---|---|
| 1 (baseline) | Embed the query, take the top 10 chunks by cosine similarity, give the top 3 to the LLM (Answer 1). |
| 2 (re-ranking) | Take the same top 10, score all 10 (query, chunk) pairs with the cross-encoder, re-sort, give the new top 3 to the LLM (Answer 2). |

The top 10 is retrieved once per question and shared, so the two pipelines differ only in how they pick the final 3 chunks.

The gold answers are short strings with no gold passages, so I used two rough checks. A chunk counts as relevant if it contains the gold answer text, and an answer counts as correct if it contains the gold answer or at least 75% of its content words. Both can be wrong in either direction, so the numbers below are indicative.

## 1. Architecture comparison

| | Bi-encoder | Cross-encoder |
|---|---|---|
| Input | Query and chunk are encoded separately | Query and chunk are encoded together as one sequence |
| Interaction | None until the final cosine similarity between two fixed vectors | Self-attention runs across the tokens of both texts |
| Precomputation | Chunk vectors are computed once and stored | Nothing can be stored, since the score depends on the query |
| Cost per query | One query encoding plus a nearest-neighbour search | One forward pass per (query, chunk) pair |
| Weakness | A whole chunk is squeezed into one vector, so details like a specific number, a negation or an exception can get lost | Too slow to run over a large collection |

## 2. Failure mode analysis and rank shifts

### Overall results (27 questions)

| Metric | Pipeline 1 | Pipeline 2 |
|---|---|---|
| LLM answer correct (hand-corrected) | 16 / 27 (59.3%) | 21 / 27 (77.8%) |
| Relevant chunk in the top 3 (keyword check) | 55.6% | 74.1% |
| MRR@10 (keyword check) | 0.732 | 0.934 |
| Chunks promoted into the top 3 | n/a | 5 |
| Chunks pushed out of the top 3 | n/a | 0 |

A relevant chunk was in the top 10 for 77.8% of questions, which is the most any re-ranker could reach from these candidates.


### Failure modes, one example each

| Failure mode | Query | Baseline rank | Re-ranked rank | Answer 1 | Answer 2 |
|---|---|---|---|---|---|
| Keyword trap / distractor | How much Fire damage does the Fire Bolt cantrip deal on a hit? (Q18, run A) | 10 | 1 | Said the damage was not mentioned | 1d10 Fire damage |
| Exception / corner case | How much longer does the Ritual version of a spell take to cast? (Q5, run A) | 5 | 1 | "Minutes or even hours" | 10 minutes longer |
| Negation / constraint | When does an object hit by Fire Bolt not start burning? (Q28, run B) | 6 | 1 | "The context does not contain the answer." | It doesn't start burning if it is being worn or carried |
| Buried chunk | What is the range of the Fireball spell? (Q14, run A) | 9 | 1 | Said the range was not mentioned | 150 feet |

What happened in each case:

| Failure mode | What went wrong in the baseline | What re-ranking did |
|---|---|---|
| Keyword trap | The top-ranked chunk was the tail of another fire spell ("Flammable objects in the area that aren't being worn or carried start burning"), which shares the words "Fire" and "damage" with the query. The chunk with Fire Bolt's damage sat at rank 10, so the baseline context never held it. | The cross-encoder moved the Fire Bolt chunk to rank 1. |
| Exception | The top-ranked chunk was the general "Longer Casting Times" text, which only says rituals take "minutes or even hours". The chunk with the 10-minute rule sat at rank 5. | The Ritual rule moved to rank 1 and Answer 2 stated it. |
| Negation | The question turns on the constraint "isn't being worn or carried". The top 3 held other spells with that same phrase (Fireball's tail, Burning Hands-style text), but not Fire Bolt's own chunk, which was at rank 6. With no Fire Bolt text, the model correctly said the context lacked the answer. | Fire Bolt's chunk moved to rank 1, and Answer 2 gave the exact condition. |
| Buried chunk | A chunk about a different fire spell outranked the Fireball block, which sat at rank 9. | The Fireball block moved to rank 1 and Answer 2 gave 150 feet. |

The negation example is the clearest case of the bi-encoder missing a constraint. The wording of the query is close to many fire-spell chunks, and only the cross-encoder picked the chunk about the right spell. The notebook's keyword check scored this question as rank 1 to rank 1, because other spells' chunks contain the same phrase. I took the Fire Bolt chunk's rank from the saved top 10 instead.

### All rank shifts

| Question | Baseline rank | Re-ranked rank | Answer 1 | Answer 2 |
|---|---|---|---|---|
| Which school of magic prevents or reverses harmful effects? (Q2, run A) | 5 | 1 | Incorrect | Correct |
| How much longer does the Ritual version take? (Q5, run A) | 5 | 1 | Incorrect | Correct |
| What is the range of the Fireball spell? (Q14, run A) | 9 | 1 | Incorrect | Correct |
| How much Fire damage does Fire Bolt deal? (Q18, run A) | 10 | 1 | Incorrect | Correct |
| When does an object hit by Fire Bolt not start burning? (Q28, run B) | 6 | 1 | Incorrect | Correct |

### Answer 1 vs. Answer 2

In all five promoted cases the baseline did not make anything up. Its top 3 lacked the deciding chunk, and the model said the context did not contain the answer. That is a missing clause, not a hallucination. Once the chunk reached the top 3, the same model with the same prompt answered correctly.

### Limitations

| Limitation | Detail |
|---|---|
| Keyword check | It is a rough proxy. It marked Q24 (Mirror Image) as correct for Pipeline 2 although that answer said the context lacked the answer, and I counted it incorrect. For Q28 it missed the real promotion because other spells share the phrase. |
| Outside knowledge | The strict prompt did not stop gemini completely. In one answer (Q20) it added a note from general D&D knowledge, outside the context. |
| Sample | 27 spell questions, so a difference of one or two questions means little. |

## 3. Latency profiling

Measured over 27 queries on a CUDA GPU, in milliseconds.

| Stage | Mean | Median | Max |
|---|---|---|---|
| Pipeline 1 retrieval (embed query + top-10 search) | 17.2 | 10.2 | 125.8 |
| Cross-encoder re-ranking of 10 chunks | 22.9 | 23.9 | 28.6 |
| Pipeline 2 retrieval total | 40.1 | 34.0 | 150.2 |
| LLM call, Pipeline 1 | 4524.3 | 3804.4 | 9743.4 |
| LLM call, Pipeline 2 | 4386.3 | 3346.4 | 13033.9 |
| End to end, Pipeline 1 | 4541.4 | 3818.0 | 9869.2 |
| End to end, Pipeline 2 | 4426.4 | 3496.6 | 13066.7 |

Re-ranking adds about 23 ms on average. At the median that takes retrieval from 10 ms to 34 ms, so retrieval is roughly three times slower. The LLM call takes seconds, so the extra 23 ms is small in the full pipeline.

 Pipeline 2's end-to-end mean is lower than Pipeline 1's, but re-ranking did not cause that. Both pipelines call the same LLM, and response time varies from call to call. Only the retrieval rows show what re-ranking costs. The 125.8 ms maximum on the first row is probably GPU warm-up on the first query.

## 4. Scaling question

| Collection size | Cross-encoder pairs per query | Estimated time per query |
|---|---|---|
| Top 10 only (what I did) | 10 | about 23 ms (measured) |
| This corpus (873 chunks) | 873 | about 2 s (estimate) |
| 1 million chunks | 1,000,000 | about 2,000 s (estimate) |

The estimates assume roughly 2 ms per pair, taken from the 23 ms for 10 pairs. I did not run the cross-encoder over the whole collection.

A cross-encoder cannot precompute anything, because its score depends on the query and the chunk together. Each pair needs its own forward pass, so the cost grows linearly with the collection size. A bi-encoder embeds each chunk once, ahead of time. At query time it embeds only the query and runs a nearest-neighbour search, which stays fast for millions of chunks.

So the two stages split the work. The bi-encoder cuts the collection to a small candidate set, and the cross-encoder re-ranks only that set. The cost is that the first stage caps the result. If the right chunk is not in the top 10, re-ranking cannot recover it.

## Conclusion

On the 27 questions, re-ranking raised correct answers from 16 to 21 and MRR@10 from 0.732 to 0.934. It added about 23 ms to retrieval and never pushed a relevant chunk out of the top 3. All five gains came from promoting the deciding chunk from rank 5, 5, 6, 9 or 10 into the top 3, including one negation case (Fire Bolt and the "not worn or carried" condition).
