---
type: research-source
item_id: 2165
title: "LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents"
source: "arxiv"
published: "2026-08-18T05:34:35Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.17393"
url: "https://arxiv.org/abs/2608.17393v1"
generated_by: codex-research-db
aliases:
  - "LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents"
topics:
  - "self-evolving-harness"
---

# LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents

[원문 열기](https://arxiv.org/abs/2608.17393v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FE2FCH39`)
- 발행일: 2026-08-18T05:34:35Z
- 저자: Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, Chaofan Tao, Xianzhi Yu, Lifeng Shang, Kam-Fai Wong, Xiaohui Li, Haoli Bai
- 식별자: `arxiv:2608.17393`

## 요약·초록

Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward hacking corrupt outcome signals, while train-inference discrepancies decouple rollout behavior from policy updates. To address this, we present LEGO-RL, a framework that bridges native coding-agent harnesses with scalable policy-gradient optimization without modifying their internal control flow. LEGO-RL is built upon three pillars: (1) faithful optimization via in-process LLM proxying that captures raw generation streams for token-level alignment and robust trainer-side log-probability recomputation, even under harness-side compaction or re-serialization; (2) reliable execution via scalable sandbox orchestration featuring image caching and stage-wise defenses to mitigate reward hacking; and (3) observable training through an integrated plugin that automates validation and monitoring, paired with a Live UI for granular trajectory diagnostics. We evaluate LEGO-RL by training the sparse MoE model Qwen3.5-35B-A3B with GSPO across three native coding-agent harnesses. LEGO-RL improves Qwen3.5-35B-A3B across OpenHands SDK (64.0% to 70.4%), Claude Code (62.4% to 68.2%), and OpenCode (57.2% to 66.6%) on SWE-bench Verified, while maintaining a rollout-training probability correlation above 0.99.

## 내 메모


