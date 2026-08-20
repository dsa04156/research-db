---
type: research-source
item_id: 2084
title: "AgentRewind: Recoverable Execution for Long-Horizon LLM Agents"
source: "arxiv"
published: "2026-08-14T15:20:35Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.14380"
url: "https://arxiv.org/abs/2608.14380v1"
generated_by: codex-research-db
aliases:
  - "AgentRewind: Recoverable Execution for Long-Horizon LLM Agents"
topics:
  - "self-evolving-harness"
---

# AgentRewind: Recoverable Execution for Long-Horizon LLM Agents

[원문 열기](https://arxiv.org/abs/2608.14380v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`THKSEBM5`)
- 발행일: 2026-08-14T15:20:35Z
- 저자: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
- 식별자: `arxiv:2608.14380`

## 요약·초록

Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, a runtime recovery framework that records aligned checkpoints of the agent context and controlled environment, allowing agents to return to an earlier state and resume execution with information from previous attempts. We also construct MettleBench, a benchmark for evaluating task completion and partial progress on long-horizon engineering assignments containing a series of related requirements. Experiments across tasks, multiple models, execution strategies, and agent harnesses show that AgentRewind improves task success rate and average checklist progress over the compared baselines.

## 내 메모


