---
type: research-source
item_id: 1743
title: "Training Small LLMs as Spatial Multi-Agent Policies"
source: "arxiv"
published: "2026-08-02T18:14:40Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01425"
url: "https://arxiv.org/abs/2608.01425v1"
generated_by: codex-research-db
aliases:
  - "Training Small LLMs as Spatial Multi-Agent Policies"
topics:
  - "ai-agents"
---

# Training Small LLMs as Spatial Multi-Agent Policies

[원문 열기](https://arxiv.org/abs/2608.01425v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SND5QGQC`)
- 발행일: 2026-08-02T18:14:40Z
- 저자: Yi Mao, Andrew Perrault
- 식별자: `arxiv:2608.01425`

## 요약·초록

Training LLM-based multi-agent systems with multi-agent reinforcement learning is rapidly gaining traction, and a parallel line of work argues that such systems should be judged by their behavior, not only their reward. We take up both threads in spatial cooperative games, where small frozen LLMs prompted with low-level actions fail outright, earning zero reward. Guided by the options/semi-MDP framework---and, because option execution is asynchronous across agents, its multi-agent extension in macro-action Dec-POMDPs---we equip each game with a library of symbolic \emph{options}: typed, state-feasible, short-horizon behaviors executed by a symbolic planner. Each library is drafted by a frontier coding model from the game's source code; the feasibility guards that filter each menu are then synthesized mechanically from cheap random-policy burn-in rollouts---a guard is adopted only if it explains repeated execution failures while hiding no logged success---so no guard is authored, selected, or reward-tuned by hand. Each agent's LLM acts as its policy over options, with a private per-agent LoRA adapter trained by a per-agent variant of multi-agent GRPO (PA-MAGRPO); this lifts frozen bases from zero reward to competent play across three games and four small backbones. Behavioral audits then reveal that reward and cooperation decouple: a rising reward curve may simply mean that one agent has learned to run the entire task alone while its partner idles---cooperation emerges only when the task makes it necessary. Reward alone is thus an unreliable readout of cooperation; behavioral evaluation must sit alongside it.

## 내 메모


