---
type: research-source
item_id: 1067
title: "Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales"
source: "arxiv"
published: "2026-07-28T07:16:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25364"
url: "https://arxiv.org/abs/2607.25364v2"
generated_by: codex-research-db
aliases:
  - "Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales"
topics:
  - "ai-agents"
---

# Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales

[원문 열기](https://arxiv.org/abs/2607.25364v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2M3ASI7W`)
- 발행일: 2026-07-28T07:16:12Z
- 저자: Genliang Zhu, Chu Wang
- 식별자: `arxiv:2607.25364`

## 요약·초록

Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. EBTE cannot widen baseline authority: conflicts deny, incomplete or uncertain claims review, and only matching claims remain eligible for governed execution. We formalize this composition under explicit mediation and trusted-fact assumptions and implement a versioned reference profile with minimized audit packets. Across 136 authored conformance scenarios, the full profile matches all specified dispositions, admits none of 96 designated hard contradictions, and passes 232 metamorphic checks. A draft-only reference integration forwards none of 48 authored hard cases under EBTE while preserving all 16 soft-review and 4 aligned draft paths. In a frozen 2026-07-12 exploratory 224-attempt hosted-model record, the historical generation/runner agreement counts are 71/96, 66/96, and 19/32; a zero-call revalidation of the preserved minimized claims under the current pipeline yields 70/96, 65/96, and 17/32. In an AgentDojo-derived semantic check, existing high-risk controls make all 12 attack proposals non-allow, while EBTE resolves the task--proposal contradictions as deny. Together, these studies establish profile conformance and demonstrate the feasibility of server-checked action claims within the evaluated settings.

## 내 메모


