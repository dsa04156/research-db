---
type: research-source
item_id: 694
title: "Adaptive Configuration Selection for Multi-Model Inference Pipelines in Edge Computing"
source: "arxiv"
published: "2025-06-03T12:44:46Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/hpcc64274.2024.00101"
url: "https://arxiv.org/abs/2506.02814v2"
generated_by: codex-research-db
aliases:
  - "Adaptive Configuration Selection for Multi-Model Inference Pipelines in Edge Computing"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Adaptive Configuration Selection for Multi-Model Inference Pipelines in Edge Computing

[원문 열기](https://arxiv.org/abs/2506.02814v2)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XWTJZWSQ`)
- 발행일: 2025-06-03T12:44:46Z
- 저자: Jinhao Sheng, Zhiqing Tang, Jianxiong Guo, Tian Wang
- 식별자: `doi:10.1109/hpcc64274.2024.00101`

## 요약·초록

The growing demand for real-time processing tasks is driving the need for multi-model inference pipelines on edge devices. However, cost-effectively deploying these pipelines while optimizing Quality of Service (QoS) and costs poses significant challenges. Existing solutions often neglect device resource constraints, focusing mainly on inference accuracy and cost efficiency. To address this, we develop a framework for configuring multi-model inference pipelines. Specifically: 1) We model the decision-making problem by considering the pipeline's QoS, costs, and device resource limitations. 2) We create a feature extraction module using residual networks and a load prediction model based on Long Short-Term Memory (LSTM) to gather comprehensive node and pipeline status information. Then, we implement a Reinforcement Learning (RL) algorithm based on policy gradients for online configuration decisions. 3) Experiments conducted in a real Kubernetes cluster show that our approach significantly improve QoS while reducing costs and shorten decision-making time for complex pipelines compared to baseline algorithms.

## 내 메모


