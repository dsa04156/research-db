---
type: research-source
item_id: 1686
title: "CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents"
source: "arxiv"
published: "2026-07-31T09:11:56Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2607.29190"
url: "https://arxiv.org/abs/2607.29190v1"
generated_by: codex-research-db
aliases:
  - "CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents"
topics:
  - "ai-agents"
---

# CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

[원문 열기](https://arxiv.org/abs/2607.29190v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZXUHCKWH`)
- 발행일: 2026-07-31T09:11:56Z
- 저자: Blaise Delattre, Cong Wang, Yang Cao
- 식별자: `arxiv:2607.29190`

## 요약·초록

Tool-using LLM agents act on typed tool returns, records pairing provenance and categorical fields with numerical values. Runtime permission gates generally authorize the observed return and action, leaving the decision unprotected against small errors in how the return was bound to its source. We ask whether a candidate action stays authorized over a declared neighborhood of plausible correctly bound returns: one admissible binding fault plus bounded numerical drift. We prove that certifying the categorical and numerical channels separately does not compose: perturbations that are safe on each channel alone can jointly turn the same action unsafe. CAGE certifies this joint neighborhood directly, enumerating the discrete branches exactly and certifying the continuous perturbation within each branch. Across synthetic, policy-as-code, regulatory, and real-transaction settings, CAGE removes the in-budget false allows that accurate pointwise gates admit, while keeping a useful fraction of decisions autonomous. When the policy is executable, CAGE-Exact certifies the policy itself; otherwise CAGE-Lip and CAGE-RS certify a learned gate under an explicit, measured fidelity assumption.

## 내 메모


