---
type: research-source
item_id: 10
title: "WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing"
source: "arxiv"
published: "2026-07-28T14:19:59Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25765"
url: "https://arxiv.org/abs/2607.25765v1"
generated_by: codex-research-db
aliases:
  - "WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing"
topics:
  - "self-evolving-harness"
---

# WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing

[원문 열기](https://arxiv.org/abs/2607.25765v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`AJBDEHV9`)
- 발행일: 2026-07-28T14:19:59Z
- 저자: Hao Liang, Meiyi Qiang, Sizhe Qiu, Linzhuang Sun, Wentao Zhang
- 식별자: `arxiv:2607.25765`

## 요약·초록

Enterprise agents often need to integrate heterogeneous knowledge sources: documents for narrative facts, tables for computation, and dependency graphs for file relationships. Existing benchmarks typically evaluate retrieval or tool use without distinguishing whether an agent first selects the appropriate knowledge sources. We introduce WorkSurface-Bench, a benchmark for evaluating this capability as surface routing. It contains 1,151 atomic tasks derived from persona-scoped Workspace-Bench-Lite workspaces, spanning document, table, graph, and cross-surface questions. Its reference answers are auditable: table answers are reproduced through executed DuckDB queries, document answers are grounded in verified text spans, and graph answers are traced to source dependency annotations. We evaluate four model backbones across six controlled agent settings, yielding 27,624 protocol-error-free trajectories. Under gold-constrained tool access, agents achieve 98.7-99.8 Route F1, while Answer remains only 56.1-75.3 percent, showing that correct surface selection is necessary but insufficient for task completion. Matched interventions further show that surface hints improve Answer for three of four models, whereas removing irrelevant tools primarily improves routing and efficiency. In an independent three-annotator audit, all 200 sampled tasks pass all six quality criteria by majority vote, with 192 receiving unanimous judgments on every criterion. We release the dataset, construction pipeline, scoring code, and agent harness at https://github.com/haolpku/WorkSurface-Bench.

## 내 메모


