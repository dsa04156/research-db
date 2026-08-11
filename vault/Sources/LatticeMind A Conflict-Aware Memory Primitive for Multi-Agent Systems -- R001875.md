---
type: research-source
item_id: 1875
title: "LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems"
source: "arxiv"
published: "2026-08-08T17:05:08Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.08236"
url: "https://arxiv.org/abs/2608.08236v1"
generated_by: codex-research-db
aliases:
  - "LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems"
topics:
  - "ai-agents"
---

# LatticeMind: A Conflict-Aware Memory Primitive for Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2608.08236v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-08T17:05:08Z
- 저자: Heng Zhou, Lian Zhang, Yutao Fan, Tiancheng He, Siki Chen, Hejia Geng, Philip Torr, Zhenfei Yin
- 식별자: `arxiv:2608.08236`

## 요약·초록

Multi-agent LLM systems often fail not for lack of candidate answers, but because they have no persistent mechanism for deciding which incompatible claim should currently be trusted. Majority vote, debate, and judge-based selection choose an output without recording which claim wins, which is contested, or why a later update supersedes it. We present \term{LatticeMind}, a conflict-aware structured memory that handles contradiction at write time. It maintains explicit item status, applies cheap symbolic conflict checks, and invokes LLM reconciliation only for unresolved semantic cases. On a label-blind ConflictBank evaluation that removes source-name hints, LatticeMind reaches 0.97 accuracy versus 0.61 for the strongest aggregation baseline, with the gap significant at $p<10^{-6}$ by paired McNemar test. Ablations show that removing the checker or the reconciler costs 12 to 14 points. On four secondary planning benchmarks the picture is mixed: LatticeMind beats naive merge on three of four, but does not replace deliberation methods on tasks rewarding iterative search.

## 내 메모


