---
type: research-source
item_id: 1850
title: "TRACE: TRajectory Attribution for Automated Context Engineering"
source: "arxiv"
published: "2026-08-10T06:01:03Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.09153"
url: "https://arxiv.org/abs/2608.09153v1"
generated_by: codex-research-db
aliases:
  - "TRACE: TRajectory Attribution for Automated Context Engineering"
topics:
  - "self-evolving-harness"
  - "ai-agents"
---

# TRACE: TRajectory Attribution for Automated Context Engineering

[원문 열기](https://arxiv.org/abs/2608.09153v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-10T06:01:03Z
- 저자: Yikai Zhao, Pradeep Kumar Misra, Saurabh Pandey
- 식별자: `arxiv:2608.09153`

## 요약·초록

Production AI agents fail when their context sources -- system prompts, knowledge bases, tool descriptions, and procedural skills -- contain errors or gaps. Current maintenance relies on manual log review and ad-hoc debugging, creating a scalability bottleneck as interaction volume grows. We present TRACE (TRajectory Attribution for Automated Context Engineering), an automated feedback loop that mines historical agent trajectories to diagnose and remediate context failures. Our key insight is that trajectories are rich with implicit dissatisfaction signals -- user corrections, rephrasing, abandonment cues -- that reveal precisely where context sources failed, without explicit feedback collection. Unlike model fine-tuning, TRACE operates on the context layer, enabling rapid iteration without retraining. We make four contributions: (1) a trajectory mining framework that systematically extracts diagnostic information from historical agent executions; (2) multi-component causal attribution that extends textual gradients from monolithic prompt optimization to heterogeneous context sources (skills, knowledge bases, tools, prompts); (3) exploratory verification, where agents actively read context sources to distinguish content gaps requiring CREATE from stale content requiring UPDATE, achieving 96% operation accuracy; and (4) a reusable simulation methodology and verifiable benchmark addressing the absence of open datasets for context debugging, with a six-category fault taxonomy, ground truth annotations, and a cross-layer verification protocol. On 60 dissatisfaction traces spanning three complexity tiers (up to 16 execution nodes), TRACE achieves 72.7% root cause attribution and 82% end-to-end fix effectiveness, showing that over 80% of context-layer failures can be automatically diagnosed and remediated by mining historical trajectories, an overlooked resource in production systems.

## 내 메모


