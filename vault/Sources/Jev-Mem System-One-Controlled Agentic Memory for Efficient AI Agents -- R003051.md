---
type: research-source
item_id: 3051
title: "Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents"
source: "arxiv"
published: "2026-09-21T01:43:12Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.23986"
url: "https://arxiv.org/abs/2609.23986v1"
generated_by: codex-research-db
aliases:
  - "Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents"
topics:
  - "ai-agents"
---

# Jev-Mem: System-One-Controlled Agentic Memory for Efficient AI Agents

[원문 열기](https://arxiv.org/abs/2609.23986v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T01:43:12Z
- 저자: Dongming Jiang, Yi Li, Bingzhe Li
- 식별자: `arxiv:2609.23986`

## 요약·초록

Agentic memory is becoming essential for long-horizon AI agents, yet many existing systems rely on autoregressive LLMs to control how memories are organized, retrieved, and used, placing expensive generation on the critical path of memory operations. We introduce \textbf{\method}, a new agentic memory architecture inspired by System-One/System-Two cognition. System One captures fast, lightweight decision-making, whereas System Two performs slower, deliberative reasoning. Jev-Mem brings this division of labor to agentic memory through a dedicated System-One control plane, a structured multi-relational memory plane, and a System-Two reasoning plane. The System-One controller governs memory typing and relational organization during construction, and dynamically performs query routing, retrieval-budget allocation, graph traversal, candidate scoring, and adaptive stopping during retrieval. System Two is invoked only for complex reasoning and answer synthesis. This design improves both memory effectiveness and system efficiency: on LoCoMo Jev-Mem achieves an overall LLM-as-a-Judge score of 0.777, an 11.0\% relative improvement over the strongest baseline, while reducing memory construction time to 158\,s, a 6.6$\times$ speedup over the fastest competing memory system, and lowering average query latency to 0.93\,s, a 36.7\% reduction.

## 내 메모
