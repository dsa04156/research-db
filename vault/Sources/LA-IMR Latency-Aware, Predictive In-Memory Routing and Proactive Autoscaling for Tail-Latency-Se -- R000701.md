---
type: research-source
item_id: 701
title: "LA-IMR: Latency-Aware, Predictive In-Memory Routing and Proactive Autoscaling for Tail-Latency-Sensitive Cloud Robotics"
source: "arxiv"
published: "2025-05-12T10:12:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.07417"
url: "https://arxiv.org/abs/2505.07417v3"
generated_by: codex-research-db
aliases:
  - "LA-IMR: Latency-Aware, Predictive In-Memory Routing and Proactive Autoscaling for Tail-Latency-Sensitive Cloud Robotics"
topics:
  - "edge-computing"
  - "kubernetes"
---

# LA-IMR: Latency-Aware, Predictive In-Memory Routing and Proactive Autoscaling for Tail-Latency-Sensitive Cloud Robotics

[원문 열기](https://arxiv.org/abs/2505.07417v3)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GSA8GMEA`)
- 발행일: 2025-05-12T10:12:24Z
- 저자: Eunil Seo, Chanh Nguyen, Erik Elmroth
- 식별자: `arxiv:2505.07417`

## 요약·초록

Hybrid cloud-edge infrastructures now support latency-critical workloads ranging from autonomous vehicles and surgical robotics to immersive AR/VR. However, they continue to experience crippling long-tail latency spikes whenever bursty request streams exceed the capacity of heterogeneous edge and cloud tiers. To address these long-tail latency issues, we present Latency-Aware, Predictive In-Memory Routing and Proactive Autoscaling (LA-IMR). This control layer integrates a closed-form, utilization-driven latency model with event-driven scheduling, replica autoscaling, and edge-to-cloud offloading to mitigate 99th-percentile (P99) delays. Our analytic model decomposes end-to-end latency into processing, network, and queuing components, expressing inference latency as an affine power-law function of instance utilization. Once calibrated, it produces two complementary functions that drive: (i) millisecond-scale routing decisions for traffic offloading, and (ii) capacity planning that jointly determines replica pool sizes. LA-IMR enacts these decisions through a quality-differentiated, multi-queue scheduler and a custom-metric Kubernetes autoscaler that scales replicas proactively -- before queues build up -- rather than reactively based on lagging CPU metrics. Across representative vision workloads (YOLOv5m and EfficientDet) and bursty arrival traces, LA-IMR reduces P99 latency by up to 20.7 percent compared to traditional latency-only autoscaling, laying a principled foundation for next-generation, tail-tolerant cloud-edge inference services.

## 내 메모


