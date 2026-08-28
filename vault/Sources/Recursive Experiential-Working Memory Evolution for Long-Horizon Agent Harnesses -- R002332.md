---
type: research-source
item_id: 2332
title: "Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses"
source: "arxiv"
published: "2026-08-25T17:56:35Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.24876"
url: "https://arxiv.org/abs/2608.24876v1"
generated_by: codex-research-db
aliases:
  - "Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses

[원문 열기](https://arxiv.org/abs/2608.24876v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`I7DHR6UU`)
- 발행일: 2026-08-25T17:56:35Z
- 저자: Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, Shuicheng Yan, Ling Yang
- 식별자: `arxiv:2608.24876`

## 요약·초록

Recursive self-improvement (RSI) remains hard in long-horizon tasks, where growing histories obscure the task state and misalign skill invocation. We introduce Recuris, a recursive Experiential-Working Memory architecture for long-horizon agent harnesses, in which Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather than the full history. This coupling also turns execution into structured evidence that localizes failures to specific memory components. Across tasks, a fixed Meta-Agent turns that evidence into localized, validation-gated updates to Skill Memory that reshape execution and yield new evidence, forming a bounded recursive memory-evolution loop. Across four long-horizon benchmarks and ten models, Recuris improves task success in 35 of the 37 completed model-benchmark pairs, carrying frontier models to SOTA-level task success: on tau-bench it adds +17.8 points to GPT-5.6 Sol and +15.6 to Claude Opus 5, taking Opus 5 to 87.9%, and +16.6/+13.5 points on Qwen3.6-27B/35B on SkillFlow. The advantage widens as the interaction horizon grows, to +32.2 points on the longest tasks, and common long-horizon failures fall by up to 80%. These results position recursively evolving memory as a scalable foundation for RSI, enabling agents to continuously transform accumulated experience into increasingly effective long-horizon behavior. Code: https://github.com/Gen-Verse/Recuris

## 내 메모


