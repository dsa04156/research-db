---
type: research-source
item_id: 1051
title: "HACO: Hedged Agent Computing for Reliable LLM Systems"
source: "openalex"
published: "2026-07-21"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19215"
url: "https://arxiv.org/abs/2607.19215"
generated_by: codex-research-db
aliases:
  - "HACO: Hedged Agent Computing for Reliable LLM Systems"
topics:
  - "ai-agents"
---

# HACO: Hedged Agent Computing for Reliable LLM Systems

[원문 열기](https://arxiv.org/abs/2607.19215)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`Q4SHCB77`)
- 발행일: 2026-07-21
- 저자: Enhan Li, Hongyang Du
- 식별자: `arxiv:2607.19215`

## 요약·초록

As large language model (LLM) agents move from isolated prompting to longhorizon workflows, failures increasingly arise at the role-to-instance binding boundary, where task-specific role requests must be assigned to concrete agent instances under current service, network, and query conditions. Existing agent system research has improved role specialization, workflow topology, memory, and tool use, but often assumes a fixed stable execution environment. This assumption limits deployed reliability, because the same role request can exhibit different latency, failure probability, and output quality across agent instances operating under different service regions and network conditions. We propose Hedged Agent Computing (HACO), a runtime control scheme that treats each role request as a reliability-constrained selection problem over candidate agent instances, each coupling a role type, an LLM, and a concrete execution environment. Different from routing, HACO adaptively selects a hedge set of candidates for each invocation. Its allocation rule combines optimistic ranking, which prioritizes candidates with high estimated quality, reliability, and informative uncertainty, with conservative reliability accumulation, which stops selection only after the hedge set reaches a target success probability. Through experience harvesting, HACO updates candidate and link profiles from all executed candidate traces, including quality, success, latency, and network statistics. Experiments on various benchmarks, together with runtime degradation studies, show that HACO improves robustness and output quality under changing deployment conditions, while using lower token and latency cost than exhaustive parallel execution.

## 내 메모


