---
type: research-source
item_id: 21
title: "Current Trends in Artificial Intelligence Architectures: From Model Scaling to System Intelligence, Post-Transformer Hybrids and World Models"
source: "openalex"
published: "2026-07-23"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.3390/electronics15153254"
url: "https://doi.org/10.3390/electronics15153254"
generated_by: codex-research-db
aliases:
  - "Current Trends in Artificial Intelligence Architectures: From Model Scaling to System Intelligence, Post-Transformer Hybrids and World Models"
topics:
  - "edge-computing"
---

# Current Trends in Artificial Intelligence Architectures: From Model Scaling to System Intelligence, Post-Transformer Hybrids and World Models

[원문 열기](https://doi.org/10.3390/electronics15153254)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`RJZX3W2P`)
- 발행일: 2026-07-23
- 저자: Salvatore Rampone
- 식별자: `doi:10.3390/electronics15153254`

## 요약·초록

Artificial intelligence architecture is no longer adequately described by model size alone. Dense Transformers remain the reference architecture for language and multimodal reasoning, but production systems increasingly combine conditional computation, retrieval, memory, tools, verifiers, edge-cloud routing, observability and governance. This review makes three engineering claims. First, sparse Mixture-of-Experts models are currently the clearest capacity-scaling pattern, because they decouple total parameters from active per-token computation, although routing imbalance and distributed communication remain hard constraints. Second, state-space, recurrent and linear attention hybrids are best interpreted as attention-budgeting architectures: they reduce KV-cache and long-context costs, but do not yet displace dense attention in every reasoning regime. Third, JEPA-style latent world models change the learning objective from surface-token or pixel prediction to representation prediction, which is strategically important for perception and planning but still not a drop-in replacement for general language interfaces. To make the maturity claims auditable, this review uses a PRISMA-inspired search protocol, an explicit technology readiness rubric, quantitative comparison tables, hardware and memory-bandwidth analysis, deployment and reproducibility categories, and failure cases for RAG and agents. The main conclusion is that the optimal architecture is task- and constraint-dependent: small dense or hybrid models are often preferred for real-time edge inference, RAG and graph memory for changing enterprise knowledge, frontier dense or sparse models for difficult reasoning, and agentic workflows only when tool permissions, rollback, provenance and human oversight are engineered as first-class components.

## 내 메모


