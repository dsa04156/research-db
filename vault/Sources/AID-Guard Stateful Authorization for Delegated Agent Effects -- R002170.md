---
type: research-source
item_id: 2170
title: "AID-Guard: Stateful Authorization for Delegated Agent Effects"
source: "arxiv"
published: "2026-08-21T14:31:29Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.21159"
url: "https://arxiv.org/abs/2608.21159v1"
generated_by: codex-research-db
aliases:
  - "AID-Guard: Stateful Authorization for Delegated Agent Effects"
topics:
  - "ai-agents"
---

# AID-Guard: Stateful Authorization for Delegated Agent Effects

[원문 열기](https://arxiv.org/abs/2608.21159v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EGM4J5ZP`)
- 발행일: 2026-08-21T14:31:29Z
- 저자: Yingzhe Tong, Leyu Dai, Songhui Guo
- 식별자: `arxiv:2608.21159`

## 요약·초록

Tool-using AI agents turn delegated tasks into provider effects, yet authorization often ends at admission while provider state, delivery, retry, and recovery evolve. A request may change before commit, or response loss may cause a replacement to create a second effect from one approval. We present AID-Guard, a stateful authorization-to-effect closure protocol. It revalidates the approved request and provider state at commit, retains one reservation under ambiguity, and permits release or one successor only after a terminal result or certified no effect with a delivery fence. For supported provider contracts, one reservation yields at most one effect across retry and recovery. To our knowledge, it is the first evaluated agent-authorization protocol to unify these controls in one lifecycle. We implement a Python/SQLite prototype. In a declared loopback MCP domain, 13 live mutations caused no unauthorized provider effects, three concurrent histories were linearizable, and evidence bundles supported public verification and replay. All 210 Stripe provider-contract trials matched predeclared outcomes. Across Stripe and Resend, 40 terminalize-successor schedules, 30 overlapping races, and 10 crash-recovery schedules completed without duplicate effects. Under complete proposer compromise, AID-Guard blocked 44/44 attacks and admitted 44/44 matched legitimate proposals. Its strict exact-manifest profile reduced benign utility by 35.4 to 43.8 percentage points; a typed frontier recovered 9-10 completions without observed unsafe effects. A composition study blocked 20/20 post-admission lifecycle attacks and preserved 8/8 valid or exact-retry executions. The results support authorization-to-effect binding under the evaluated effect-path inventory, provider contracts, and failure schedules.

## 내 메모


