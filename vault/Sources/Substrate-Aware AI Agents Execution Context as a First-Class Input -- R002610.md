---
type: research-source
item_id: 2610
title: "Substrate-Aware AI Agents: Execution Context as a First-Class Input"
source: "arxiv"
published: "2026-09-04T14:57:17Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.05232"
url: "https://arxiv.org/abs/2609.05232v1"
generated_by: codex-research-db
aliases:
  - "Substrate-Aware AI Agents: Execution Context as a First-Class Input"
topics:
  - "ai-agents"
---

# Substrate-Aware AI Agents: Execution Context as a First-Class Input

[원문 열기](https://arxiv.org/abs/2609.05232v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-04T14:57:17Z
- 저자: Manu Agrawal
- 식별자: `arxiv:2609.05232`

## 요약·초록

Autonomous AI agents increasingly select actions in environments whose memory, execution-time, runtime, compute, and operational constraints determine what counts as a suitable plan. We call the absence of this execution context from an agent's planning state substrate blindness. We test this general proposition through numerical code generation, where selected implementation choices and operational consequences are directly observable. Three frontier model configurations--Anthropic Claude Opus 5, OpenAI GPT-5.6-Sol, and Google Gemini 3.7 Flash--generate code for a high-dimensional pairwise Euclidean-distance task either from the task alone or with a 128 MB RAM and 10.0 s wall-time contract. Contract disclosure reduced measured peak process memory in 13 of 14 executable index-aligned task-only versus contract-disclosed comparisons and reduced mean wall time in all three cohorts, making execution up to 3.1x faster. Across the audited corpus, disclosure produced structural code changes including bounded blocking, float32 retention, upper-triangle traversal, and in-place or memory-mapped buffers. At a tighter 96 MB contract, independently sampled contract-disclosed cohorts achieved correct-and-within-budget outcomes of 4/5 for Claude Opus 5, 5/5 for GPT-5.6-Sol, and 3/5 for Gemini 3.7 Flash, compared with task-only outcomes of 0/5, 1/5, and 0/5; cohort mean MaxRSS and wall time were 49-74% and 35-64% lower than their task-only references. These results establish a controlled proof of concept for substrate-aware agent planning: a minimal execution contract induces proactive structural adaptation in generated programs, shifting computation away from unconstrained allocations and substantially improving observed resource-time profiles before execution.

## 내 메모


