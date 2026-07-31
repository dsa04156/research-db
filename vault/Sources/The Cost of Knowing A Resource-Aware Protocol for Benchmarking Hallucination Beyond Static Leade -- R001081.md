---
type: research-source
item_id: 1081
title: "The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards"
source: "arxiv"
published: "2026-07-27T07:05:11Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.24063"
url: "https://arxiv.org/abs/2607.24063v2"
generated_by: codex-research-db
aliases:
  - "The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards"
topics:
  - "ai-agents"
---

# The Cost of Knowing: A Resource-Aware Protocol for Benchmarking Hallucination Beyond Static Leaderboards

[원문 열기](https://arxiv.org/abs/2607.24063v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9PA7VBKJ`)
- 발행일: 2026-07-27T07:05:11Z
- 저자: Keyu Li, Jin Gao, Dequan Wang
- 식별자: `arxiv:2607.24063`

## 요약·초록

On standard factuality tasks, frontier models now cluster near the top of the scale. The question is therefore shifting from how factual a system is toward how much compute that factuality costs. Static leaderboards score factuality in isolation and treat compute as free, so they cannot tell a genuinely better system apart from one that simply spends more. Consider a ranking reversal. A brute-force Best-of-4 agent posts the higher raw factuality score (H-Score 0.9169 vs 0.9103) and would top a static leaderboard, but once cost is counted it is the worse system, losing on Q-Score (0.5169 vs 0.5217) at roughly four times the tokens and latency, under a reported cost weight whose sensitivity we sweep. So the system that tops a static leaderboard can be the worse one to deploy. To make this trade-off visible, we introduce MAS-HQ (Multi-Agent System Hallucination Quest), a resource-aware evaluation protocol. It wraps any factuality detector and normalizes for cost, and it pits systems against each other rather than scoring them in isolation. The Q-Score measures factuality minus normalized cost under a competitive match. Across summarization and open-domain QA, single-agent baselines drift into resource-heavy over-optimization, while competition elicits more resource-efficient policies. These gains are small but consistent, and stable across 100 trials. The axis stays discriminative for frontier systems (Gemini-2.5-Pro, and GPT-5) whose raw factuality scores are already bunched near the ceiling. MAS-HQ provides a reproducible way to measure how much a factual answer costs.

## 내 메모


