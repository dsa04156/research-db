---
type: research-source
item_id: 881
title: "Intra-DP: A High Performance Collaborative Inference System for Mobile Edge Computing"
source: "arxiv"
published: "2025-07-08T09:50:57Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.05829"
url: "https://arxiv.org/abs/2507.05829v2"
generated_by: codex-research-db
aliases:
  - "Intra-DP: A High Performance Collaborative Inference System for Mobile Edge Computing"
topics:
  - "edge-computing"
---

# Intra-DP: A High Performance Collaborative Inference System for Mobile Edge Computing

[원문 열기](https://arxiv.org/abs/2507.05829v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RAEPAA6A`)
- 발행일: 2025-07-08T09:50:57Z
- 저자: Zekai Sun, Xiuxian Guan, Zheng Lin, Zihan Fang, Xiangming Cai, Zhe Chen, Fangming Liu, Heming Cui, Jie Xiong, Wei Ni, Chau Yuen
- 식별자: `arxiv:2507.05829`

## 요약·초록

Deploying deep neural networks (DNNs) on resource-constrained mobile devices presents significant challenges, particularly in achieving real-time performance while simultaneously coping with limited computational resources and battery life. While Mobile Edge Computing (MEC) offers collaborative inference with GPU servers as a promising solution, existing approaches primarily rely on layer-wise model partitioning and undergo significant transmission bottlenecks caused by the sequential execution of DNN operations. To address this challenge, we present Intra-DP, a high-performance collaborative inference system optimized for DNN inference on MEC. Intra DP employs a novel parallel computing technique based on local operators (i.e., operators whose minimum unit input is not the entire input tensor, such as the convolution kernel). By decomposing their computations (operations) into several independent sub-operations and overlapping the computation and transmission of different sub-operations through parallel execution, Intra-DP mitigates transmission bottlenecks in MEC, achieving fast and energy-efficient inference. The evaluation demonstrates that Intra-DP reduces per-inference latency by up to 50% and energy consumption by up to 75% compared to state-of-the-art baselines, without sacrificing accuracy.

## 내 메모


