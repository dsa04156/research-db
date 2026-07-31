---
type: research-source
item_id: 1152
title: "CRAWO: Custom Resources for Adaptive Workload Orchestration"
source: "arxiv"
published: "2026-06-08T15:45:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.20490"
url: "https://arxiv.org/abs/2607.20490v1"
generated_by: codex-research-db
aliases:
  - "CRAWO: Custom Resources for Adaptive Workload Orchestration"
topics:
  - "kubernetes"
---

# CRAWO: Custom Resources for Adaptive Workload Orchestration

[원문 열기](https://arxiv.org/abs/2607.20490v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9XS4NWXF`)
- 발행일: 2026-06-08T15:45:03Z
- 저자: Eugênio Santos, Daniel Maia, Stefano Loss, José Manoel Silva, Aluizio Rocha Neto, Thais Batista, Everton Cavalcante, Nélio Cacho, Eduardo Nogueira, Daniel Araújo, Frederico Lopes
- 식별자: `arxiv:2607.20490`

## 요약·초록

Edge Intelligence has emerged as a key paradigm for enabling real-time applications in smart cities by shifting computation from centralized cloud data centers to the network edge, thereby reducing latency and bandwidth consumption. However, deploying Artificial Intelligence (AI) pipelines across heterogeneous edge infrastructures remains challenging due to the wide range of device capabilities, from low-power microcontrollers to accelerator-equipped systems. Existing edge orchestration platforms primarily focus on deployment automation and infrastructure management, but these approaches are often inefficient and limit the ability to adaptively allocate resources under dynamic conditions. To tackle these issues, this paper introduces CRAWO (Custom Resources for Adaptive Workload Orchestration), an architectural framework for coordinating AI pipelines across distributed edge environments. CRAWO follows a control-loop-based model that separates allocation intelligence from execution by managing placement decisions, state management, and inter-stage data flows while instantiating services on edge nodes. The framework incorporates a hardware-aware allocator with a pluggable multi-criteria decision layer that leverages real-time infrastructure metrics to enable adaptive workload placement. The reference implementation adopts a microservices architecture deployed on a lightweight Kubernetes distribution (K3s), using Custom Resource Definitions (CRDs) for domain modeling and a dedicated operator for state reconciliation. Evaluation in a vehicle surveillance scenario using license plate recognition demonstrates improved workload distribution and reduced reliance on centralized cloud processing in latency-sensitive environments.

## 내 메모


