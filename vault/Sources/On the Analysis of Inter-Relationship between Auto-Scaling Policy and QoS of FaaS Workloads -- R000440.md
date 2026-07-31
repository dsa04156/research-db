---
type: research-source
item_id: 440
title: "On the Analysis of Inter-Relationship between Auto-Scaling Policy and QoS of FaaS Workloads"
source: "openalex"
published: "2024-06-10"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.3390/s24123774"
url: "https://doi.org/10.3390/s24123774"
generated_by: codex-research-db
aliases:
  - "On the Analysis of Inter-Relationship between Auto-Scaling Policy and QoS of FaaS Workloads"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# On the Analysis of Inter-Relationship between Auto-Scaling Policy and QoS of FaaS Workloads

[원문 열기](https://doi.org/10.3390/s24123774)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`I7IKSNHV`)
- 발행일: 2024-06-10
- 저자: Sara Hong, Yeeun Kim, Jaehyun Nam, Seongmin Kim
- 식별자: `doi:10.3390/s24123774`

## 요약·초록

A recent development in cloud computing has introduced serverless technology, enabling the convenient and flexible management of cloud-native applications. Typically, the Function-as-a-Service (FaaS) solutions rely on serverless backend solutions, such as Kubernetes (K8s) and Knative, to leverage the advantages of resource management for underlying containerized contexts, including auto-scaling and pod scheduling. To take the advantages, recent cloud service providers also deploy self-hosted serverless services by facilitating their on-premise hosted FaaS platforms rather than relying on commercial public cloud offerings. However, the lack of standardized guidelines on K8s abstraction to fairly schedule and allocate resources on auto-scaling configuration options for such on-premise hosting environment in serverless computing poses challenges in meeting the service level objectives (SLOs) of diverse workloads. This study fills this gap by exploring the relationship between auto-scaling behavior and the performance of FaaS workloads depending on scaling-related configurations in K8s. Based on comprehensive measurement studies, we derived the logic as to which workload should be applied and with what type of scaling configurations, such as base metric, threshold to maximize the difference in latency SLO, and number of responses. Additionally, we propose a methodology to assess the scaling efficiency of the related K8s configurations regarding the quality of service (QoS) of FaaS workloads.

## 내 메모


