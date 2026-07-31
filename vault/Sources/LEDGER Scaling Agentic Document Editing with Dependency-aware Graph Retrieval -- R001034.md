---
type: research-source
item_id: 1034
title: "LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval"
source: "arxiv"
published: "2026-06-19T17:35:05Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.28379"
url: "https://arxiv.org/abs/2606.28379v1"
generated_by: codex-research-db
aliases:
  - "LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval"
topics:
  - "self-evolving-harness"
---

# LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval

[원문 열기](https://arxiv.org/abs/2606.28379v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`F7J8HA9H`)
- 발행일: 2026-06-19T17:35:05Z
- 저자: Mike Hang Wang, Utkarsh Garg, Reza Davari, Huitian Jiao, Hao Cheng, Baolin Peng, Tao Ge, Si-Qing Chen
- 식별자: `arxiv:2606.28379`

## 요약·초록

We introduce LEDGER to tackle the novel context engineering challenge of agentic document editing, where localized edits to long, structured documents must be applied efficiently without breaking cross-references or semantic consistency. LEDGER constructs a lightweight dependency graph that explicitly models document structure, including hierarchical organization, explicit references, implicit dependencies, and semantic relationships. For each edit, graph-guided retrieval selects only the necessary context, avoiding full-document processing while preserving consistency. We evaluate LEDGER on a curated benchmark of 1.9k test cases with various document types and lengths, spanning six state-of-the-art models: LEDGER improves consistency from 56% to 76% across all six models and test scenarios while reducing token usage. Notably, LEDGER with low reasoning effort matches baseline performance at high reasoning effort using fewer tokens, showing that explicit dependency representations can partially substitute for expensive internal reasoning in agentic document editing.

## 내 메모


