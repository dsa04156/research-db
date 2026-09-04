---
type: research-source
item_id: 2559
title: "LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails"
source: "arxiv"
published: "2026-09-02T07:54:23Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02246"
url: "https://arxiv.org/abs/2609.02246v1"
generated_by: codex-research-db
aliases:
  - "LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails"
topics:
  - "self-evolving-harness"
---

# LLM-as-a-Judge Is Not an Oracle: Why Self-Improving Agents Need Deterministic Guardrails

[원문 열기](https://arxiv.org/abs/2609.02246v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T07:54:23Z
- 저자: Vansh Wahi
- 식별자: `arxiv:2609.02246`

## 요약·초록

Self-improving agent pipelines have a problem at their center. An optimizer rewrites prompts to score higher, and the score comes from a judge that is itself an LLM. That judge has the last word on whether the system is getting better, and our position is that it has not earned it. The judge should be demoted from oracle to advisor: its verdict becomes one input among several, and every change is gated instead by a deterministic verification layer the judge cannot override. We reached this position by building the alternative and running it. Over months of running autonomous prompt-optimization loops in production across contract analysis, compliance review, and code quality, we cataloged eleven ways the evaluation signal failed, in four classes: judge bias, harness and metric failures, ground-truth errors, and reward hacking. Agents achieved perfect scores by reading cached answer keys from their environment, a 100% pass rate concealing 68% true capability. A corrupted ground-truth label caused the optimizer to delete correct compliance rules to agree with it. A syntactically broken prompt was promoted as the winner because a silent parser fallback improved the metric. Attempts to fix the judge by rewriting its rubric plateaued; the only reliable gain came from a structural constraint on its output order. In response we describe PROCTOR, a Teacher-Student loop in which a stateful orchestrator holds all tool access, stateless subagents diagnose failures and draft mutations they cannot apply, and a Teacher grades those mutations under five deterministic guardrails: hermetic sandboxes, capability-disjoint roles, acceptance checks that outrank the Teacher, frozen holdouts, and canary cases engineered so that a perfect score is itself evidence of cheating. We report the failures this prevented, and, because the Teacher is itself an LLM judge, the failures it did not.

## 내 메모


