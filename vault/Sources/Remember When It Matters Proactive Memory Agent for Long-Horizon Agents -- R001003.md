---
type: research-source
item_id: 1003
title: "Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents"
source: "arxiv"
published: "2026-07-09T17:26:28Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.08716"
url: "https://arxiv.org/abs/2607.08716v1"
generated_by: codex-research-db
aliases:
  - "Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents

[원문 열기](https://arxiv.org/abs/2607.08716v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IWEGD7XW`)
- 발행일: 2026-07-09T17:26:28Z
- 저자: Yifan Wu, Lizhu Zhang, Yuhang Zhou, Mingyi Wang, Bo Peng, Serena Li, Xiangjun Fan, Zhuokai Zhao
- 식별자: `arxiv:2607.08716`

## 요약·초록

In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate memory agent runs alongside an unmodified action agent, updating a structured memory bank from the recent trajectory and deciding whether to inject a memory-grounded reminder or remain silent. The module is plug-and-play with frontier action agents and existing agent harnesses. Across Terminal-Bench 2.0 and $τ^2$-Bench, it improves pass@1 for both weaker and stronger action agents, with gains of +8.3 pp on Terminal-Bench and +6.8 pp on $τ^2$-Bench. Ablations show that selective intervention outperforms passive bank exposure, always-on injection, advisor-only guidance, and general retrieval. As an early step toward open-weight memory policies, we train Qwen3.5-27B on SETA using SFT and GRPO, improving validation reward and achieving partial transfer to Terminal-Bench.

## 내 메모


