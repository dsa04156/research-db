---
type: research-source
item_id: 3057
title: "AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation"
source: "arxiv"
published: "2026-09-20T11:55:26Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.23578"
url: "https://arxiv.org/abs/2609.23578v1"
generated_by: codex-research-db
aliases:
  - "AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation"
topics:
  - "ai-agents"
---

# AR-WAM: A Visual-Conditioned Agent-Ready World Action Model for Robotic Manipulation

[원문 열기](https://arxiv.org/abs/2609.23578v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-20T11:55:26Z
- 저자: Yicheng Jiang, Zesen Gan, Xiaobo Wang, Tianlun He, Chenxu Zhao, Minghui Wu, Xinyue Wang, Jiaxu Wang, Junhao He, Jianan Wang, Qiming Shao
- 식별자: `arxiv:2609.23578`

## 요약·초록

As AI agents become increasingly capable, agent-driven robotic control is emerging as a compelling paradigm. However, prevailing vision-language-action (VLA) models and world action models (WAMs) still rely on natural-language instructions to specify manipulation tasks, an ill-suited interface for agent-driven control: referentially ambiguous, spatially imprecise, redundant with the agent's inherent language understanding, and entangling intent with execution. We present AR-WAM, a visual-conditioned, agent-ready world action model that replaces language with two complementary conditions: a visual grounding prompt (a bounding box of the target) denoting the interaction object and location, and a learnable operation token dictating the atomic skill to execute. Our compact 0.5B-parameter model, with a frozen pretrained visual encoder and no language encoder, predicts scene evolution within compact latent states while decoding actions, exposing the policy's intent through explicit, supervisable reasoning signals. A model-agnostic compatibility layer provides three primitives (detect, execute, and query) so that local VLMs or online agent APIs can drive the policy directly, with long-horizon memory and closed-loop error recovery delegated to the agent side. On RoboTwin 2.0, RMBench, and a real Astribot S1 dual-arm platform, AR-WAM matches the strongest baselines on standard manipulation (87.2% average success) and outperforms them on memory-dependent and real-robot long-horizon tasks, improving success rates by 5.9% and 36.7%, respectively, while maintaining the lowest inference latency (14.1 ms).

## 내 메모
