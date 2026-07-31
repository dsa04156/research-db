---
type: research-source
item_id: 1002
title: "Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift"
source: "arxiv"
published: "2026-07-10T08:10:37Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.09175"
url: "https://arxiv.org/abs/2607.09175v1"
generated_by: codex-research-db
aliases:
  - "Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift

[원문 열기](https://arxiv.org/abs/2607.09175v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`N6GX52JH`)
- 발행일: 2026-07-10T08:10:37Z
- 저자: Dan C. Hsu, Luke Lu
- 식별자: `arxiv:2607.09175`

## 요약·초록

Deployed LLM agents rely on agentic context, the model-external textual control content assembled by an operational harness. In this work, the mutable component of that context is a persistent system-level instruction that is updated from operational experience while the model, tools, and harness remain fixed. Over long evolution horizons, flat-text maintenance makes verification increasingly difficult as accumulated instructions grow and interact. We propose Graph-Regularized Agentic Context Evolution (GRACE), which maintains the persistent instruction component as a typed semantic graph and validates proposed updates within the local typed neighborhoods of modified nodes. Accepted graph updates are reconstructed as incremental edits to the textual instruction checkpoint used at deployment. We evaluate GRACE within a fixed telecom agent harness derived from $τ^2$-bench under a controlled distribution-shift protocol. Across five independent replications, GRACE improves strict reliability, measured by pass^3, from the Gemini 2.5 Flash zero-shot value of 0.091 to 0.673$\pm$0.136 at the final checkpoint. This exceeds a Gemini 3.1 Pro zero-shot reference of 0.242 on the same held-out set, while the flat-text HCE baseline finishes at 0.191$\pm$0.051. These results identify two requirements for reliable long-horizon context evolution, a structural substrate that makes verification local and a consolidation mechanism that keeps accumulated instruction content usable.

## 내 메모


