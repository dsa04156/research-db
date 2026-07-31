---
type: research-source
item_id: 302
title: "Safety-Critical Edge Robotics Architecture with Bounded End-to-End Latency"
source: "arxiv"
published: "2024-06-20T15:11:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.14391"
url: "https://arxiv.org/abs/2406.14391v2"
generated_by: codex-research-db
aliases:
  - "Safety-Critical Edge Robotics Architecture with Bounded End-to-End Latency"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Safety-Critical Edge Robotics Architecture with Bounded End-to-End Latency

[원문 열기](https://arxiv.org/abs/2406.14391v2)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`M7WZKFSB`)
- 발행일: 2024-06-20T15:11:22Z
- 저자: Gautam Gala, Tilmann Unte, Luiz Maia, Johannes Kühbacher, Isser Kadusale, Mohammad Ibrahim Alkoudsi, Gerhard Fohler, Sebastian Altmeyer
- 식별자: `arxiv:2406.14391`

## 요약·초록

Edge computing processes data near its source, reducing latency and enhancing security compared to traditional cloud computing while providing its benefits. This paper explores edge computing for migrating an existing safety-critical robotics use case from an onboard dedicated hardware solution. We propose an edge robotics architecture based on Linux, Docker containers, Kubernetes, and a local wireless area network based on the TTWiFi protocol. Inspired by previous work on real-time cloud, we complement the architecture with a resource management and orchestration layer to help Linux manage, and Kubernetes orchestrate the system-wide shared resources (e.g., caches, memory bandwidth, and network). Our architecture aims to ensure the fault-tolerant and predictable execution of robotic applications (e.g., path planning) on the edge while upper-bounding the end-to-end latency and ensuring the best possible quality of service without jeopardizing safety and security.

## 내 메모


