---
type: research-source
item_id: 1084
title: "MemTX: Transactional Belief Commit for Stateful Agent Memory"
source: "arxiv"
published: "2026-07-27T01:57:39Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.23929"
url: "https://arxiv.org/abs/2607.23929v2"
generated_by: codex-research-db
aliases:
  - "MemTX: Transactional Belief Commit for Stateful Agent Memory"
topics:
  - "ai-agents"
---

# MemTX: Transactional Belief Commit for Stateful Agent Memory

[원문 열기](https://arxiv.org/abs/2607.23929v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UF97ZS8Z`)
- 발행일: 2026-07-27T01:57:39Z
- 저자: Xiaoyang Li, Yiqi Wang, Haohui Lu, Zhi Chen, Mo Li, Pingan Song, Mingkai Zheng, Taotao Cai
- 식별자: `arxiv:2607.23929`

## 요약·초록

LLM agents increasingly coordinate through persistent shared memory: one agent's write becomes another agent's premise, and eventually a tool call with real side effects. Current agent memory systems treat every accepted write as immediately actionable truth, so a polluted tool result, a stale update, or a teammate's half-finished note can silently drive an irreversible action. We argue that a memory write is not a belief commit. We present MemTX, a transactional belief-commit protocol. Each record carries evidence, permissions, provenance, and validity. Writes are staged inside snapshot-isolated transactions and admitted by a validate-and-commit pipeline, irreversible tool calls are gated on in-flight belief state, and retracting a belief triggers typed cascading repair of its derived records and tool side effects. Two invariants, action-safety gating and cascade-repair completeness, are machine-checked by property-based testing and bounded exhaustive enumeration of 5.5 million protocol states, with zero violations. Across five backbones from three model families, MemTX leads all eight baselines with paired-McNemar significance on four backbones and statistically ties the best baseline on the fifth and strongest, while remaining the only method with zero downstream harm on every backbone. Backbone capability does not substitute for commit discipline.

## 내 메모


