---
type: research-source
item_id: 20
title: "PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning"
source: "arxiv"
published: "2026-07-22T12:11:51Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.20064"
url: "https://arxiv.org/abs/2607.20064v2"
generated_by: codex-research-db
aliases:
  - "PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning"
topics:
  - "self-evolving-harness"
---

# PRO-LONG: Programmatic Memory Enables Long-Horizon Reasoning

[원문 열기](https://arxiv.org/abs/2607.20064v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RPTDDDHS`)
- 발행일: 2026-07-22T12:11:51Z
- 저자: Alexis Fox, Junlin Wang, Paul Rosu, Bhuwan Dhingra
- 식별자: `arxiv:2607.20064`

## 요약·초록

Long-horizon tasks require sustained perception, reasoning, and exploration, and are a persistent challenge for large language model (LLM) agents. This gap is reflected in their limited performance on continual learning benchmarks such as ARC-AGI-3, especially when models are evaluated out of the box. Various agent harnesses have been proposed to close this gap, and each commits to a strategy for handling long sequences of observations, i.e., what information to save from the environment and how to load it into model context, a choice we argue is particularly consequential. Existing methods for context management face a significant tradeoff, as preserving more information makes retrieving relevant details less tractable. We propose PRO-LONG, a minimal context management framework built around programmatic memory for LLM agents in long-horizon, exploratory settings. PRO-LONG addresses the tradeoff by keeping a complete, structured interaction log and capitalizing on recent progress in coding agents to search this history efficiently. On the full ARC-AGI-3 public game set, PRO-LONG improves over a base coding agent by an average of 18.0 percentage points across frontier models, and matches or exceeds state-of-the-art specialized harnesses (up to 76.1% pass@1) while using 4.2-5.8x fewer tokens. With Fable 5, PRO-LONG achieves 97.4% best@2 at a total cost of \$1,750. Relevant code and logs are available at https://github.com/alexisfox7/PRO-LONG.

## 내 메모


