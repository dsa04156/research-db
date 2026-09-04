---
type: research-source
item_id: 2561
title: "CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?"
source: "arxiv"
published: "2026-09-01T17:59:13Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.01600"
url: "https://arxiv.org/abs/2609.01600v1"
generated_by: codex-research-db
aliases:
  - "CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?"
topics:
  - "self-evolving-harness"
---

# CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?

[원문 열기](https://arxiv.org/abs/2609.01600v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-01T17:59:13Z
- 저자: Damien Sileo, Dimitri Kachler
- 식별자: `arxiv:2609.01600`

## 요약·초록

Dynamic agent harnesses let language models change the software that shapes their own execution. This flexibility brings a new reasoning burden: a local plugin change can propagate through dependencies and cleanup. We introduce CordisBench, a 1,200-question benchmark of this lifecycle reasoning. It combines a controlled formal setting with programs executed against Cordis, a runtime that manages component dependencies and cleanup, and asks models to identify affected components, predict state after a specified teardown order, determine which conditions hold under all or some orders, and choose reconfigurations that succeed when executed. Across these tasks, we evaluate three efficiency-oriented models at low reasoning effort with 2, 4, 8, 16, 24, or 32 relevant interactions, using deterministic task-specific scoring. Models usually handle small systems well but grow less reliable as more interactions become relevant, especially when predicting final state and when reasoning across teardown orders. Additional inference effort recovers marked gains for some models. The cost is nontrivial: on our 16-interaction subset, GPT-5.6 Luna uses nearly 3,000 reasoning tokens per question at medium effort. For these controlled instances, that cost is avoidable: an independent finite reference semantics agrees with Cordis execution on every observation and action outcome used for scoring across all 528 executable questions.

## 내 메모


