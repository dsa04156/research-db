---
type: research-source
item_id: 2347
title: "When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory"
source: "arxiv"
published: "2026-08-26T09:04:21Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25553"
url: "https://arxiv.org/abs/2608.25553v1"
generated_by: codex-research-db
aliases:
  - "When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory"
topics:
  - "ai-agents"
---

# When Stale Constraints Go Unchecked: Budgeted Verification Failures in Inherited Agent Memory

[원문 열기](https://arxiv.org/abs/2608.25553v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-26T09:04:21Z
- 저자: Kazuki Nakayashiki
- 식별자: `arxiv:2608.25553`

## 요약·초록

An agent that inherits a consolidated memory may inherit a constraint that was true when written and has since been withdrawn by a newer authoritative record. Under a scarce verification budget, does the agent recover the withdrawal, and if not, is the error avoidable without spending more? We model supersession explicitly -- historical provenance is immutable; what changes is which record is current -- and assign by design the memory's form, the world's state (source current or superseded), and the verification policy at a fixed budget of two records: the agent's own allocation, or the same budget with one slot re-assigned to the critical provenance path or to a random record. With a constraint stated, agents inspected its provenance path in about one episode in five; when that constraint had been superseded, native allocation produced stale-consistent decisions in 77.3%, 74.7% and 74.7% of episodes across a primary run, a fresh-wording replication and a held-out domain. Re-assigning one slot to the critical path raised current-record-consistent decisions by +74.0, +72.7 and +61.3 points, positive in six of six models in each of those runs, and changed nothing when the record agreed with the memory. The held-out scenario was later found to contain a temporal inconsistency; a robustness replication with one sentence corrected, deposited externally before execution, gave +73.3 points and is reported alongside the original. The intervention uses knowledge of the critical path and is not a scheduler; it identifies that the share of stale-memory error attributable to verification allocation is close to its structural ceiling. Memory systems may need freshness or supersession signals separate from relevance.

## 내 메모
