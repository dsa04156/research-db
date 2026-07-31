---
type: research-source
item_id: 716
title: "Disruption-aware Microservice Re-orchestration for Cost-efficient Multi-cloud Deployments"
source: "arxiv"
published: "2025-01-27T15:36:51Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/tsc.2025.3604373"
url: "https://arxiv.org/abs/2501.16143v4"
generated_by: codex-research-db
aliases:
  - "Disruption-aware Microservice Re-orchestration for Cost-efficient Multi-cloud Deployments"
topics:
  - "kubernetes"
---

# Disruption-aware Microservice Re-orchestration for Cost-efficient Multi-cloud Deployments

[원문 열기](https://arxiv.org/abs/2501.16143v4)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KF8NTV82`)
- 발행일: 2025-01-27T15:36:51Z
- 저자: Marco Zambianco, Silvio Cretti, Domenico Siracusa
- 식별자: `doi:10.1109/tsc.2025.3604373`

## 요약·초록

Multi-cloud environments enable a cost-efficient scaling of cloud-native applications across geographically distributed virtual nodes with different pricing models. In this context, the resource fragmentation caused by frequent changes in the resource demands of deployed microservices, along with the allocation or termination of new and existing microservices, increases the deployment cost. Therefore, re-orchestrating deployed microservices on a cheaper configuration of multi-cloud nodes offers a practical solution to restore the cost efficiency of deployment. However, the rescheduling procedure causes frequent service interruptions due to the continuous termination and rebooting of the containerized microservices. Moreover, it may potentially interfere with and delay other deployment operations, compromising the stability of the running applications. To address this issue, we formulate a multi-objective integer linear programming (ILP) problem that computes a microservice rescheduling solution capable of providing minimum deployment cost without significantly affecting the service continuity. At the same time, the proposed formulation also preserves the quality of service (QoS) requirements, including latency, expressed through microservice co-location constraints. Additionally, we present a heuristic algorithm to approximate the optimal solution, striking a balance between cost reduction and service disruption mitigation. We integrate the proposed approach as a custom plugin of the Kubernetes (K8s) scheduler. Results reveal that our approach significantly reduces multi-cloud deployment costs and service disruptions compared to the benchmark schemes, while ensuring QoS requirements are consistently met.

## 내 메모


