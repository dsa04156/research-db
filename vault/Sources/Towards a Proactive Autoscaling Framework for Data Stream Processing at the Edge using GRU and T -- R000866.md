---
type: research-source
item_id: 866
title: "Towards a Proactive Autoscaling Framework for Data Stream Processing at the Edge using GRU and Transfer Learning"
source: "arxiv"
published: "2025-07-19T12:47:50Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.14597"
url: "https://arxiv.org/abs/2507.14597v1"
generated_by: codex-research-db
aliases:
  - "Towards a Proactive Autoscaling Framework for Data Stream Processing at the Edge using GRU and Transfer Learning"
topics:
  - "kubernetes"
  - "edge-computing"
---

# Towards a Proactive Autoscaling Framework for Data Stream Processing at the Edge using GRU and Transfer Learning

[원문 열기](https://arxiv.org/abs/2507.14597v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZMXXRN6A`)
- 발행일: 2025-07-19T12:47:50Z
- 저자: Eugene Armah, Linda Amoako Bannning
- 식별자: `arxiv:2507.14597`

## 요약·초록

Processing data at high speeds is becoming increasingly critical as digital economies generate enormous data. The current paradigms for timely data processing are edge computing and data stream processing (DSP). Edge computing places resources closer to where data is generated, while stream processing analyzes the unbounded high-speed data in motion. However, edge stream processing faces rapid workload fluctuations, complicating resource provisioning. Inadequate resource allocation leads to bottlenecks, whereas excess allocation results in wastage. Existing reactive methods, such as threshold-based policies and queuing theory scale only after performance degrades, potentially violating SLAs. Although reinforcement learning (RL) offers a proactive approach through agents that learn optimal runtime adaptation policies, it requires extensive simulation. Furthermore, predictive machine learning models face online distribution and concept drift that minimize their accuracy. We propose a three-step solution to the proactive edge stream processing autoscaling problem. Firstly, a GRU neural network forecasts the upstream load using real-world and synthetic DSP datasets. Secondly, a transfer learning framework integrates the predictive model into an online stream processing system using the DTW algorithm and joint distribution adaptation to handle the disparities between offline and online domains. Finally, a horizontal autoscaling module dynamically adjusts the degree of operator parallelism, based on predicted load while considering edge resource constraints. The lightweight GRU model for load predictions recorded up to 1.3\% SMAPE value on a real-world data set. It outperformed CNN, ARIMA, and Prophet on the SMAPE and RMSE evaluation metrics, with lower training time than the computationally intensive RL models.

## 내 메모


