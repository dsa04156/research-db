---
type: research-source
item_id: 2806
title: "Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science"
source: "arxiv"
published: "2026-09-14T17:58:55Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.15983"
url: "https://arxiv.org/abs/2609.15983v2"
generated_by: codex-research-db
aliases:
  - "Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science"
topics:
  - "self-evolving-harness"
---

# Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science

[원문 열기](https://arxiv.org/abs/2609.15983v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-14T17:58:55Z
- 저자: Honghao Lin, David P. Woodruff, Yuan Deng, Jieming Mao, Song Zuo, Vahab Mirrokni
- 식별자: `arxiv:2609.15983`

## 요약·초록

Language models can produce plausible short proofs, but may still be unreliable on long-horizon research problems, where progress depends on a sequence of uncertain and interdependent decisions. We introduce Stellar Colosseum, a model-agnostic harness for allocating inference across research in mathematics and theoretical computer science. Colosseum explores alternative strategies before proof construction, uses a readiness gate to decide when a route is mature enough to decompose, represents the proof plan as interdependent section-level subproblems, and routes verifier findings back to the affected part of the argument. Across these stages, it generates candidates in parallel, attacks them with targeted falsification, and combines candidates and their critiques into a single research artifact through overlapping random-sample tree aggregation. The Colosseum workflow has also been integrated into Google Antigravity's Teamwork framework as the Long Proof pattern. We demonstrate the capabilities of Colosseum through open-ended research and evaluations on theorem-proving and competitive programming benchmarks. Using Colosseum with Gemini 3.1 Pro, we obtain several new results that address open problems arising from papers published at top venues such as FOCS and JMLR. On TCS-Bench, a benchmark of research-level theorem-proving tasks drawn from papers published at FOCS, STOC, and SODA, Colosseum achieves 71.0% accuracy using Gemini 3.1 Pro and Gemini 3.7 Flash. In a separate Codeforces evaluation using Gemini 3.1 Pro, the proof-oriented pipeline with execution feedback solves 218 of 222 problems.

## 내 메모
