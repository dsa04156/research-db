---
type: research-source
item_id: 2571
title: "Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory"
source: "arxiv"
published: "2026-09-03T03:56:15Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03340"
url: "https://arxiv.org/abs/2609.03340v1"
generated_by: codex-research-db
aliases:
  - "Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory"
topics:
  - "ai-agents"
---

# Fresh Memory, Stale Plans: Dependency-Scoped Validation for Distributed LLM-Agent Memory

[원문 열기](https://arxiv.org/abs/2609.03340v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T03:56:15Z
- 저자: Evan Chen, Shiqiang Wang, Christopher G. Brinton
- 식별자: `arxiv:2609.03340`

## 요약·초록

Distributed LLM-agent teams can read the latest shared facts and still act on an obsolete plan. A planner may derive an action from requirement $r_3$, another agent may commit $r_4$, and an executor may receive $r_4$ without replacing the plan derived from $r_3$. We call this \emph{stale-plan execution}: state freshness does not establish that the plan authorizing an action remains valid. We introduce PlanFence, a dependency-scoped action-validation protocol. Plans cite the exact public records they used, and an executor validates only the records that can affect the pending external action, replanning once or blocking when validation is incomplete. In 30 controlled live workflows with a post-plan revision, a freshness-only executor acts on the obsolete plan in every task, whereas PlanFence completes all tasks without an invalid action. Controlled replay reveals two conditional boundaries: proactive synchronization yields lower coordination stall at low churn, while PlanFence avoids repeated update-path coordination as churn grows and avoids validating unrelated state as the shared keyspace grows. These are controlled safety and systems-cost results, not general task-accuracy gains.

## 내 메모


