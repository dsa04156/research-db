---
type: research-source
item_id: 1214
title: "A Kubernetes custom scheduler based on reinforcement learning for compute-intensive pods"
source: "arxiv"
published: "2026-01-20T04:06:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2601.13579"
url: "https://arxiv.org/abs/2601.13579v1"
generated_by: codex-research-db
aliases:
  - "A Kubernetes custom scheduler based on reinforcement learning for compute-intensive pods"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# A Kubernetes custom scheduler based on reinforcement learning for compute-intensive pods

[원문 열기](https://arxiv.org/abs/2601.13579v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QD9XS3QU`)
- 발행일: 2026-01-20T04:06:24Z
- 저자: Hanlin Zhou, Huah Yong Chan, Shun Yao Zhang, Meie Lin, Jingfei Ni
- 식별자: `arxiv:2601.13579`

## 요약·초록

With the rise of cloud computing and lightweight containers, Docker has emerged as a leading technology for rapid service deployment, with Kubernetes responsible for pod orchestration. However, for compute-intensive workloads-particularly web services executing containerized machine-learning training-the default Kubernetes scheduler does not always achieve optimal placement. To address this, we propose two custom, reinforcement-learning-based schedulers, SDQN and SDQN-n, both built on the Deep Q-Network (DQN) framework. In compute-intensive scenarios, these models outperform the default Kubernetes scheduler as well as Transformer-and LSTM-based alternatives, reducing average CPU utilization per cluster node by 10%, and by over 20% when using SDQN-n. Moreover, our results show that SDQN-n approach of consolidating pods onto fewer nodes further amplifies resource savings and helps advance greener, more energy-efficient data centers.Therefore, pod scheduling must employ different strategies tailored to each scenario in order to achieve better performance.Since the reinforcement-learning components of the SDQN and SDQN-n architectures proposed in this paper can be easily tuned by adjusting their parameters, they can accommodate the requirements of various future scenarios.

## 내 메모


