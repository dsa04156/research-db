---
type: research-source
item_id: 754
title: "A distributed architecture of reactive microservices orchestrated by kubernetes case study on load balancing in local cloud"
source: "openalex"
published: "2025-06-12"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.11606/d.55.2025.tde-09092025-191832"
url: "https://doi.org/10.11606/d.55.2025.tde-09092025-191832"
generated_by: codex-research-db
aliases:
  - "A distributed architecture of reactive microservices orchestrated by kubernetes case study on load balancing in local cloud"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# A distributed architecture of reactive microservices orchestrated by kubernetes case study on load balancing in local cloud

[원문 열기](https://doi.org/10.11606/d.55.2025.tde-09092025-191832)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`UR3AAAPS`)
- 발행일: 2025-06-12
- 저자: Gustavo Mota Freire
- 식별자: `doi:10.11606/d.55.2025.tde-09092025-191832`

## 요약·초록

Reactive architectures represent a design paradigm centered on responsiveness, resilience, elasticity, and message-driven communication-qualities essential for handling high concurrency in modern distributed systems.This work addressed the design, implementation, and evaluation of a reactive distributed software architecture for high-concurrency scenarios, combining microservices, container orchestration with Kubernetes, cloud design patterns, and asynchronous event streams.Deployed on a local cloud data center (LaSDPC/ICMC/USP), the architecture leveraged well-known design patterns (e.g., Singleton, Bulkhead, Circuit Breaker) and explored optimized topologies to support read-intensive workloads at scale.To address limitations inherent in non-reactive approaches, multiple load-balancing algorithms were tested, and an AI-based observability service was developed to augment real-time orchestration insights.The principal contributions of this work are fourfold: (i) an in-depth analysis of resilience and elasticity scenarios where the orchestrator dynamically expands or reduces infrastructure resources, demonstrating increased reactivity, minimal downtime, and faster recovery in both the messaging subsystem and service nodes; (ii) a systematic performance evaluation of multiple load-balancing strategies (e.g., Round Robin, EWMA) under intense workloads of up to 50,000 concurrent requests, quantifying how reactive design principles can maintain low-latency communication and high throughput; (iii) a read-intensive framework comprising database read replicas, connection pooling, and distributed network/service layers to support large volumes of read operations without linearly increasing hardware demands and (iv) a specialized AI-based observability service that integrates log and telemetry analysis to suggest real-time adjustments for distinct load distributions.Conclusions emphasized the architecture's robustness and scalability, highlighting the critical role of load-balancing strategies.Overall, this work offered a concrete foundation for building modern, highly flexible distributed systems that aligned with reactive principles and leveraged intelligent observability to meet evolving operational demands.

## 내 메모


