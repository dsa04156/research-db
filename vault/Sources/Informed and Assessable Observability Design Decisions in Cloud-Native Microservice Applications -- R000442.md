---
type: research-source
item_id: 442
title: "Informed and Assessable Observability Design Decisions in Cloud-Native Microservice Applications"
source: "openalex"
published: "2024-06-04"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/icsa59870.2024.00015"
url: "https://doi.org/10.1109/icsa59870.2024.00015"
generated_by: codex-research-db
aliases:
  - "Informed and Assessable Observability Design Decisions in Cloud-Native Microservice Applications"
topics:
  - "kubernetes"
---

# Informed and Assessable Observability Design Decisions in Cloud-Native Microservice Applications

[원문 열기](https://doi.org/10.1109/icsa59870.2024.00015)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`VNMU9UKI`)
- 발행일: 2024-06-04
- 저자: Maria C. Borges, Joshua Bauer, Sebastian Werner, Michael Gebauer, Stefan Tai
- 식별자: `doi:10.1109/icsa59870.2024.00015`

## 요약·초록

Observability is important to ensure the reliability of microservice applications. These applications are often prone to failures, since they have many independent services deployed on heterogeneous environments. When employed “correctly”, observability can help developers identify and troubleshoot faults quickly. However, instrumenting and configuring the observability of a microservice application is not trivial but tool-dependent and tied to costs. Architects need to understand observability-related trade-offs in order to weigh between different observability design alternatives. Still, these architectural design decisions are not supported by systematic methods and typically just rely on “professional intuition”. In this paper, we argue for a systematic method to arrive at informed and continuously assessable observability design decisions. Specifically, we focus on fault observability of cloud-native microservice applications, and turn this into a testable and quantifiable property. Towards our goal, we first model the scale and scope of observability design decisions across the cloud-native stack. Then, we propose observability metrics which can be determined for any microservice application through so-called observability experiments. We present a proof-of-concept implementation of our experiment tool Oxn. Oxn is able to inject arbitrary faults into an application, similar to Chaos Engineering, but also possesses the unique capability to modify the observability configuration, allowing for the assessment of design decisions that were previously left unexplored. We demonstrate our approach using a popular open source microservice application and show the trade-offs involved in different observability design decisions.

## 내 메모


