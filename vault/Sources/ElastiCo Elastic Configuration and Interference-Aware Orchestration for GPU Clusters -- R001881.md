---
type: research-source
item_id: 1881
title: "ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters"
source: "arxiv"
published: "2026-08-08T07:09:38Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.07971"
url: "https://arxiv.org/abs/2608.07971v1"
generated_by: codex-research-db
aliases:
  - "ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters"
topics:
  - "kubernetes"
---

# ElastiCo: Elastic Configuration and Interference-Aware Orchestration for GPU Clusters

[원문 열기](https://arxiv.org/abs/2608.07971v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-08T07:09:38Z
- 저자: Jinghao Wang, Yihang Zhou, Xiaoyang Sun, Chunming Hu, Tianyu Wo, Xu Wang, Albert Y. Zomaya, Renyu Yang
- 식별자: `arxiv:2608.07971`

## 요약·초록

Modern GPU clusters must simultaneously serve deep learning training and offline large language model inference workloads, yet existing schedulers treat these as isolated resource consumers with rigid, static allocations. This leaves substantial GPU capacity underutilized: training jobs reserve entire devices despite periodic idle phases, while offline inference tasks over-provision GPUs despite bursty demand patterns. We present ElastiCo, an elastic co-location framework that enables training and inference workloads to safely share GPUs through three integrated mechanisms. First, Resource Shape Transformation exposes each job as a family of feasible resource-performance configurations. Second, Elastic Shadow Pricing decomposes the resulting multi-resource allocation problem into per-job configuration selection subproblems via dynamic per-resource shadow prices. Third, Interference-Aware Co-location uses a predictor trained on hardware-counter and task-level features to estimate pairwise performance degradation under GPU sharing. Implemented as native Kubernetes middleware requiring no user-code modifications, ElastiCo is evaluated on a 64-GPU testbed and through large-scale trace-driven simulations (up to 512 GPUs), reducing the average JCT by up to 2.94x, increasing the cluster throughput by 2.02x, and increasing the GPU utilization from approximately 25% to 46%.

## 내 메모


