---
type: research-source
item_id: 2892
title: "UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning"
source: "arxiv"
published: "2026-09-17T11:49:31Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.20089"
url: "https://arxiv.org/abs/2609.20089v1"
generated_by: codex-research-db
aliases:
  - "UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning"
topics:
  - "ai-agents"
---

# UnifiedPlayers: Enhance Tool-Integrated Reasoning in Agentic Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2609.20089v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JWPCPZME`)
- 발행일: 2026-09-17T11:49:31Z
- 저자: Wenjie Liao, Liangjie Zhao, Zehong Cao
- 식별자: `arxiv:2609.20089`

## 요약·초록

Self-evolving methods reduce the need for human-annotated trajectories by allowing tool-using agents to generate their own training data. Yet existing methods typically separate trajectory generation from evaluation, relying on static verifiers that cannot adapt to emerging failure modes or self-consistency signals that may reinforce errors shared across trajectories. Jointly adapting planning, execution, and evaluation offers a promising alternative, but introduces a fundamental coordination challenge: each component continuously changes the data or feedback used to train the others. We address this challenge with \textbf{UnifiedPlayers}, a cooperative framework comprising a Planning Player that generates tasks, an Execution Player that produces multi-turn trajectories with Python tool calls, and an Evaluation Player that constructs executable verifiers. We design role-specific rewards that coordinate the three players toward a shared learning objective under GRPO. Across two model backbones and twelve reasoning benchmarks, UnifiedPlayers outperforms the strongest prior baseline by at least 3.5\% on mathematical reasoning and 3.9\% on general reasoning tasks. Moreover, the learned verifier achieves 84.2\% adversarial detection accuracy, while its reward signal exhibits 2.03$\times$ higher per-question variance than a self-consistency baseline, providing more discriminative verifications. These results highlight cooperation among specialized players as a promising path toward self-enhanced tool-integrated agents.

## 내 메모


