---
type: research-source
item_id: 1351
title: "HiRL: Hierarchical Reinforcement Learning for Coordinated Resource Management in Heterogeneous Edge Computing"
source: "arxiv"
published: "2026-05-11T12:14:45Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.10443"
url: "https://arxiv.org/abs/2605.10443v1"
generated_by: codex-research-db
aliases:
  - "HiRL: Hierarchical Reinforcement Learning for Coordinated Resource Management in Heterogeneous Edge Computing"
topics:
  - "edge-computing"
---

# HiRL: Hierarchical Reinforcement Learning for Coordinated Resource Management in Heterogeneous Edge Computing

[원문 열기](https://arxiv.org/abs/2605.10443v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZK2AJX4W`)
- 발행일: 2026-05-11T12:14:45Z
- 저자: Jianyong Zhu, Hao Chen, Juan Zhang, Fangda Guo, Albert Y. Zomaya, Renyu Yang
- 식별자: `arxiv:2605.10443`

## 요약·초록

Edge computing faces unprecedented resource orchestration challenges from multi-dimensional heterogeneity across device architectures, diverse task requirements in CPU-intensive, GPU-intensive, I/O-intensive, and dynamic network conditions. The edge environments demand real-time task processing within strict energy budgets, yet conventional approaches struggle with mixed continuous-discrete optimization while meeting deadline and energy constraints. This paper presents HiRL, a hierarchical reinforcement learning framework that decomposes complex resource orchestration into coordinated power control and task allocation decisions. Our approach separates continuous power management using the Twin Delayed Deep Deterministic Policy Gradient (TD3) and discrete task placement using Double Deep Q-Network (DDQN), unified through a coordination engine with five-dimensional queue state representation. We propose a heterogeneous assessment of resource compatibility with deadline-oriented prioritization and failure-penalized adaptive sampling to enhance decision quality under resource constraints. To improve practical applicability, the framework models comprehensive system dynamics including device mobility, queue congestion patterns, infrastructure heterogeneity, and priority-sensitive scheduling demands. Experimental results show that HiRL achieves effective latency-energy trade-offs with 28% latency reduction compared to Single-DDQN and maintains nearly 100% task completion rates under all load conditions. Compared to baseline algorithms, HiRL reduces energy consumption by up to 51% under low load while achieving 24% better latency performance than static optimization approaches under high load, establishing effective resource orchestration in heterogeneous edge environments.

## 내 메모


