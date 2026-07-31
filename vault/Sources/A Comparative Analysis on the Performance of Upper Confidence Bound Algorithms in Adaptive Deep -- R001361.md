---
type: research-source
item_id: 1361
title: "A Comparative Analysis on the Performance of Upper Confidence Bound Algorithms in Adaptive Deep Neural Networks"
source: "arxiv"
published: "2026-04-27T08:51:44Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.24810"
url: "https://arxiv.org/abs/2604.24810v3"
generated_by: codex-research-db
aliases:
  - "A Comparative Analysis on the Performance of Upper Confidence Bound Algorithms in Adaptive Deep Neural Networks"
topics:
  - "edge-computing"
---

# A Comparative Analysis on the Performance of Upper Confidence Bound Algorithms in Adaptive Deep Neural Networks

[원문 열기](https://arxiv.org/abs/2604.24810v3)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WFD4UGEC`)
- 발행일: 2026-04-27T08:51:44Z
- 저자: Grigorios Papanikolaou, Ioannis Kontopoulos, Konstantinos Tserpes
- 식별자: `arxiv:2604.24810`

## 요약·초록

Edge computing environments impose strict constraints on energy consumption and latency, making the deployment of deep neural networks a significant challenge. Therefore, smart and adaptive inference strategies that dynamically balance computational cost or latency with predictive accuracy are critical in edge computing scenarios. In this work, we build on Adaptive Deep Neural Networks (ADNNs) that employ the Multi-Armed Bandit (MAB) framework. Current literature leverages the first version of the Upper Confidence Bound (UCB1) strategy to dynamically select the optimal confidence threshold, enabling efficient early exits without sacrificing accuracy. However, we introduce four additional Upper Confidence Bound strategies in ADNNs, namely UCB-V, UCB-Tuned, UCB-Bayes, and UCB-BwK, and perform, for the first time, a comparative study of these strategies with respect to trade-offs between accuracy, energy consumption, and latency. The proposed UCB strategies are employed on the ResNet and MobileViT neural networks, and are evaluated on the benchmark datasets of CIFAR-10, CIFAR-10.1, and CIFAR-100. Experimental results demonstrate that all strategies achieve sub-linear cumulative regret, with UCB-Bayes converging the fastest, followed by UCB-Tuned and UCB-V. Finally, UCB-V and UCB-Tuned dominate the Pareto Frontiers of accuracy-latency and accuracy-energy trade-offs. The implementation code is available here: https://github.com/gr3gor1/MAB_UCB

## 내 메모


