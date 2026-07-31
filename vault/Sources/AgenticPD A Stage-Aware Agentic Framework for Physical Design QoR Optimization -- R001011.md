---
type: research-source
item_id: 1011
title: "AgenticPD: A Stage-Aware Agentic Framework for Physical Design QoR Optimization"
source: "arxiv"
published: "2026-07-06T07:55:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.04758"
url: "https://arxiv.org/abs/2607.04758v2"
generated_by: codex-research-db
aliases:
  - "AgenticPD: A Stage-Aware Agentic Framework for Physical Design QoR Optimization"
topics:
  - "self-evolving-harness"
---

# AgenticPD: A Stage-Aware Agentic Framework for Physical Design QoR Optimization

[원문 열기](https://arxiv.org/abs/2607.04758v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8PWVGIDP`)
- 발행일: 2026-07-06T07:55:34Z
- 저자: Shuo Ren, Zijin Cheng, Yaohui Han, Libo Shen, Leilei Jin, Wanting Tian, Rongliang Fu, Chao Wang, Bei Yu, Tsung-Yi Ho
- 식별자: `arxiv:2607.04758`

## 요약·초록

Physical design quality-of-results~(QoR) optimization is hard and expensive. Choices made at one stage can help or hurt later stages. Each evaluation requires a costly EDA run through the full flow. While existing methods still treat optimization as flat parameter tuning or a LLM-based script generation task, we present AgenticPD, a stage-aware agentic framework for physical design QoR optimization. Instead of re-running the full flow after every trial, AgenticPD is organized around the stage boundaries of the physical design flow, where a Judge Agent navigates the search and stage-specialized agents make local decisions within their own stage using stage-local tools. Additionally, the agent harness in AgenticPD provides structured observations, execution history, and agent context management. As a result, the system can branch from prior intermediate states and reuse checkpoints to continue the optimization procedure, and every candidate is evaluated at the post-route signoff. Across these baselines, AgenticPD achieves strong post-route timing while remaining competitive in power and area.

## 내 메모


