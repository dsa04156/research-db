---
type: research-source
item_id: 986
title: "AI Agents Do Not Fail Alone:The Context Fails First"
source: "arxiv"
published: "2026-07-15T18:33:02Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14275"
url: "https://arxiv.org/abs/2607.14275v1"
generated_by: codex-research-db
aliases:
  - "AI Agents Do Not Fail Alone:The Context Fails First"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# AI Agents Do Not Fail Alone:The Context Fails First

[원문 열기](https://arxiv.org/abs/2607.14275v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`I2RT4VNJ`)
- 발행일: 2026-07-15T18:33:02Z
- 저자: Fouad Bousetouane
- 식별자: `arxiv:2607.14275`

## 요약·초록

Context engineering has become central to building reliable AI agents, yet it remains largely unmeasured. Agents do not fail in isolation: their behavior is shaped by the instructions, tools, memory, retrieved knowledge, guardrails, and untrusted inputs accumulated in their context. When this context is weak, agents drift, hallucinate, misuse tools, ignore constraints, become vulnerable to injection, and waste tokens. This paper validates context-engineering quality as an independent leading indicator of agent reliability. We implement the measurement in ProofAgent-Harness, an open-source infrastructure for AI agent evaluation that uses multi-juror, consensus-based scoring. The harness assesses context across seven criteria: role clarity, guardrail coverage, instruction consistency, tool schema quality, grounding sufficiency, injection hardening, and token efficiency. Crucially, the context score is isolated from behavioral metrics and release decisions, enabling a non-circular validation. Through a controlled context-quality study across regulated agent domains, holding frontier LLM agents fixed and varying only their operating context, we show that context-quality criteria consistently predict their corresponding behavioral outcomes. Grounding sufficiency predicts hallucination resistance, guardrail coverage predicts manipulation resistance, instruction consistency predicts instruction following, and tool-schema quality predicts tool use. These findings establish context measurement as a validated preflight signal for agent reliability and position context engineering as an auditable layer of agent evaluation and governance.

## 내 메모


