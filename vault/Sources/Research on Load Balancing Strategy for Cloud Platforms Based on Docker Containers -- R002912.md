---
type: research-source
item_id: 2912
title: "Research on Load Balancing Strategy for Cloud Platforms Based on Docker Containers"
source: "openalex"
published: "2026-09-15"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "doi:10.38007/ijmc.2026.070204"
url: "https://doi.org/10.38007/ijmc.2026.070204"
generated_by: codex-research-db
aliases:
  - "Research on Load Balancing Strategy for Cloud Platforms Based on Docker Containers"
topics:
  - "kubernetes"
---

# Research on Load Balancing Strategy for Cloud Platforms Based on Docker Containers

[원문 열기](https://doi.org/10.38007/ijmc.2026.070204)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`5EGF6X64`)
- 발행일: 2026-09-15
- 식별자: `doi:10.38007/ijmc.2026.070204`

## 요약·초록

Given the problems of resource skew, tail latency amplification and frequent migration under bursty traffic in heterogeneous nodes and cross-node network latency of Docker container cloud platforms, a predictive multi-metric load balancing strategy has been designed.This strategy jointly uses CPU, memory, network, queues and energy consumption as the state, applies exponential smoothing for short-term request intensity prediction, and conducts container placement and request distribution via feasible domain filtering, dynamic weight scoring, hysteresis migration, and abnormal node deweighting.Based on public research papers and experimental data from the last three years, this study also has some secondary analysis.According to the above results, at fewer than 16 concurrent requests, a 30ms inter-node latency can reduce throughput by 58.0% under a uniform Pod distribution; localisation and resource-aware scheduling can mitigate this drop significantly.The proposed method takes into account the constraints of load dispersion, P95 latency and migration cost simultaneously to offer an interpretable and deployable load balancing framework for Docker Swarm and other compatible orchestration platforms. Research Background and Objectives of Load Tilt in Docker Container Cloud PlatformsContainers reduce the overhead of virtualisation by sharing the host kernel and can run microservices on cloud platforms with small images, fast startup times, and high deployment density.However, a lightweight Design does not automatically eliminate resource contention: if a large number of requests are directed to a small number of containers over a short period, the CPU and memory capacities of these nodes may become unbalanced, or when service calls cross highlatency links, a round-robin strategy might treat "request quantity balancing" as "system load balancing", resulting in queuing at hot nodes, increased tail latency, and SLA violations.Recently, most research has moved away from a single-CPU threshold to multi-resource cooperation.Qian and others proposed a differentiated resource weighting mechanism for the OpenStack and Docker converged environment, and showed that the matching of container type with node resources directly affects the load dispersion inside and outside the node [1].A review of Kubernetes scheduling algorithms further shows that although general rules, multi-objective

## 내 메모


