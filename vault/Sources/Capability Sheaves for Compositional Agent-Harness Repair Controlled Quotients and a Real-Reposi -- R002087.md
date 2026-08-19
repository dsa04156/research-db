---
type: research-source
item_id: 2087
title: "Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test"
source: "arxiv"
published: "2026-08-13T13:31:09Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.13228"
url: "https://arxiv.org/abs/2608.13228v1"
generated_by: codex-research-db
aliases:
  - "Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test"
topics:
  - "self-evolving-harness"
---

# Capability Sheaves for Compositional Agent-Harness Repair: Controlled Quotients and a Real-Repository Stress Test

[원문 열기](https://arxiv.org/abs/2608.13228v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-13T13:31:09Z
- 저자: Saveliy Batruin
- 식별자: `arxiv:2608.13228`

## 요약·초록

Agent harnesses combine retrieval, routing, state, provenance, and verification, but locally successful components may disagree on shared state. We model this failure with a finite \emph{capability sheaf}: stalks encode typed behavior signatures, restriction maps retain shared fields, and accepted runs are useful global sections. An exact finite constraint-satisfaction problem (CSP) defines acceptance, while a linearized relative cohomology class provides a diagnostic and search feature. A controlled experiment over 20 task clusters introduces hidden interior mediators whose raw states are nuisance variables. Quotienting their coboundaries reduces the candidate budget from 2,000 to 1,000 per cluster; aligning the hidden state removes the gap. Exact CSP matches the quotient, so the result demonstrates invariance to stale representatives, not superiority over exact reasoning. We then test the method on a discovery split from the SWE-bench Multilingual pool of PatchFuseBench: 160 issues from 20 repositories, 875 real candidate patches, 2,579 source-aware edit atoms, and 153 newly executed patches. A first pool-level construction is constant because $[b-Dx]=[b]$ in $\operatorname{coker}D$ and therefore cannot rank configurations. A candidate-indexed repair is nontrivial on 848/875 candidates and varies within 120/160 issues. It resolves 118 issues versus 116 for a matched noncohomological selector, but the difference is not supported across repositories (exact sign-flip $p=0.75$). A leave-one-repository-out abstention gate reaches 127/160, tying the strong anchor and exceeding its matched gate by one issue ($p=1.0$). The discovery gate therefore fails and the confirmatory split remains sealed. The study supports the controlled invariance mechanism and an identifiability correction, but not a real-world cohomological advantage.

## 내 메모


