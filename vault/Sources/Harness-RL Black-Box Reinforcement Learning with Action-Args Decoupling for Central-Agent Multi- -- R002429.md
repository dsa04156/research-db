---
type: research-source
item_id: 2429
title: "Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses"
source: "arxiv"
published: "2026-08-30T08:07:17Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.29641"
url: "https://arxiv.org/abs/2608.29641v1"
generated_by: codex-research-db
aliases:
  - "Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Central-Agent Multi-Agent Harnesses

[원문 열기](https://arxiv.org/abs/2608.29641v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2QJHX2U9`)
- 발행일: 2026-08-30T08:07:17Z
- 저자: Xinke Jiang, Zhixin Zhang, Zhibang Yang, Jiaran Gao, Rihong Qiu, Shijin Chen, Xu Chu, Junfeng Zhao, Yasha Wang
- 식별자: `arxiv:2608.29641`

## 요약·초록

Large language model agents increasingly solve long-horizon tasks through multi-agent harnesses in which a central agent coordinates specialized sub-agents, tools, and environments. Training the central policy in such a harness raises two challenges. First, an action label is a low-cardinality decision, whereas its args form a high-dimensional conditional sequence; optimizing both with a shared sequence-level signal can produce conflicting gradients. Second, dynamic scheduling creates interdependent sessions with branches, parallel calls, and rewritten contexts, which cannot be faithfully reduced to one flat token sequence. We introduce Harness-RL, a structured reinforcement learning framework that combines Conflict-Aware Policy Optimization (CAPO) with interface-level black-box trajectory construction. The black-box component captures Interface Call Records, builds per-session prefix trees, and aligns outcome and process rewards with trainable tokens. CAPO uses forward activations to identify parameter partitions associated with action and args tokens, then routes their policy gradients to the corresponding subspaces. Harness-RL supports both central-only and joint multi-agent training. Across seven multi-hop question answering and agentic retrieval benchmarks, it reaches average F1 scores of 42.93 and 47.79 with Qwen2.5-1.5B and Qwen2.5-3B, respectively, while ablations validate the contribution of CAPO and favor central-only optimization in the evaluated setting. Our code is available at https://github.com/jiangxinke/Harness-RL.

## 내 메모


