---
type: research-source
item_id: 1060
title: "OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation"
source: "arxiv"
published: "2026-07-28T12:43:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25656"
url: "https://arxiv.org/abs/2607.25656v1"
generated_by: codex-research-db
aliases:
  - "OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation"
topics:
  - "ai-agents"
---

# OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation

[원문 열기](https://arxiv.org/abs/2607.25656v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2BJG2SU7`)
- 발행일: 2026-07-28T12:43:34Z
- 저자: Zhenzhen Ren, Jiyan He, Xinpeng Zhang, Zhenxing Qian, Ke Han, Shuxin Zheng, GuoBiao Li, Xiaoqing Zhang
- 식별자: `arxiv:2607.25656`

## 요약·초록

Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. Moreover, the time and token costs of real execution grow rapidly with workflow scale, making systematic evaluation expensive. We present OrchBench, a simulation-based benchmark for evaluating multi-agent orchestration plans in isolation. Starting from real-world tasks, OrchBench constructs directed acyclic graphs (DAGs) that encode task dependencies, with controlled sizes and degrees of parallelism. Given a DAG, a per-agent context limit, and an agent budget, the evaluated planner assigns subtasks to agents and specifies cross-agent information transfers and their retention ratios. A deterministic simulator evaluates the resulting plan without invoking worker agents and returns interpretable measures of result quality, makespan, and token cost. The simulated scores produced by OrchBench correlate strongly with quality scores from Claude Code executions, achieving a Pearson correlation of \(r=0.816\), while requiring only \(1.3\%\) of the tokens and \(10.3\%\) of the wall-clock time. Across diverse planners and workflow scales, we find that preserving task-critical information is more important than simply increasing the number of agents, and the benefits of parallelism diminish as coordination failures accumulate. These results establish OrchBench as an efficient and interpretable benchmark for comparing and diagnosing multi-agent orchestration plans.

## 내 메모


