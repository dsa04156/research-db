---
type: research-source
item_id: 2740
title: "Kernel-Managed Shared Memory for System-Wide Personalization"
source: "arxiv"
published: "2026-09-09T13:20:47Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.10144"
url: "https://arxiv.org/abs/2609.10144v1"
generated_by: codex-research-db
aliases:
  - "Kernel-Managed Shared Memory for System-Wide Personalization"
topics:
  - "ai-agents"
---

# Kernel-Managed Shared Memory for System-Wide Personalization

[원문 열기](https://arxiv.org/abs/2609.10144v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`H6K9QB42`)
- 발행일: 2026-09-09T13:20:47Z
- 저자: Ryan Lum, Yongfeng Zhang
- 식별자: `arxiv:2609.10144`

## 요약·초록

AI systems become more useful when they can adapt to the people using them, but in multi-agent systems, useful context learned by one agent often remains unavailable to others. We present kernel-managed shared memory, a system-level abstraction in which specialized agents write structured, tagged memories while the agent-system kernel, not individual agents, governs retrieval, privacy enforcement, and prompt injection. We implement and evaluate this design on AIOS and compare it against three alternatives across three assistant models (GPT-4o, Llama-3.1:8B, Qwen-2.5:7B) and 1,800 total trials. Against an unmanaged external memory backend (Mem0) using identical underlying storage, kernel-managed retrieval and injection improve personalization scores by 2.4-4.0 points on a 5-point scale (e.g., 1.05 to 4.69 profile usage on GPT-4o), with every comparison significant at p < 10^-18. Against standard retrieval-augmented injection, gains are similarly large and consistent across all three models. Against full, unfiltered context concatenation, a soft ceiling on available context rather than on response quality, kernel-managed injection statistically matches performance on two of three models and shows a small, model-specific deficit on the third, while using substantially shorter prompts: end-to-end latency is 15-61% lower across all three models, with corresponding reductions in per-call token usage and inference cost. These results indicate that centralizing memory management in the agent-system kernel, rather than leaving retrieval and privacy enforcement to individual agents, delivers most of the personalization benefit of unconstrained context at a fraction of its cost.

## 내 메모


