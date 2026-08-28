---
type: research-source
item_id: 2263
title: "The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate"
source: "arxiv"
published: "2026-08-23T00:47:00Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.22152"
url: "https://arxiv.org/abs/2608.22152v1"
generated_by: codex-research-db
aliases:
  - "The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate"
topics:
  - "ai-agents"
---

# The Collaboration Tax: How Much LLM Multi-Agent Systems Pay to Coordinate

[원문 열기](https://arxiv.org/abs/2608.22152v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JXV8WQRM`)
- 발행일: 2026-08-23T00:47:00Z
- 저자: Weixiang Sun, Zehong Wang, Hong Huang, Colby Nelson, Yanfang Ye
- 식별자: `arxiv:2608.22152`

## 요약·초록

Multi-agent systems built from large language models are deployed widely, yet how much performance is lost when two LLMs must coordinate rather than act alone remains unclear. We formulate the collaboration tax as the team-decentralisation loss of a two-player cooperative game with private information, with two propositions characterising its sign and its equivalence to a max-superadditivity violation. We operationalise this definition on 32 solo-tractable tasks grouped by source of grounding friction and measure it on 11 models from 7 providers. The tax is structured along two no-exception axes: a category ordering across every model and a monotonic decrease with capability. The proximate mechanism is not a reasoning deficit but a four-stage conversational cascade in which agents make ungrounded claims, fail to query the partner, skip integrating both views, and accept the answer without re-derivation. The tax is mechanically predictable from conversation features and partly tractable: a prompt intervention targeting all four stages closes a substantial fraction of the gap, with the dominant bottleneck differing across categories. In heterogeneous pairs the tax is pulled toward the stronger partner rather than the additive midpoint, empirically realising the max-superadditivity violation predicted by our framework. Together these results recast collaboration in LLM systems as a measurable, predictable, and partly tractable cost.

## 내 메모


