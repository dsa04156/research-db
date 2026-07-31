---
type: research-source
item_id: 985
title: "Copy-on-Write Scoring: Application-Specific Agent Evaluations"
source: "arxiv"
published: "2026-07-15T19:59:33Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14336"
url: "https://arxiv.org/abs/2607.14336v1"
generated_by: codex-research-db
aliases:
  - "Copy-on-Write Scoring: Application-Specific Agent Evaluations"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Copy-on-Write Scoring: Application-Specific Agent Evaluations

[원문 열기](https://arxiv.org/abs/2607.14336v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W2XG92RI`)
- 발행일: 2026-07-15T19:59:33Z
- 저자: Joanna Roy, Sven Hoelzel
- 식별자: `arxiv:2607.14336`

## 요약·초록

Trustworthy deployment of LLM-based agents in software systems requires evaluating how they perform on application-specific workflows, with enough granularity to localize where they succeed and fail. Yet existing agent evaluation mechanisms are limited: benchmarks have low construct validity for application-specific workflows and environments, and replica evaluation environments are expensive and prone to drift. We propose Copy-on-Write (CoW) Scoring, a framework that evaluates agent operations directly within application environments using a PostgreSQL-level Copy-on-Write mechanism to isolate agent writes. CoW Scoring produces session- and operation-level scores that highlight where agents' database write operations succeed and fail in a given application environment, enabling inexpensive evaluation and iteration on agent harnesses and tool surfaces. We demonstrate the framework on Plane, an open-source project-management platform, where analysis surfaced specific issues in the tool surface, and corresponding fixes produced measurable improvements on affected models. Python library: https://github.com/trail-ml/agent-cow-python

## 내 메모


