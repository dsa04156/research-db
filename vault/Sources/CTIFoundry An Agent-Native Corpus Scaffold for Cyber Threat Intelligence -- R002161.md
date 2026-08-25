---
type: research-source
item_id: 2161
title: "CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence"
source: "arxiv"
published: "2026-08-19T07:00:29Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.18613"
url: "https://arxiv.org/abs/2608.18613v1"
generated_by: codex-research-db
aliases:
  - "CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence"
topics:
  - "self-evolving-harness"
---

# CTIFoundry: An Agent-Native Corpus Scaffold for Cyber Threat Intelligence

[원문 열기](https://arxiv.org/abs/2608.18613v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZJ8IN8GH`)
- 발행일: 2026-08-19T07:00:29Z
- 저자: Yutong Cheng, Changze Li, Qian Cui, Wei Ding, Lingzhi Wang, Yan Chen, Peng Gao
- 식별자: `arxiv:2608.18613`

## 요약·초록

Cyber threat intelligence (CTI) is increasingly consumed not by human analysts but by LLM agents that compose multi-step investigations at query time. The harness side of this shift has matured rapidly (planning loops, tool protocols, context management), but the corpus side has not: threat reports and vulnerability databases are still packaged for retrieval-augmented generation, as opaque chunks behind an embedding index. We argue that this substrate, not model capability, is the bottleneck on agentic CTI investigation, and present CTIFoundry, an agent-native corpus scaffold. At build time, CTIFoundry materializes the latent structure of a CTI corpus: a deterministic ontology graph over four authoritative knowledge bases (CVE, CWE, CAPEC, ATT&CK) whose official cross-references become typed, traversable edges; a span-grounded report layer whose canonical, alias-resolved cross-vendor entities index provenance-carrying chunks; and hybrid dense+lexical retrieval surfaces. At query time this structure is exposed through seven typed tools and three procedural skills mounted on a stock open-source agent harness. On the public CTIConnect benchmark, swapping only the action surface lifts the identically-harnessed agent by +0.19 to +0.28 overall F1 across a four-model, two-provider panel: a small model on CTIFoundry surpasses a flagship on the flat substrate, and the gain is not bought with search effort, since on both Claude models the scaffolded agent is more accurate at roughly half the tool calls. An ablation attributes it: typed structure carries the larger share, procedural skills convert structure into discipline, and the two compose super-additively, because skills bind only to structure that exists.

## 내 메모


