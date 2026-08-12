---
type: research-source
item_id: 1858
title: "FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows"
source: "openalex"
published: "2026-08-06"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.06144"
url: "https://arxiv.org/abs/2608.06144"
generated_by: codex-research-db
aliases:
  - "FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows"
topics:
  - "self-evolving-harness"
---

# FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows

[원문 열기](https://arxiv.org/abs/2608.06144)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`MBJ4J77T`)
- 발행일: 2026-08-06
- 저자: Bo Deng, Kang Zhou, Lifan Guo, Chongyang Tao, Xuanren Chen, Chenggang Xie, Renzhao Liang, Feng Chen, Chi Zhang
- 식별자: `arxiv:2608.06144`

## 요약·초록

Most agent benchmarks evaluate tasks independently and cannot measure whether experience from one task helps with later tasks. Existing self-evolution benchmarks do not jointly cover professional workflows, open-ended deliverables, and multi-aspect evaluation. We introduce FinEvo-Bench, a longitudinal benchmark with 120 real-case-grounded tasks, 20 business scenes across six financial domains. Institution-provided professional procedures define the required operations and constraints. Eligible institution-provided and publicly documented cases supply the task facts. Each scene contains six related but substantively distinct cases that share a professional procedure and a manually reviewed rubric for task quality and financial compliance. We compare four self-evolving agent scaffolds using the same Qwen3.7-Max backbone and three independently shuffled, globally interleaved task streams. Paired non-evolving controls estimate each scaffold's self-evolution gain from retained experience, while an independent Claude Code scoring agent backed by Claude Opus 4.6 evaluates all outputs. Letta achieves the highest evolved score (91.65) and fewest compliance issues (0.09 per task); Codex achieves the largest self-evolution gain (+19.37). Across scaffolds, the evolving condition raises scores by 9.33-19.37 points and reduces compliance issues by 0.12-0.44 per task. Paired score gains at within-scene ranks 4-6 exceed those at ranks 1-3 by 6.10-8.70 points. In Claude Code, skill-only evolution produces higher task quality and fewer compliance issues than memory-only and combined memory-skill evolution. Across all four scaffolds, rubric feedback also yields higher scores and fewer compliance issues than reference-answer feedback. FinEvo-Bench measures both professional performance and self-evolution ability: how effectively an agent turns prior experience into later improvement.

## 내 메모


