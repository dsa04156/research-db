---
type: research-source
item_id: 1737
title: "Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation"
source: "arxiv"
published: "2026-08-03T14:58:06Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02345"
url: "https://arxiv.org/abs/2608.02345v1"
generated_by: codex-research-db
aliases:
  - "Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation"
topics:
  - "ai-agents"
---

# Can AI Agents Simulate A/B Test Outcomes? A Validation Framework for Agentic Experimentation

[원문 열기](https://arxiv.org/abs/2608.02345v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NH7FB642`)
- 발행일: 2026-08-03T14:58:06Z
- 저자: Stefan Hut, Lorenzo Masoero
- 식별자: `arxiv:2608.02345`

## 요약·초록

A/B testing remains the standard for rolling out new features in the technology industry. Each experiment, however, consumes real traffic, engineering effort, and weeks of wall-clock time. Can AI agents---conditioned on behavioral profiles and contextual descriptions of the intervention---simulate outcomes accurately enough to vet candidate treatments before committing live traffic? We formalize this question as a \emph{Simulated Randomized Controlled Trial} (S-RCT) and derive a two-layer error decomposition that separates agent approximation error from subsampling error, enabling targeted improvements to each. The framework is agent-agnostic: any behavioral model---from a fine-tuned specialist to a general-purpose foundation model---can serve as the simulation engine. Validated on 67 historical marketing A/B tests, a baseline S-RCT using an off-the-shelf foundation model captures directional signal (sign overlap 0.70) but systematically overshoots effect magnitudes. A two-phase pre-period calibration protocol reduces the squared prediction error (after removing irreducible measurement noise) by ${\sim}77\times$; a within-subject design---where each agent is exposed to both arms---reduces standard errors by ${\sim}2.4\times$. We discuss limitations of the current approach and identify applications where experimenters stand to benefit from agentic signals.

## 내 메모


