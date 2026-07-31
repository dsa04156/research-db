---
type: research-source
item_id: 1205
title: "Performance Optimization in Stream Processing Systems: Experiment-Driven Configuration Tuning for Kafka Streams"
source: "arxiv"
published: "2026-03-04T13:04:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3777911.3800636"
url: "https://arxiv.org/abs/2603.04027v1"
generated_by: codex-research-db
aliases:
  - "Performance Optimization in Stream Processing Systems: Experiment-Driven Configuration Tuning for Kafka Streams"
topics:
  - "kubernetes"
---

# Performance Optimization in Stream Processing Systems: Experiment-Driven Configuration Tuning for Kafka Streams

[원문 열기](https://arxiv.org/abs/2603.04027v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`Z92VE63G`)
- 발행일: 2026-03-04T13:04:03Z
- 저자: David Chen, Sören Henning, Kassiano Matteussi, Rick Rabiser
- 식별자: `doi:10.1145/3777911.3800636`

## 요약·초록

Configuring stream processing systems for efficient performance, especially in cloud-native deployments, is a challenging and largely manual task. We present an experiment-driven approach for automated configuration optimization that combines three phases: Latin Hypercube Sampling for initial exploration, Simulated Annealing for guided stochastic search, and Hill Climbing for local refinement. The workflow is integrated with the cloud-native Theodolite benchmarking framework, enabling automated experiment orchestration on Kubernetes and early termination of underperforming configurations. In an experimental evaluation with Kafka Streams and a Kubernetes-based cloud testbed, our approach identifies configurations that improve throughput by up to 23% over the default. The results indicate that Latin Hypercube Sampling with early termination and Simulated Annealing are particularly effective in navigating the configuration space, whereas additional fine-tuning via Hill Climbing yields limited benefits.

## 내 메모


