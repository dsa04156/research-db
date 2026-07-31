---
type: research-source
item_id: 548
title: "WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis"
source: "arxiv"
published: "2025-07-06T12:31:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.04370"
url: "https://arxiv.org/abs/2507.04370v1"
generated_by: codex-research-db
aliases:
  - "WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis"
topics:
  - "self-evolving-harness"
---

# WebSynthesis: World-Model-Guided MCTS for Efficient WebUI-Trajectory Synthesis

[원문 열기](https://arxiv.org/abs/2507.04370v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6ED8NIIW`)
- 발행일: 2025-07-06T12:31:10Z
- 저자: Yifei Gao, Junhong Ye, Jiaqi Wang, Jitao Sang
- 식별자: `arxiv:2507.04370`

## 요약·초록

Recent advancements in large language models (LLMs) have significantly improved the capabilities of web agents. However, effectively navigating complex and dynamic web environments still requires more advanced trajectory-level planning and execution. Prior studies have addressed self-improving agents by collecting extensive GUI trajectories from real-environment interactions. Despite their effectiveness, these approaches encounter two critical challenges: (1) Uncontrollable environment states, where real or sandboxed web environments often yield unstable and non-deterministic feedback, complicating the reproduction and debugging of agent behaviors; and (2) High API costs, as generating even a single interaction trajectory can involve hundreds of queries, leading to considerable API usage and computational expenses. To address these limitations and enable scalable self-improvement for agents, we propose WebSynthesis, a novel framework for trajectory synthesis and training. WebSynthesis leverages a learned world model to simulate virtual web environments, allowing a policy agent to perform efficient and reversible tree-based planning. This approach supports the large-scale generation of diverse and high-quality trajectories, which are subsequently utilized to refine the agent's policy. Experimental results demonstrate that an agent trained using WebSynthesis on a small-scale synthetic dataset achieves performance comparable to or even surpassing that of models trained on large-scale real-world data.

## 내 메모


