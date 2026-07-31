---
type: research-source
item_id: 497
title: "Gradient-Congruity Guided Federated Sparse Training"
source: "arxiv"
published: "2024-05-02T11:29:48Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.01189"
url: "https://arxiv.org/abs/2405.01189v1"
generated_by: codex-research-db
aliases:
  - "Gradient-Congruity Guided Federated Sparse Training"
topics:
  - "edge-computing"
---

# Gradient-Congruity Guided Federated Sparse Training

[원문 열기](https://arxiv.org/abs/2405.01189v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HDN8CG4A`)
- 발행일: 2024-05-02T11:29:48Z
- 저자: Chris Xing Tian, Yibing Liu, Haoliang Li, Ray C. C. Cheung, Shiqi Wang
- 식별자: `arxiv:2405.01189`

## 요약·초록

Edge computing allows artificial intelligence and machine learning models to be deployed on edge devices, where they can learn from local data and collaborate to form a global model. Federated learning (FL) is a distributed machine learning technique that facilitates this process while preserving data privacy. However, FL also faces challenges such as high computational and communication costs regarding resource-constrained devices, and poor generalization performance due to the heterogeneity of data across edge clients and the presence of out-of-distribution data. In this paper, we propose the Gradient-Congruity Guided Federated Sparse Training (FedSGC), a novel method that integrates dynamic sparse training and gradient congruity inspection into federated learning framework to address these issues. Our method leverages the idea that the neurons, in which the associated gradients with conflicting directions with respect to the global model contain irrelevant or less generalized information for other clients, and could be pruned during the sparse training process. Conversely, the neurons where the associated gradients with consistent directions could be grown in a higher priority. In this way, FedSGC can greatly reduce the local computation and communication overheads while, at the same time, enhancing the generalization abilities of FL. We evaluate our method on challenging non-i.i.d settings and show that it achieves competitive accuracy with state-of-the-art FL methods across various scenarios while minimizing computation and communication costs.

## 내 메모


