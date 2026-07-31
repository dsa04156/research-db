---
type: research-source
item_id: 498
title: "Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent Learning"
source: "arxiv"
published: "2024-05-01T20:03:37Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/icdcs60910.2024.00069"
url: "https://arxiv.org/abs/2405.00839v1"
generated_by: codex-research-db
aliases:
  - "Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent Learning"
topics:
  - "ai-agents"
---

# Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent Learning

[원문 열기](https://arxiv.org/abs/2405.00839v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TBE9U35A`)
- 발행일: 2024-05-01T20:03:37Z
- 저자: Seyed Mahmoud Sajjadi Mohammadabadi, Lei Yang, Feng Yan, Junshan Zhang
- 식별자: `doi:10.1109/icdcs60910.2024.00069`

## 요약·초록

Decentralized Multi-agent Learning (DML) enables collaborative model training while preserving data privacy. However, inherent heterogeneity in agents' resources (computation, communication, and task size) may lead to substantial variations in training time. This heterogeneity creates a bottleneck, lengthening the overall training time due to straggler effects and potentially wasting spare resources of faster agents. To minimize training time in heterogeneous environments, we present a Communication-Efficient Training Workload Balancing for Decentralized Multi-Agent Learning (ComDML), which balances the workload among agents through a decentralized approach. Leveraging local-loss split training, ComDML enables parallel updates, where slower agents offload part of their workload to faster agents. To minimize the overall training time, ComDML optimizes the workload balancing by jointly considering the communication and computation capacities of agents, which hinges upon integer programming. A dynamic decentralized pairing scheduler is developed to efficiently pair agents and determine optimal offloading amounts. We prove that in ComDML, both slower and faster agents' models converge, for convex and non-convex functions. Furthermore, extensive experimental results on popular datasets (CIFAR-10, CIFAR-100, and CINIC-10) and their non-I.I.D. variants, with large models such as ResNet-56 and ResNet-110, demonstrate that ComDML can significantly reduce the overall training time while maintaining model accuracy, compared to state-of-the-art methods. ComDML demonstrates robustness in heterogeneous environments, and privacy measures can be seamlessly integrated for enhanced data protection.

## 내 메모


