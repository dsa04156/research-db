---
type: research-source
item_id: 2952
title: "Multi-Agent Event-Triggered LQG Control under Shared Communication Constraints"
source: "arxiv"
published: "2026-09-18T16:36:51Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.21974"
url: "https://arxiv.org/abs/2609.21974v1"
generated_by: codex-research-db
aliases:
  - "Multi-Agent Event-Triggered LQG Control under Shared Communication Constraints"
topics:
  - "ai-agents"
---

# Multi-Agent Event-Triggered LQG Control under Shared Communication Constraints

[원문 열기](https://arxiv.org/abs/2609.21974v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6E6S3QAZ`)
- 발행일: 2026-09-18T16:36:51Z
- 저자: Zahra Hashemi, Dipankar Maity
- 식별자: `arxiv:2609.21974`

## 요약·초록

This letter studies event-triggered linear-quadratic-Gaussian (LQG) control for multi-agent systems sharing a communication network with limited per-step capacity. Although the agent dynamics are decoupled, the communication decisions are coupled through the shared network constraint, leading to a constrained multi-agent scheduling problem. We show that the optimal control law remains certainty-equivalent and decouples across agents through independent finite-horizon Riccati recursions, whereas the transmission schedule remains globally coupled. Based on this structure, we develop a centralized receding-horizon scheduling framework and reformulate the resulting problem as a mixed-integer linear program (MILP) using a closed-form characterization of the estimation-error covariance. To improve scalability, we derive a window-based skip-pruning condition that safely fixes consecutive transmission decisions to zero before solving the MILP, and we propose an auction-inspired scheduler based on one-step transmission-benefit scores. Numerical results show that the proposed model predictive control (MPC) scheduler achieves the best trade-off between control performance and communication cost, while the auction-based scheduler attains performance close to MPC with substantially lower computational complexity.

## 내 메모
