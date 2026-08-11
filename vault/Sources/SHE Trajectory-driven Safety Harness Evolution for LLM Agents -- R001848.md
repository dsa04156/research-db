---
type: research-source
item_id: 1848
title: "SHE: Trajectory-driven Safety Harness Evolution for LLM Agents"
source: "arxiv"
published: "2026-08-10T17:35:08Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.09885"
url: "https://arxiv.org/abs/2608.09885v1"
generated_by: codex-research-db
aliases:
  - "SHE: Trajectory-driven Safety Harness Evolution for LLM Agents"
topics:
  - "self-evolving-harness"
---

# SHE: Trajectory-driven Safety Harness Evolution for LLM Agents

[원문 열기](https://arxiv.org/abs/2608.09885v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-10T17:35:08Z
- 저자: Wanying Qu, Qinghua Mao, Yu Li, Jiyao Liu, Xin Zhang, Dadi Guo, Yanxu Zhu, Qingyu Liu, Leitao Yuan, Xi Lin, Shanfeng Zhu, Yanwei Fu, Jing Shao, Xia Hu, Dongrui Liu
- 식별자: `arxiv:2608.09885`

## 요약·초록

The safety of large language model (LLM) agents depends not only on model weights but also on the agent harness that manages context, memory, tools, permissions, and runtime control. Existing safety mechanisms often treat the harness as a fixed deployment artifact, limiting their ability to evolve with emerging risks. Moreover, coupled functions across harness components obscure safety responsibility attribution, making localized evolution difficult. We propose Safety Harness Evolution (SHE), a framework that learns evolving safe boundaries from rollout trajectories. SHE decomposes the harness into four artifacts with explicit safety responsibilities, including the System Prompt, Rule Bank, Safety Memory, and Tool Policy, defining clear functional boundaries for localized evolution. Based on this decomposition, SHE introduces an attribution-guided evolution loop that converts trajectory failures into structured diagnoses, learns artifact-specific boundary refinements, and selects evolved harnesses through safety-utility validation. Experiments on Agent-SafetyBench demonstrate that SHE effectively enhances safety through harness evolution, achieving a 3.1x ASR reduction compared with static SafeHarness, while also improving benign utility. The evolved harness further generalizes to unseen risks on the held-out AgentHarm benchmark and transfers across agent models without additional evolution.

## 내 메모


