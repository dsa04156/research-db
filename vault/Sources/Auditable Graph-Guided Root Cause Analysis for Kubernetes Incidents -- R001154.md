---
type: research-source
item_id: 1154
title: "Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents"
source: "arxiv"
published: "2026-06-07T12:05:09Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.08590"
url: "https://arxiv.org/abs/2606.08590v1"
generated_by: codex-research-db
aliases:
  - "Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents"
topics:
  - "kubernetes"
---

# Auditable Graph-Guided Root Cause Analysis for Kubernetes Incidents

[원문 열기](https://arxiv.org/abs/2606.08590v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`536IR7KE`)
- 발행일: 2026-06-07T12:05:09Z
- 저자: Anastasiia Kuvshinova, Seungmin Jin
- 식별자: `arxiv:2606.08590`

## 요약·초록

Kubernetes incidents are diagnosed reliably only when a root-cause system's reported gains come from incident evidence rather than scenario-specific shortcuts. We present Graph Traversal Agent, a graph-guided RCA agent that combines LLM reasoning with specialized tools. The model reasons over a typed evidence graph, while deterministic graph and tool operations collect evidence, bound the search, and check proposed verdicts. We map operational constraints, including read-only evidence collection, propagation-aware diagnosis, bounded execution, and independently validated verdicts, to a typed incident graph, a LangGraph traversal state machine, and a separate validation stage. On ITBench snapshots scored by one fixed qwen-plus judge, the audited system raises root-cause-entity F1 over an earlier iteration of the same system from 0.6087 to 0.9130 on a 23-scenario common subset. A prompt-level ablation separates prompt-tuned gains from gains that survive once scenario-specific hints are removed: the stripped-prompt configuration retains 0.6958 F1 on a 19-scenario subset. The surviving gain concentrates on ChaosMesh scenarios whose ground-truth root cause is the injected fault object already present in the evidence graph, so we report it as benchmark-coupled rather than broad cross-cluster RCA evidence. Lightweight checks, including same-judge comparison, prompt-level ablation, cascade-source checking, and a telemetry no-leak test, mark claims as supported, pending, or out of scope. We scope the work to ITBench OpenTelemetry-demo snapshots. Live-cluster trials served as an engineering stress test, but alert state and trace availability did not stay stable enough for controlled scoring, so we make no production-readiness or mean-time-to-repair claim.

## 내 메모


