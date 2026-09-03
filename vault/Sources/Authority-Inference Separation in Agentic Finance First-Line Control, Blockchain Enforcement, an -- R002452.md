---
type: research-source
item_id: 2452
title: "Authority-Inference Separation in Agentic Finance: First-Line Control, Blockchain Enforcement, and Replayable Assurance"
source: "arxiv"
published: "2026-08-31T09:53:18Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.30519"
url: "https://arxiv.org/abs/2608.30519v1"
generated_by: codex-research-db
aliases:
  - "Authority-Inference Separation in Agentic Finance: First-Line Control, Blockchain Enforcement, and Replayable Assurance"
topics:
  - "ai-agents"
---

# Authority-Inference Separation in Agentic Finance: First-Line Control, Blockchain Enforcement, and Replayable Assurance

[원문 열기](https://arxiv.org/abs/2608.30519v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6IGWCFF6`)
- 발행일: 2026-08-31T09:53:18Z
- 저자: Hui Gong, Michail Samawi, Francesca Medda
- 식별자: `arxiv:2608.30519`

## 요약·초록

AI agents can select tools, counterparties, and transaction parameters, yet inference should not itself confer authority to execute a financial action. This study develops and evaluates Authority-Inference Separation (AIS), an intent-centered architecture for bounded agentic finance. AIS treats a financial action intent as the control object: a machine-generated proposal can receive temporary executable authority only after an independent deterministic control plane validates registered agent identity, accountable ownership, mandate and risk-appetite lineage, policy version, state, approvals, and exact economic semantics. Blockchain can then enforce the operational representation of granted authority and record portable settlement evidence, while institutional legitimacy, service delivery, accounting classification, and human accountability remain off-chain obligations. Evaluation combines four-domain instantiation, official BIS and MAS cases, a 48-fixture executable prototype, and a public-ledger observability test. Across 36 synthetic authorization attacks, a direct-agent baseline accepted 36 attack effects, a prompt-policy baseline accepted 20, and AIS accepted none; all three accepted 8/8 admissible fixtures. AIS also rejected 4/4 token replays and 8/8 recipient or rail substitutions, withheld completion in 4/4 service-delivery failures, and populated all 13 defined evidence fields. A test of 1,700 recent Base transactions associated with public x402 facilitator addresses shows that public ledgers can evidence settlement and selected authorization parameters but cannot establish institutional mandate, legal accountability, service delivery, or accounting treatment. AIS and blockchain are therefore complementary: AIS decides whether a specific intent may act, while blockchain can make granted authority bounded, executable, and independently observable.

## 내 메모


