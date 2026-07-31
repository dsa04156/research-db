---
type: research-source
item_id: 1167
title: "Evaluating Container Orchestration for Neuromorphic Workloads in Virtual Edge Environments"
source: "arxiv"
published: "2026-05-15T11:34:25Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.20124585"
url: "https://arxiv.org/abs/2605.15866v1"
generated_by: codex-research-db
aliases:
  - "Evaluating Container Orchestration for Neuromorphic Workloads in Virtual Edge Environments"
topics:
  - "kubernetes"
  - "edge-computing"
---

# Evaluating Container Orchestration for Neuromorphic Workloads in Virtual Edge Environments

[원문 열기](https://arxiv.org/abs/2605.15866v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8RFANDNA`)
- 발행일: 2026-05-15T11:34:25Z
- 저자: Huyen Pham, Bilhanan Silverajan
- 식별자: `doi:10.5281/zenodo.20124585`

## 요약·초록

The growing adoption of edge computing has created an increasing need for workloads capable of operating under strict resource and energy constraints. Neuromorphic computing, and spiking neural networks (SNNs) in particular, offers an energy-efficient alternative to conventional machine learning through event-driven computation. However, how SNN workloads behave when deployed within modern container orchestration frameworks, especially in edge environments, remains largely unexplored. This paper investigates the feasibility of deploying and orchestrating SNN workloads in a virtual edge environment using Kubernetes, focusing on end-to-end latency, throughput, classification accuracy, infrastructure overhead, and runtime behavior under concurrent load. Experiments were conducted on a single-node K3d cluster running on a Windows 11 host with WSL2 and Docker Desktop. The results show that SNN workloads are highly sensitive to resource availability. Restricting CPU to 0.5 cores increased median latency by 47.6x and reduced throughput by 49x, while the most constrained configuration failed due to insufficient memory. Classification accuracy remained stable across all working configurations. From an orchestration perspective, K3d successfully deployed and scaled SNN workloads, though its default round-robin routing policy introduced significant tail latency under replica scaling, highlighting a mismatch between stateless load-balancing assumptions and long-running inference workloads. Overall, this study provides a baseline for deploying neuromorphic workloads in containerized edge environments and highlights the importance of resource provisioning and orchestration configuration. Future work should explore improved routing strategies, memory optimization, and validation on physical edge hardware.

## 내 메모


