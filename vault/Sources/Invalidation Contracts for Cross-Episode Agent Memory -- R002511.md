---
type: research-source
item_id: 2511
title: "Invalidation Contracts for Cross-Episode Agent Memory"
source: "arxiv"
published: "2026-08-31T18:45:07Z"
first_seen: "2026-09-02"
review_status: "pending"
canonical_key: "arxiv:2609.00243"
url: "https://arxiv.org/abs/2609.00243v1"
generated_by: codex-research-db
aliases:
  - "Invalidation Contracts for Cross-Episode Agent Memory"
topics:
  - "ai-agents"
---

# Invalidation Contracts for Cross-Episode Agent Memory

[원문 열기](https://arxiv.org/abs/2609.00243v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-02|2026-09-02]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MVDDE22J`)
- 발행일: 2026-08-31T18:45:07Z
- 저자: Michael Wu, Arquimedes Canedo
- 식별자: `arxiv:2609.00243`

## 요약·초록

LLM agents that cache recovery suggestions from API errors can skip re-derivation in later episodes, spending fewer tokens and fewer model calls on constraints they have already learned. Server-side data drift turns those cached fixes into silent failures, and the usual remedy, re-deriving on every episode, gives the savings back. We introduce invalidation contracts, a protocol layer that attaches version stamps and cacheability hints to every recovery suggestion so the client can evict stale entries without trial and error, and keep the rest. The contract decomposes realized savings into two independent factors: validity, the fraction of cached suggestions that remain correct after a drift event, and compliance, the fraction the planner applies on the first attempt. Validity depends only on the protocol and is vendor-independent. Compliance depends on the planner model: identical wire bytes yield 100% first-try compliance on Claude Haiku 4.5 and 11% or below on Claude Sonnet 5, which exhibits input-schema conservatism, refusing fixes that add fields the original request did not contain. We evaluate across seven models, three serving paths, two domains, and approximately 9,400 episodes. Row-level invalidation raises compliance by 0 to 66.7 percentage points across the seven models, 55.6 to 66.7 on three, and recovers 29-33% of baseline token cost on four of seven models, while table-level invalidation destroys co-located entries and drops post-drift first-try rates to 0% on five of seven. Eviction precision is 1.00 at row granularity on every model under the row-level oracle of Section 4.1. The contract adds 15% to response payload. Version-stamp validity is deterministic by construction and produced identical results across every model and serving path, with zero contract failures in the entire evaluation.

## 내 메모


