---
type: research-source
item_id: 1217
title: "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
source: "arxiv"
published: "2026-01-14T08:36:21Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/access.2026.3665989"
url: "https://arxiv.org/abs/2601.09282v2"
generated_by: codex-research-db
aliases:
  - "Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing"
topics:
  - "kubernetes"
---

# Cluster Workload Allocation: Semantic Soft Affinity Using Natural Language Processing

[원문 열기](https://arxiv.org/abs/2601.09282v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5547JFX9`)
- 발행일: 2026-01-14T08:36:21Z
- 저자: Leszek Sliwko, Jolanta Mizeria-Pietraszko
- 식별자: `doi:10.1109/access.2026.3665989`

## 요약·초록

Cluster workload allocation often requires complex configurations, creating a usability gap. This paper introduces a semantic, intent-driven scheduling paradigm for cluster systems using Natural Language Processing. The system employs a Large Language Model (LLM) integrated via a Kubernetes scheduler extender to interpret natural language allocation hint annotations for soft affinity preferences. A prototype featuring a cluster state cache and an intent analyzer (using AWS Bedrock) was developed. Empirical evaluation demonstrated high LLM parsing accuracy (>95% Subset Accuracy on an evaluation ground-truth dataset) for top-tier models like Amazon Nova Pro/Premier and Mistral Pixtral Large, significantly outperforming a baseline engine. Scheduling quality tests across six scenarios showed the prototype achieved superior or equivalent placement compared to standard Kubernetes configurations, particularly excelling in complex and quantitative scenarios and handling conflicting soft preferences. The results validate using LLMs for accessible scheduling but highlight limitations like synchronous LLM latency, suggesting asynchronous processing for production readiness. This work confirms the viability of semantic soft affinity for simplifying workload orchestration and presents a proof-of-concept design.

## 내 메모


