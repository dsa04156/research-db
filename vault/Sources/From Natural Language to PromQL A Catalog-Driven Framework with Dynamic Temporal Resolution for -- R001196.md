---
type: research-source
item_id: 1196
title: "From Natural Language to PromQL: A Catalog-Driven Framework with Dynamic Temporal Resolution for Cloud-Native Observability"
source: "arxiv"
published: "2026-03-15T18:48:15Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.13048"
url: "https://arxiv.org/abs/2604.13048v1"
generated_by: codex-research-db
aliases:
  - "From Natural Language to PromQL: A Catalog-Driven Framework with Dynamic Temporal Resolution for Cloud-Native Observability"
topics:
  - "kubernetes"
---

# From Natural Language to PromQL: A Catalog-Driven Framework with Dynamic Temporal Resolution for Cloud-Native Observability

[원문 열기](https://arxiv.org/abs/2604.13048v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GFTN88BR`)
- 발행일: 2026-03-15T18:48:15Z
- 저자: Twinkll Sisodia
- 식별자: `arxiv:2604.13048`

## 요약·초록

Modern cloud-native platforms expose thousands of time series metrics through systems like Prometheus, yet formulating correct queries in domain-specific languages such as PromQL remains a significant barrier for platform engineers and site reliability teams. We present a catalog-driven framework that translates natural language questions into executable PromQL queries, bridging the gap between human intent and observability data. Our approach introduces three contributions: (1) a hybrid metrics catalog that combines a statically curated base of approximately 2,000 metrics with runtime discovery of hardware-specific signals across GPU vendors, (2) a multi-stage query pipeline with intent classification, category-aware metric routing, and multi-dimensional semantic scoring, and (3) a dynamic temporal resolution mechanism that interprets diverse natural language time expressions and maps them to appropriate PromQL duration syntax. We integrate the framework with the Model Context Protocol (MCP) to enable tool-augmented LLM interactions across multiple providers. The catalog-driven approach achieves sub-second metric discovery through pre-computed category indices, with the full pipeline completing in approximately 1.1 seconds via the catalog path. The system has been deployed on production Kubernetes clusters managing AI inference workloads, where it supports natural language querying across approximately 2,000 metrics spanning cluster health, GPU utilization, and model-serving performance.

## 내 메모


