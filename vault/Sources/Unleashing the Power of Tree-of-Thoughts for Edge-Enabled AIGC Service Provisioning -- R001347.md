---
type: research-source
item_id: 1347
title: "Unleashing the Power of Tree-of-Thoughts for Edge-Enabled AIGC Service Provisioning"
source: "arxiv"
published: "2026-05-18T20:50:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.19108"
url: "https://arxiv.org/abs/2605.19108v1"
generated_by: codex-research-db
aliases:
  - "Unleashing the Power of Tree-of-Thoughts for Edge-Enabled AIGC Service Provisioning"
topics:
  - "edge-computing"
---

# Unleashing the Power of Tree-of-Thoughts for Edge-Enabled AIGC Service Provisioning

[원문 열기](https://arxiv.org/abs/2605.19108v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JPZBRG73`)
- 발행일: 2026-05-18T20:50:47Z
- 저자: Zhang Liu, Shanhao Zhan, Shaowei Shen, Lianfen Huang, Qiao Xiang, Ying-Jun Angela Zhang, Dusit Niyato
- 식별자: `arxiv:2605.19108`

## 요약·초록

Delivering AI-generated content (AIGC) services fundamentally relies on the reasoning capabilities of generative AI (GenAI) models. Chain-of-Thought (CoT) enhances such reasoning by guiding models through intermediate steps, while Tree-of-Thoughts (ToT) further extends CoT by exploring multiple candidate reasoning paths simultaneously, thereby greatly improving AIGC service quality. However, generating diverse reasoning paths requires separate calls to computationally intensive GenAI models, posing significant challenges for resource constrained user devices. In this paper, we investigate mobile edge computing-enabled AIGC service provisioning with ToT prompting. Specifically, using creative writing AIGC tasks as a case study, we first characterize the number of output tokens as a measure of computational resources in GenAI models and establish its relationship with generation delay and quality through experiments with Qwen 2.5-7B-Instruct. Afterward, we introduce a directed acyclic graph (DAG) model to accurately characterize the reasoning process of ToT prompting, where each vertex represents a thought and each directed edge denotes a transition between consecutive thoughts. We then formulate a DAG-based thought assignment problem aimed at minimizing generation delay subject to a user-adjustable quality constraint. To address this problem, we propose a diffusion-based soft actor-critic (DSAC) algorithm that innovatively integrates diffusion models to determine optimal thought assignment decisions. Through extensive simulations, we demonstrate that the proposed DSAC achieves total generation delay reductions of up to 8.32% over PPO, 11.57% over SAC, and 36.09% over DDQN across various simulation settings, while reducing latency by over 80% compared to the fully local generation baseline even under stringent quality requirements.

## 내 메모


