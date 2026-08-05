---
type: research-source
item_id: 1676
title: "MDGAM-Based Cooperative Task Scheduling for Communication-Constrained Distributed Multi-Agent Systems"
source: "arxiv"
published: "2026-08-01T13:08:16Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00648"
url: "https://arxiv.org/abs/2608.00648v1"
generated_by: codex-research-db
aliases:
  - "MDGAM-Based Cooperative Task Scheduling for Communication-Constrained Distributed Multi-Agent Systems"
topics:
  - "ai-agents"
---

# MDGAM-Based Cooperative Task Scheduling for Communication-Constrained Distributed Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2608.00648v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7GIH7XGQ`)
- 발행일: 2026-08-01T13:08:16Z
- 저자: Licheng Wang, Mingtao Huang, Yuan Shen
- 식별자: `arxiv:2608.00648`

## 요약·초록

Cooperative task scheduling in communication-constrained distributed multi-agent systems is challenging because each agent must make decisions from partial and dynamic observations while satisfying complex practical constraints. Existing heuristics rely on handcrafted bidding rules and repeated consensus, whereas many learning-based methods assume global observations and lack explicit communication-based coordination. To address these limitations, this paper proposes a neural scheduling framework for distributed multi-robot task allocation (MRTA), consisting of a multi-decoder graph attention model (MDGAM) policy model and a critic-free group relative multi-agent policy gradient (GRMAPG) training algorithm. MDGAM uses an extended graph attention mechanism to jointly update node and edge features, and employs multiple decoders to generate task-selection decisions and communication messages. GRMAPG constructs group-relative advantages from equivalent task-planning instances to replace the critic network used in conventional MARL algorithms, thereby reducing training difficulty and improving convergence performance. Experiments under different problem scales and communication ranges show that the proposed method improves task-completion performance over existing heuristic and learning-based methods, while ablation, complexity, and generalization tests further validate the proposed innovations.

## 내 메모


