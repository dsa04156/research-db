---
type: research-source
item_id: 2083
title: "ClawGym II: Exploring Black-Box RL on Agent Harness"
source: "arxiv"
published: "2026-08-17T16:53:03Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.16798"
url: "https://arxiv.org/abs/2608.16798v1"
generated_by: codex-research-db
aliases:
  - "ClawGym II: Exploring Black-Box RL on Agent Harness"
topics:
  - "self-evolving-harness"
---

# ClawGym II: Exploring Black-Box RL on Agent Harness

[원문 열기](https://arxiv.org/abs/2608.16798v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-17T16:53:03Z
- 저자: Huatong Song, Fei Bai, Ming Yang, Renyuan Li, Jia Deng, Jujie He, Zhange Zhang, Daixuan Cheng, Yan Xing, Qi Yun, Xuxing Chen, Danyang Li, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Mingjie Tang, Ji-Rong Wen
- 식별자: `arxiv:2608.16798`

## 요약·초록

Agent harnesses have substantially improved performance on long-horizon tasks by coordinating agent interactions with the environment. However, reinforcement learning through complex harnesses remains largely unexplored, as scaling such training to long-horizon agent tasks introduces fundamental challenges. In this work, we present a unified black-box RL framework for stable and scalable optimization of general agents through complex harnesses. Concretely, we first build a sandbox-based execution infrastructure that isolates task environments and harnesses within temporary sandboxes for large-scale concurrent rollouts. We then decouple policy optimization from opaque harness execution and place a serving proxy at the model boundary to capture model calls. To reconstruct multi-turn trajectories and improve training efficiency, we organize the captured calls into prefix trees and further adapt both critic-based PPO and critic-free GRPO to optimize over the recovered tree structure. Meanwhile, we maintain training-inference consistency throughout the optimization process. Finally, we introduce mix-harness training, allowing a single model to be jointly optimized by heterogeneous harnesses. With Qwen3-30A3B, black-box RL improves Pass@1 on ClawGym-Bench by 9.98 and 14.81 points through OpenClaw and Claude Code, respectively, while remaining stable over 200-400 optimization steps. Moreover, the framework yields consistent gains on more challenging tasks such as JobBench and OfficeQA. Overall, our framework enables effective, stable, and scalable optimization of general agents through black-box harnesses, supporting unified training across heterogeneous execution systems.

## 내 메모


