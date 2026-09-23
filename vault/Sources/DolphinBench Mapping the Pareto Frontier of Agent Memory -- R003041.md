---
type: research-source
item_id: 3041
title: "DolphinBench: Mapping the Pareto Frontier of Agent Memory"
source: "arxiv"
published: "2026-09-21T17:54:35Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24971"
url: "https://arxiv.org/abs/2609.24971v1"
generated_by: codex-research-db
aliases:
  - "DolphinBench: Mapping the Pareto Frontier of Agent Memory"
topics:
  - "ai-agents"
---

# DolphinBench: Mapping the Pareto Frontier of Agent Memory

[원문 열기](https://arxiv.org/abs/2609.24971v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T17:54:35Z
- 저자: Soumil Rathi, Deshraj Yadav, Taranjeet Singh
- 식별자: `arxiv:2609.24971`

## 요약·초록

Agents today often take real-world actions that depend on long-term memory and context recall over time. However, most current memory benchmarks are built for a conversational question-answer format, where the question itself signals that some fact must be retrieved, and often which one. Moreover, benchmarks rarely require anything beyond accuracy from submissions, allowing memory systems to make unreasonable cost/time tradeoffs to achieve higher scores. We present DolphinBench, a benchmark that evaluates memory directly through an agent's task completion. DolphinBench includes three knowledge-work personas with roughly 500k tokens of user messages per persona and evaluates agents on tasks that depend on information from that history. We verify all 200 tasks per persona by running an agent with and without the relevant history, requiring success with it and failure without it. Finally, we require all evaluations to report total cost and latency alongside accuracy, which enables us to evaluate agent memory systems holistically. No existing memory benchmark combines all three. The dataset and evaluation code are available at https://dolphinbench.ai.

## 내 메모
