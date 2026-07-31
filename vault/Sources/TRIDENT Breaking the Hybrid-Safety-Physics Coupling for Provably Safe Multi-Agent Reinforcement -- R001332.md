---
type: research-source
item_id: 1332
title: "TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning"
source: "arxiv"
published: "2026-06-16T07:41:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.18308"
url: "https://arxiv.org/abs/2606.18308v1"
generated_by: codex-research-db
aliases:
  - "TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning"
topics:
  - "ai-agents"
  - "edge-computing"
---

# TRIDENT: Breaking the Hybrid-Safety-Physics Coupling for Provably Safe Multi-Agent Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2606.18308v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`22GUJCWN`)
- 발행일: 2026-06-16T07:41:43Z
- 저자: Zijie Meng, Ziwei Li, Yufei Liu, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Miao Zhang
- 식별자: `arxiv:2606.18308`

## 요약·초록

Safe coordination in networked cyber-physical systems forces learning algorithms to simultaneously handle hybrid discrete-continuous actions, hard training-time safety constraints, and physics-governed dynamics. We show that these three features form a directed cycle of biases that defeats any naive composition of off-the-shelf modules, and formalize this as a three-way coupling lemma. We then introduce TRIDENT, the first MARL framework whose three components are co-designed to cancel each leak: a Richardson-Romberg gradient correction reducing Gumbel-Softmax bias from O(tau) to O(tau^2), a Lyapunov-constrained sequential trust-region update enforcing per-iterate feasibility, and a physics-informed residual critic that decomposes value rather than reward. We prove an O~(1/sqrt(K)) convergence rate to a constrained Nash equilibrium and an O(sqrt(K)) cumulative-violation bound. On multi-UAV mobile-edge computing, autonomous intersection management, and a hybrid SMAC variant, TRIDENT cuts training-time violations by 95.5% over MADDPG and 76.3% over MACPO, while improving reward by 13.5% over the strongest unconstrained baseline.

## 내 메모


