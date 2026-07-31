---
type: research-source
item_id: 1038
title: "SEAGym: An Evaluation Environment for Self-Evolving LLM Agents"
source: "arxiv"
published: "2026-06-16T05:50:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.17546"
url: "https://arxiv.org/abs/2606.17546v1"
generated_by: codex-research-db
aliases:
  - "SEAGym: An Evaluation Environment for Self-Evolving LLM Agents"
topics:
  - "self-evolving-harness"
---

# SEAGym: An Evaluation Environment for Self-Evolving LLM Agents

[원문 열기](https://arxiv.org/abs/2606.17546v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`92DSNUU9`)
- 발행일: 2026-06-16T05:50:55Z
- 저자: Congjie Zheng, Chuanyi Xue, Bin Liang, Jun Yang, Changshui Zhang
- 식별자: `arxiv:2606.17546`

## 요약·초록

Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

## 내 메모


