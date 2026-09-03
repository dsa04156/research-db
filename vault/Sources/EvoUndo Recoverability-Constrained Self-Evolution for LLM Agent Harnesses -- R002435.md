---
type: research-source
item_id: 2435
title: "EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses"
source: "arxiv"
published: "2026-08-28T14:15:36Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.28363"
url: "https://arxiv.org/abs/2608.28363v1"
generated_by: codex-research-db
aliases:
  - "EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses"
topics:
  - "self-evolving-harness"
---

# EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent Harnesses

[원문 열기](https://arxiv.org/abs/2608.28363v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`INHEN3TQ`)
- 발행일: 2026-08-28T14:15:36Z
- 저자: Tanmay Sah, Dolly Sah, Harshul Jain, Tanya Sah
- 식별자: `arxiv:2608.28363`

## 요약·초록

LLM agents increasingly modify their own prompts, tools, middleware, resources, and execution harnesses at runtime. Such self-evolution can improve capability, but a successful mutation may leave persistent effects that cannot be safely reversed in states different from the one in which it was created. We introduce EvoUndo, a framework for representing, synthesizing, diagnosing, and independently verifying recoverability of model-generated self-modifications across counterfactual states. Across 600 unseen one-shot self-evolution tasks, we identify 197 capability-improving mutations that fail recoverability verification. Under the original recovery representation, conventional repair strategies recover 0/197 of these natural failures. Deterministic oracle analysis recovers 48/197 under the original recovery language L0, while the extended recovery calculus increases empirical oracle recovery to 191/197. A protocol-locked 2x2 grounding-by-expressivity intervention then separates two bottlenecks: exact state-address grounding increases successful recovery from 0/48 to 38/48 (79.2%) when the original language is sufficient, while extending the recovery language enables recovery on 142/143 (99.3%) failures in the oracle-defined S1 stratum. On the primary gpt-oss-120b backbone, adding exact-address diagnostics to the richer language reduces recovery to 133/143 (93.0%); a Qwen3.8-27B replication preserves the grounding and expressivity effects but not this negative interaction, indicating that the latter is model-dependent. These results indicate that reliable agent self-evolution requires co-designing verification, state grounding, witness semantics, and recovery-language expressivity rather than relying on iterative prompting alone.

## 내 메모


