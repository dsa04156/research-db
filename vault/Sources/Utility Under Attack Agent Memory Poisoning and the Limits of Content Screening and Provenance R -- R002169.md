---
type: research-source
item_id: 2169
title: "Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking"
source: "arxiv"
published: "2026-08-21T15:37:35Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.21230"
url: "https://arxiv.org/abs/2608.21230v1"
generated_by: codex-research-db
aliases:
  - "Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking"
topics:
  - "ai-agents"
---

# Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking

[원문 열기](https://arxiv.org/abs/2608.21230v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZH98W6T6`)
- 발행일: 2026-08-21T15:37:35Z
- 저자: Arulnidhi Karunanidhi
- 식별자: `arxiv:2608.21230`

## 요약·초록

Persistent memory makes false information durable: once a false statement is stored, it can be retrieved into future sessions that match it. We measure the cost of this failure mode using plainly worded false assertions generated in a single pass, with no instruction, trigger, or retriever optimization. Poisoning 1.2% of a LongMemEval corpus reduces accuracy from 0.850 to 0.300. A four-stage write-time screening pipeline that reaches 0.832 recall on indirect prompt injection while flagging 1.5% of trigger-word-laden benign text rejects 0 of 360 poisoned memories. We argue this exposes a boundary of content-only screening: distinguishing a false assertion from a true one generally requires external grounding beyond the text itself. We then evaluate provenance-weighted retrieval. The shipped weight is statistically indistinguishable from no defense (p=0.80), while a stronger weight recovers utility only by excluding untrusted content. In a mixed-provenance corpus where untrusted content is mostly benign, accuracy rises from 0.3167 to 0.7000; when the answer-bearing evidence itself arrives untrusted, evidence recall falls to zero and accuracy to 0.0417. Under the measured similarity regime, the additive provenance term has no usable setting: a weight strong enough to resist query-shaped poison is also strong enough to suppress legitimate untrusted evidence. We therefore argue for bounded occupancy constraints at retrieval rather than additive provenance penalties, and release the harnesses, corpora, and aggregate run reports.

## 내 메모


