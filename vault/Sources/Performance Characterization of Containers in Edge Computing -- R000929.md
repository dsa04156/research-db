---
type: research-source
item_id: 929
title: "Performance Characterization of Containers in Edge Computing"
source: "arxiv"
published: "2025-05-04T12:21:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.02082"
url: "https://arxiv.org/abs/2505.02082v2"
generated_by: codex-research-db
aliases:
  - "Performance Characterization of Containers in Edge Computing"
topics:
  - "edge-computing"
---

# Performance Characterization of Containers in Edge Computing

[원문 열기](https://arxiv.org/abs/2505.02082v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3GUCAGH5`)
- 발행일: 2025-05-04T12:21:16Z
- 저자: Ragini Gupta, Klara Nahrstedt
- 식별자: `arxiv:2505.02082`

## 요약·초록

Edge computing addresses critical limitations of cloud computing such as high latency and network congestion by decentralizing processing from cloud to the edge. However, the need for software replication across heterogeneous edge devices introduces dependency and portability challenges, driving the adoption of containerization technologies like Docker. While containers offer lightweight isolation and deployment advantages, they introduce new bottlenecks in edge environments, including cold-start delays, memory constraints, network throughput variability, and inefficient IO handling when interfacing with embedded peripherals. This paper presents an empirical evaluation of Docker containers on resource-constrained edge devices, using Raspberry Pi as a representative platform. We benchmark performance across diverse workloads, including microbenchmarks (CPU, memory, network profiling) and macrobenchmarks (AI inference, sensor IO operations), to quantify the overheads of containerization in real-world edge scenarios. Our testbed comprises physical Raspberry Pi nodes integrated with environmental sensors and camera modules, enabling measurements of latency, memory faults, IO throughput, and cold start delays under varying loads. Key findings reveal trade-offs between container isolation and edge-specific resource limitations, with performance degradation observed in IO heavy and latency sensitive tasks. We identify configuration optimizations to mitigate these issues, providing actionable insights for deploying containers in edge environments while meeting real time and reliability requirements. This work advances the understanding of containerized edge computing by systematically evaluating its feasibility and pitfalls on low-power embedded systems.

## 내 메모


