---
type: research-source
item_id: 2358
title: "Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems"
source: "arxiv"
published: "2026-08-25T10:18:19Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.24361"
url: "https://arxiv.org/abs/2608.24361v1"
generated_by: codex-research-db
aliases:
  - "Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Adaptive Influence Graphs for Failure Attribution in Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2608.24361v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`CMD4MNIZ`)
- 발행일: 2026-08-25T10:18:19Z
- 저자: Yarden Bakish, Amir Dudai, Roy Ganz, Oren Nuriel, Elad Ben Avraham, Mor Shpigel Nacson, Ron Litman
- 식별자: `arxiv:2608.24361`

## 요약·초록

Multi-agent LLM systems are increasingly deployed in real-world applications, where failures can be costly and difficult to localize. Despite growing efforts to automate failure attribution, diagnosing failed runs still largely relies on human engineers. Yet engineers rarely debug complex systems by reading raw logs end to end. Instead, observability tools organize traces around components, actions, and dependencies to support targeted navigation. We hypothesize that modern LLMs can benefit from the same paradigm. To test this hypothesis, we introduce Adaptive Influence Graphs (AIGs), a two-stage agentic framework that first transforms a failed trace into a structured graph and then navigates it to identify the critical error. Across multiple models, we show that richer trace representations consistently improve failure attribution, with adaptive graph construction and agent-directed traversal yielding the strongest results. AIGs establish a new state of the art on Who&When, the standard benchmark for multi-agent failure attribution. This affirms our hypothesis that attribution depends not only on the diagnosing model, but also on how the trace is represented and explored.

## 내 메모


