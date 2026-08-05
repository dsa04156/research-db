---
type: research-source
item_id: 1679
title: "MAPLE-Guard: Memory-Aware Link Enforcement Against Memory-Link Poisoning in Multi-Agent Systems"
source: "arxiv"
published: "2026-08-01T03:55:13Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00426"
url: "https://arxiv.org/abs/2608.00426v1"
generated_by: codex-research-db
aliases:
  - "MAPLE-Guard: Memory-Aware Link Enforcement Against Memory-Link Poisoning in Multi-Agent Systems"
topics:
  - "ai-agents"
---

# MAPLE-Guard: Memory-Aware Link Enforcement Against Memory-Link Poisoning in Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2608.00426v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`V2HKKQWW`)
- 발행일: 2026-08-01T03:55:13Z
- 저자: Wenjun Xiong, Yijin Zhou, Jiaqian Wang, Shangding Gu, Bo Tang, Zhiyu Li, Feiyu Xiong, Ying Wen, Muning Wen
- 식별자: `arxiv:2608.00426`

## 요약·초록

LLM-based multi-agent systems (MAS) increasingly rely on persistent private and shared memories for long-horizon coordination. This memory layer improves continuity, but it also gives attackers a durable channel: a poisoned memory can be written once, continuously retrieved in later tasks, promoted into shared memory, and reused by other agents. A single poisoned write can therefore steer many later decisions and contaminate agents that never saw the original attack, all while no malicious message crosses a visible communication edge at the moment of harm. Further, because existing safeguards mainly inspect prompts, actions, or communication edges, they can miss attacks whose content appears benign at write time but becomes harmful after retrieval. We introduce Memory-Aware Propagation and Link Enforcement Guard, MAPLE-Guard, a memory-link guard for memory-enabled MAS. MAPLE-Guard monitors the memory lifecycle and places gates at write, retrieval, promotion, and cross-agent reuse, so risky memories can be quarantined, unsafe retrievals filtered, and poisoned private memories blocked before they enter shared memory. In the main evaluation, MAPLE-Guard lowers attack success rate (ASR) from 38.2% to 0.9% on LongMemEval and from 34.7% to 0.2% on AppWorld; it also raises multi-agent defense success rate (MDSR) from 54.0% to 74.3% and from 42.5% to 99.8% on the same benchmarks. These results suggest that memory-aware link enforcement covers a gap left by prompt-level and topology-level defenses. Code is available at the link: https://github.com/xiong-wenjun/MAPLE-Guard.

## 내 메모


