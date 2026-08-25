---
type: research-source
item_id: 2247
title: "Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep"
source: "arxiv"
published: "2026-08-24T15:40:15Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.23395"
url: "https://arxiv.org/abs/2608.23395v1"
generated_by: codex-research-db
aliases:
  - "Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep"
topics:
  - "ai-agents"
---

# Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep

[원문 열기](https://arxiv.org/abs/2608.23395v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-24T15:40:15Z
- 저자: Pedro Santos
- 식별자: `arxiv:2608.23395`

## 요약·초록

Recent LLM-agent systems make conflicting design bets: decompose work across many narrow agents, or use one strong tool-using agent. This pilot studies that choice on bounded cross-border VAT determination with reverse charge, where every case has an oracle label and each intermediate decision is independently scoreable. We hold the activity surface fixed (subtasks, tools, I/O schemas, validation checks, orchestrator, base model, and merge policy) and vary only the assignment of subtasks to workers across four orchestrated configurations, from one wide worker to five narrow ones, against S0, a tuned no-orchestrator single agent, with a deterministic rule engine as oracle. The program spans 4,400 runs: a 40-case, five-repeat main sweep, matched-token arms separating prompt-budget from agent-count effects, and three failure-injection arms, all judged against pre-registered falsification criteria. The two intermediate configurations lead on accuracy (0.830, against endpoints at 0.720 and 0.770) but miss the pre-stated bar against the fine endpoint, so the intermediate-optimum hypothesis remains unsupported at pilot scale. The single agent does not Pareto-dominate the orchestrated set. The matched-token criterion fires: the budget-matched single agent lands 6.5 points below the leader, but the interval includes zero, so any advantage is consistent with a prompt-budget explanation. Under injection, availability faults are absorbed at every granularity, with wide-scope restart over-recovering its baseline by +0.160, while one schema-conforming hallucinated record degrades every configuration and inverts the ordering, hitting fragmented configurations hardest. The contribution is a bounded, preregistered pilot heuristic for right-sizing decomposition (place one partition boundary at the dependency-layer midpoint), released with oracle, dataset, harness, raw traces, and analysis pipeline.

## 내 메모
