---
type: research-source
item_id: 51
title: "LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters"
source: "arxiv"
published: "2026-07-19T10:21:30Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.17175"
url: "https://arxiv.org/abs/2607.17175v1"
generated_by: codex-research-db
aliases:
  - "LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters"
topics:
  - "kubernetes"
---

# LMEdge: QoS-Aware LLM Inference Orchestration on Edge Clusters

[원문 열기](https://arxiv.org/abs/2607.17175v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5RMKX3A4`)
- 발행일: 2026-07-19T10:21:30Z
- 저자: Reza Farahani, Zoha Azimi, Mario Colosi, Schahram Dustdar
- 식별자: `arxiv:2607.17175`

## 요약·초록

Large language model (LLM) services increasingly operate on edge infrastructure, enabling low-latency and privacy-preserving AI services. However, efficiently serving LLM requests across heterogeneous and resource-constrained edge devices require orchestration mechanisms that jointly determine model configuration (family, size, and quantization level) and execution placement while satisfying user- and system-level quality of service (QoS) requirements. This paper introduces LMEdge, a QoS-aware orchestration service that dynamically makes these decisions across heterogeneous edge devices. We formulate the problem as a binary integer linear programming (BILP) optimization that minimizes response time under accuracy, network, and resource constraints. To enable scalable online scheduling, we employ five lightweight machine learning (ML) models to predict query-specific latency, accuracy, resource usage, and response size for each model-size-quantization-device combination, and design a lightweight heuristic that approximates the BILP solution. We collect a comprehensive benchmarking dataset of over 59000 rows to train models and support reproducibility. Evaluation on a Kubernetes-based edge testbed with 57 instances and diverse query categories shows that LMEdge reduces latency, preserves accuracy, improves resource utilization, and increases serving ratio compared to two baselines.

## 내 메모


