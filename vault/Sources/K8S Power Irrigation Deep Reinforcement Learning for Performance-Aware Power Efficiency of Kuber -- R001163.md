---
type: research-source
item_id: 1163
title: "K8S Power Irrigation: Deep Reinforcement Learning for Performance-Aware Power Efficiency of Kubernetes Cloud-Native Microservices"
source: "arxiv"
published: "2026-05-24T18:54:19Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.25218"
url: "https://arxiv.org/abs/2605.25218v1"
generated_by: codex-research-db
aliases:
  - "K8S Power Irrigation: Deep Reinforcement Learning for Performance-Aware Power Efficiency of Kubernetes Cloud-Native Microservices"
topics:
  - "kubernetes"
---

# K8S Power Irrigation: Deep Reinforcement Learning for Performance-Aware Power Efficiency of Kubernetes Cloud-Native Microservices

[원문 열기](https://arxiv.org/abs/2605.25218v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`983FE36F`)
- 발행일: 2026-05-24T18:54:19Z
- 저자: Zouhir Bellal, Laaziz Lahlou, Nadjia Kara, Timothy Murphy, Tan Phat Nguyen
- 식별자: `arxiv:2605.25218`

## 요약·초록

Modern cloud platforms are facing a sharp increase in power demand driven by the rapid adoption of AI-powered applications, making power optimization urgent under net-zero commitments and sustainability goals. Yet, reducing power in production remains challenging for latency-sensitive microservices, where performance violations directly affect user experience and operational risk. Such services exhibit heterogeneous workload characteristics and dynamic load patterns. In multi-tenant environments, contention on shared uncore resources, including last-level cache and memory bandwidth, can degrade performance, especially for memory-intensive workloads. As a safeguard, providers often run servers in performance mode, fixing core and uncore frequencies at high levels. Existing power governors largely ignore application-level performance requirements and uncore interference, leading to systematic power over-provisioning. To address this, we introduce K8SPI, a hierarchical reinforcement learning controller that jointly optimizes CPU core and uncore frequencies for cloud-native deployments. K8SPI uses a two-stage architecture: a coarse-grained agent rapidly mitigates performance violations, while a fine-grained agent minimizes power once requirements are satisfied. Using telemetry from hardware, Kubernetes, and application layers, K8SPI adapts to workload heterogeneity and cross-microservice interference. We evaluate K8SPI on a Kubernetes testbed across multiple scenarios. Results show that K8SPI reduces node-level power by 23--30\% compared with the Linux performance governor while keeping performance requirement violations below 2--3\%, even under severe uncore contention and dynamic load fluctuations.

## 내 메모


