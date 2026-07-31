---
type: research-source
item_id: 1073
title: "PLATO: Pointer Learner for Agent and Task Openness"
source: "arxiv"
published: "2026-07-27T21:20:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25082"
url: "https://arxiv.org/abs/2607.25082v2"
generated_by: codex-research-db
aliases:
  - "PLATO: Pointer Learner for Agent and Task Openness"
topics:
  - "ai-agents"
---

# PLATO: Pointer Learner for Agent and Task Openness

[원문 열기](https://arxiv.org/abs/2607.25082v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W8UR4UT8`)
- 발행일: 2026-07-27T21:20:13Z
- 저자: Alireza Saleh Abadi, Leen-Kiat Soh, Daniel Alan Redder, Adam Eck, Prashant Doshi
- 식별자: `arxiv:2607.25082`

## 요약·초록

Open agent systems (OASYS) are increasingly prevalent in real-world domains where the sets of agents and tasks change unpredictably over time. Such openness, including agent openness (AO) and task openness (TO), poses a fundamental challenge to multi-agent reinforcement learning (MARL), which typically assumes fixed state and action spaces. Existing methods address openness only partially: padding and masking approaches introduce artificial bounds, while recent graph-based or hypergraph methods handle one dimension of openness but still depend on restrictive assumptions. In this paper, we introduce Pointer Learner for Agent and Task Openness (PLATO), a pointer-network-based actor combined with a centralized graph neural network (GNN) critic, trained with multi-agent proximal policy optimization under a centralized training and decentralized execution paradigm. Our pointer-based actor outputs distributions directly over the current task set. This directly supports changing action spaces without masking or retraining. Our GNN critic encodes agent-task interactions as a graph that changes shape with task and agent composition. Together, these components consider AO and TO without the boundedness of existing approaches. We formalize PLATO in a Task-and-Agent-Open Markov Game (TaAgO-MG), extending prior task-open formulations, and prove it is well-defined over the resulting unbounded state and action spaces. We evaluate PLATO with the Methods for Open Agent Systems Evaluation Initiative (MOASEI) wildfire suppression domain, an environment designed for open multi-agent system evaluation, and we demonstrate strong performance and more consistent zero-shot generalization than state-of-the-art baselines in OASYS.

## 내 메모


