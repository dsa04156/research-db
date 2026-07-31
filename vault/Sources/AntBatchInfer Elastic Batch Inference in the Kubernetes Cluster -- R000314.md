---
type: research-source
item_id: 314
title: "AntBatchInfer: Elastic Batch Inference in the Kubernetes Cluster"
source: "arxiv"
published: "2024-04-15T11:37:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2404.09686"
url: "https://arxiv.org/abs/2404.09686v1"
generated_by: codex-research-db
aliases:
  - "AntBatchInfer: Elastic Batch Inference in the Kubernetes Cluster"
topics:
  - "kubernetes"
---

# AntBatchInfer: Elastic Batch Inference in the Kubernetes Cluster

[원문 열기](https://arxiv.org/abs/2404.09686v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NR86ECR6`)
- 발행일: 2024-04-15T11:37:40Z
- 저자: Siyuan Li, Youshao Xiao, Fanzhuang Meng, Lin Ju, Lei Liang, Lin Wang, Jun Zhou
- 식별자: `arxiv:2404.09686`

## 요약·초록

Offline batch inference is a common task in the industry for deep learning applications, but it can be challenging to ensure stability and performance when dealing with large amounts of data and complicated inference pipelines. This paper demonstrated AntBatchInfer, an elastic batch inference framework, which is specially optimized for the non-dedicated cluster. AntBatchInfer addresses these challenges by providing multi-level fault-tolerant capabilities, enabling the stable execution of versatile and long-running inference tasks. It also improves inference efficiency by pipelining, intra-node, and inter-node scaling. It further optimizes the performance in complicated multiple-model batch inference scenarios. Through extensive experiments and real-world statistics, we demonstrate the superiority of our framework in terms of stability and efficiency. In the experiment, it outperforms the baseline by at least $2\times$ and $6\times$ in the single-model or multiple-model batch inference. Also, it is widely used at Ant Group, with thousands of daily jobs from various scenarios, including DLRM, CV, and NLP, which proves its practicability in the industry.

## 내 메모


