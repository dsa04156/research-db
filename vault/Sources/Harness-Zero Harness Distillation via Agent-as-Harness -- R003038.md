---
type: research-source
item_id: 3038
title: "Harness-Zero: Harness Distillation via Agent-as-Harness"
source: "arxiv"
published: "2026-09-21T17:55:20Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24974"
url: "https://arxiv.org/abs/2609.24974v1"
generated_by: codex-research-db
aliases:
  - "Harness-Zero: Harness Distillation via Agent-as-Harness"
topics:
  - "self-evolving-harness"
---

# Harness-Zero: Harness Distillation via Agent-as-Harness

[원문 열기](https://arxiv.org/abs/2609.24974v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T17:55:20Z
- 저자: Haoran Ye, Yuxing Lu, Haonan Dong, Zhaochen Su, Guojie Song
- 식별자: `arxiv:2609.24974`

## 요약·초록

Agent harnesses, the external systems that mediate model-environment interaction, can substantially improve agent performance, but their gains remain tied to the harness at deployment. Because the best harness varies across domains, instances, and models, a general-purpose agent must either settle for a suboptimal shared harness or route among an ever-growing set of specialized ones. We therefore study agent harness distillation: using a domain- or instance-optimized harness as training-time guidance and transferring the behaviors it induces into model weights, so that its gains survive under a single fixed target harness. The challenge is that the two harnesses differ in action space and available information, so guidance from the optimized harness cannot serve directly as supervision for the target one. We introduce Harness-Zero, which enables harness distillation through agent-as-harness. Guided by the optimized harness, a harnessing agent corrects student responses before execution in the target harness's action space, turning harness guidance into training demonstrations. Fine-tuning on the resulting trajectories internalizes harness-induced behavior into the model, so the specialized harness can be removed at deployment. Our experiments spanning knowledge work, tool use, and science domains show that: (1) For frontier LLMs using the same evolved harness, agent-as-harness outperforms code-as-harness. (2) With the specialized harness removed at deployment, Harness-Zero improves the base model's macro-average task success from 23.3% to 44.3%, even exceeding the 41.7% it reaches with that harness still attached. (3) Harness-Zero recovers harness-induced behaviors absent from the base model, with 82.3% average recovery across 28 patterns in the three domains.

## 내 메모
