---
type: research-source
item_id: 1733
title: "ACEM: A Cost Estimation Model for Agentic Software Engineering"
source: "arxiv"
published: "2026-08-03T17:54:11Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02582"
url: "https://arxiv.org/abs/2608.02582v1"
generated_by: codex-research-db
aliases:
  - "ACEM: A Cost Estimation Model for Agentic Software Engineering"
topics:
  - "ai-agents"
---

# ACEM: A Cost Estimation Model for Agentic Software Engineering

[원문 열기](https://arxiv.org/abs/2608.02582v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`C9HB8J8P`)
- 발행일: 2026-08-03T17:54:11Z
- 저자: Mohammad El-Ramly
- 식별자: `arxiv:2608.02582`

## 요약·초록

Traditional software cost estimation models, such as COCOMO II, Function Points, and Story Points, assume that development effort is primarily driven by human labor in design, coding, and testing. Agentic software engineering, where autonomous AI agents perform substantial implementation work and humans focus on planning, specification, and validation, challenges this assumption. New cost dimensions arise: large language model (LLM) token consumption across agent actions, Human-in-the-Loop (HITL) oversight effort, and infrastructure costs for agent orchestration and tooling. These costs are nondeterministic: identical tasks may consume different tokens, follow divergent reasoning paths, and require varying human correction, phenomena absent in traditional development. A new framework is needed to bridge standard sizing metrics with this cost structure. This paper proposes ACEM (Agentic Cost Estimation Model), which decomposes total agentic development cost into three additive dimensions: LLM, HITL, and infrastructure cost. ACEM introduces three constructs for agentic dynamics: the Revision Factor (RF), modeling token overhead from output rejection and retries; the Context Factor (CF), capturing rising token consumption as context accumulates; and the HITL Intensity Score (HIS), a four-level oversight classification scheme. It further maps Use Case Points, Story Points, and Function Points to estimated token consumption, enabling organizations to reuse existing project-scoping data for agentic cost forecasting. ACEM is presented as a fully specified model structure and calibration methodology, with constants left symbolic pending empirical grounding. As an early-stage proposal, it invites the research community to calibrate, test, and extend the model through real project data.

## 내 메모


