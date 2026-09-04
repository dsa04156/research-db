---
type: research-source
item_id: 2581
title: "Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents"
source: "arxiv"
published: "2026-09-02T05:35:33Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02127"
url: "https://arxiv.org/abs/2609.02127v1"
generated_by: codex-research-db
aliases:
  - "Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents"
topics:
  - "ai-agents"
---

# Stored Is Not Supported: Typed Provenance and Assertion Guardrails for Persistent AI Agents

[원문 열기](https://arxiv.org/abs/2609.02127v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T05:35:33Z
- 저자: Jun He, Deying Yu
- 식별자: `arxiv:2609.02127`

## 요약·초록

Persistent AI agents construct autobiographical state through reflection, retrieval, and consolidation. Persistence changes availability, not epistemic standing: stored or retrieved material is not thereby supported. Untrusted inputs, prompt injections, and model inferences can therefore enter persistent state and later be presented as agent history or user commitments. We specify typed provenance and assertion guardrails for autobiographical assertion boundedness, a system-relative release property requiring governed statements about the agent, user, or named relationships to satisfy accepted-evidence, temporal-validity, and disclosure policies. A typed provenance graph separates origin, dependency lineage, epistemic role, validity, and disclosure scope. A resolver evaluates authorized state projections and returns one evidential status, orthogonal conflict, staleness, and withholding flags, and a protected decision witness. A generate-verify-revise mediator then checks candidate semantic units before release and renders policy-authorized status responses. Under explicit assumptions about extraction, predicate correctness, resolution soundness, view declassification, and channel mediation, we prove a conditional assertion-boundedness contract. In an executable suite of 24 hand-authored conformance cases, typed mediation passed none of 19 unsafe opportunities unqualified while preserving all five supported controls. The flat/prior and source-tag comparison rules released 19/19 and 18/19 unsafe candidates, respectively. These results validate the encoded resolver and mediator obligations; they do not constitute an end-to-end evaluation of language models or retrieval systems.

## 내 메모


