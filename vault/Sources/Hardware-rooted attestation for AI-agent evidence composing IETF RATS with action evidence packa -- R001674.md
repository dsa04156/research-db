---
type: research-source
item_id: 1674
title: "Hardware-rooted attestation for AI-agent evidence: composing IETF RATS with action evidence packages"
source: "arxiv"
published: "2026-08-01T18:01:36Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00801"
url: "https://arxiv.org/abs/2608.00801v1"
generated_by: codex-research-db
aliases:
  - "Hardware-rooted attestation for AI-agent evidence: composing IETF RATS with action evidence packages"
topics:
  - "ai-agents"
---

# Hardware-rooted attestation for AI-agent evidence: composing IETF RATS with action evidence packages

[원문 열기](https://arxiv.org/abs/2608.00801v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RUHSBART`)
- 발행일: 2026-08-01T18:01:36Z
- 저자: Anton Sokolov
- 식별자: `arxiv:2608.00801`

## 요약·초록

An action evidence package (AEP) is a signed, append-only record of what an AI agent did, who or what authorised the action, and what the outcome was. It is a software-layer artefact: it tells a verifier the story of an action as the agent's own runtime reports it. This note argues that software attestation of this kind is necessary but not sufficient. When a verifier's question shifts from "what does the agent claim it did?" to "did the specific model version the operator claims to have deployed actually produce this output, on unmodified hardware?", the AEP alone cannot answer. The missing element is a hardware root of trust: an attestation that the measured boot and runtime state of the platform match an endorsed reference. The IETF Remote Attestation Procedures (RATS) architecture (RFC 9334) and Veraison, an open-source RATS Verifier implementation (Confidential Computing Consortium / Linux Foundation), supply exactly this. We propose a composite attestation: hardware Evidence appraised under RATS, bound to a software AEP. We map a small verifier vocabulary (Authorised / Unauthorised / Indeterminate / Attested / Contested / Expired) onto RATS appraisal outcomes, and demonstrate feasibility with a small executed experiment: on a software Trusted Platform Module (TPM; the swtpm emulator), an output-binding protocol folds the hash of an AEP outcome and a fresh appraiser nonce into an attestation-key-signed quote, with a model-artefact measurement carried in a platform register. A minimal RATS-Verifier stand-in resolves the three platform outcomes as designed -- Attested for a good, fresh quote; Contested when the model measurement is swapped; Expired when a stale quote is replayed -- and rejects a forged AEP outcome bound to a valid quote. The result is a feasibility demonstration on emulated hardware, not a hardware-rooted guarantee.

## 내 메모


