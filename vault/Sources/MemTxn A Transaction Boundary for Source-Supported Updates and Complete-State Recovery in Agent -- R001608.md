---
type: research-source
item_id: 1608
title: "MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory"
source: "arxiv"
published: "2026-07-30T08:15:02Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.27834"
url: "https://arxiv.org/abs/2607.27834v1"
generated_by: codex-research-db
aliases:
  - "MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory"
topics:
  - "ai-agents"
---

# MemTxn: A Transaction Boundary for Source-Supported Updates and Complete-State Recovery in Agent Memory

[원문 열기](https://arxiv.org/abs/2607.27834v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XJZ3C4MI`)
- 발행일: 2026-07-30T08:15:02Z
- 저자: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Qianli Ma, Weijia Jia
- 식별자: `arxiv:2607.27834`

## 요약·초록

Persistent memory lets long-running large language model agents reuse information across sessions and tasks. Yet errors in writable memory can persist and corrupt future behavior. Existing systems improve storage and retrieval, but they do not provide a transaction boundary for reliable updates and recovery. We therefore propose MemTxn, a governance layer outside the answer model. MemTxn verifies whether an update is supported by its source. It also selects the visible version when facts conflict and restores the application-visible state after a fault. The system uses Ordered PatchTest to validate writes, a Temporal Resolver to select versions, and a durable snapshot journal to recover state. On an item-disjoint audit, MemTxn accepts all 60 supported originals and rejects all 179 hard negatives. Under persistent multi-key faults on LongMemEval-S and LoCoMo states, it restores the complete declared active map without knowing the actual physical write set. On MemoryAgentBench FactConsolidation, MemTxn achieves the highest average F1 across all twelve answer-model configurations. It outperforms Dense by 17.06--24.07 points in five representative settings.

## 내 메모


