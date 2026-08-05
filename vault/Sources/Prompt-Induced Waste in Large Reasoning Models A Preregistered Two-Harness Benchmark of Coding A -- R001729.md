---
type: research-source
item_id: 1729
title: "Prompt-Induced Waste in Large Reasoning Models: A Preregistered Two-Harness Benchmark of Coding Agents"
source: "arxiv"
published: "2026-08-02T16:10:02Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01347"
url: "https://arxiv.org/abs/2608.01347v1"
generated_by: codex-research-db
aliases:
  - "Prompt-Induced Waste in Large Reasoning Models: A Preregistered Two-Harness Benchmark of Coding Agents"
topics:
  - "self-evolving-harness"
---

# Prompt-Induced Waste in Large Reasoning Models: A Preregistered Two-Harness Benchmark of Coding Agents

[원문 열기](https://arxiv.org/abs/2608.01347v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HDT59C7R`)
- 발행일: 2026-08-02T16:10:02Z
- 저자: Sarel Weinberger, Amir Hozez
- 식별자: `arxiv:2608.01347`

## 요약·초록

Large reasoning models used as coding agents incur costs from deliberation, tool calls, and repeated agent turns, yet the causal effect of prompt wording on this spend has not been measured systematically. We present a preregistered benchmark across six large reasoning models, two real agent harnesses, and 24 deterministic coding tasks with hidden evaluators. Across 4,643 valid runs, including screening, stress, holdout, replication, and cross-provider studies, we find that prompt formulation can multiply reasoning cost without improving correctness. Asking the model to develop and compare several approaches is the most consistently wasteful instruction, increasing reasoning tokens by 2.4-7.4x across all models. Generic "think deeply" cues also increase deliberation by 1.6-2.2x, while a bounded-efficiency template specifying scope, acceptance criteria, and a stop condition is cost-neutral and can halve reasoning. Harness choice matters even more: identical model-task-prompt triples cost 5-30x more per success under Claude Code than under pi, mainly because of larger static prefixes and more turns. Misleading architectural hints are far costlier than irrelevant prose, and provider-side caching reduces billed cost without changing behavior, so it must not be treated as efficiency. Replications on Kimi-K3 and Claude Sonnet 5 preserve the main effect directions while revealing model-specific sensitivity to thinking and certainty cues. Overall, prompt wording and harness design materially affect agent cost, often with no gain in task success.

## 내 메모


