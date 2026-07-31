---
type: research-source
item_id: 1222
title: "Remoe: Towards Efficient and Low-Cost MoE Inference in Serverless Computing"
source: "arxiv"
published: "2025-12-21T10:27:50Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.18674"
url: "https://arxiv.org/abs/2512.18674v1"
generated_by: codex-research-db
aliases:
  - "Remoe: Towards Efficient and Low-Cost MoE Inference in Serverless Computing"
topics:
  - "cloud-infrastructure"
  - "kubernetes"
---

# Remoe: Towards Efficient and Low-Cost MoE Inference in Serverless Computing

[원문 열기](https://arxiv.org/abs/2512.18674v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2K32XCHP`)
- 발행일: 2025-12-21T10:27:50Z
- 저자: Wentao Liu, Yuhao Hu, Ruiting Zhou, Baochun Li, Ne Wang
- 식별자: `arxiv:2512.18674`

## 요약·초록

Mixture-of-Experts (MoE) has become a dominant architecture in large language models (LLMs) due to its ability to scale model capacity via sparse expert activation. Meanwhile, serverless computing, with its elasticity and pay-per-use billing, is well-suited for deploying MoEs with bursty workloads. However, the large number of experts in MoE models incurs high inference costs due to memory-intensive parameter caching. These costs are difficult to mitigate via simple model partitioning due to input-dependent expert activation. To address these issues, we propose Remoe, a heterogeneous MoE inference system tailored for serverless computing. Remoe assigns non-expert modules to GPUs and expert modules to CPUs, and further offloads infrequently activated experts to separate serverless functions to reduce memory overhead and enable parallel execution. We incorporate three key techniques: (1) a Similar Prompts Searching (SPS) algorithm to predict expert activation patterns based on semantic similarity of inputs; (2) a Main Model Pre-allocation (MMP) algorithm to ensure service-level objectives (SLOs) via worst-case memory estimation; and (3) a joint memory and replica optimization framework leveraging Lagrangian duality and the Longest Processing Time (LPT) algorithm. We implement Remoe on Kubernetes and evaluate it across multiple LLM benchmarks. Experimental results show that Remoe reduces inference cost by up to 57% and cold start latency by 47% compared to state-of-the-art baselines.

## 내 메모


