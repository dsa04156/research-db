---
type: research-source
item_id: 1074
title: "Addressable Recall Compaction for Long Context-Window Control in AI Agents"
source: "arxiv"
published: "2026-07-27T20:51:05Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25066"
url: "https://arxiv.org/abs/2607.25066v1"
generated_by: codex-research-db
aliases:
  - "Addressable Recall Compaction for Long Context-Window Control in AI Agents"
topics:
  - "ai-agents"
---

# Addressable Recall Compaction for Long Context-Window Control in AI Agents

[원문 열기](https://arxiv.org/abs/2607.25066v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PN54NK76`)
- 발행일: 2026-07-27T20:51:05Z
- 저자: Thang Dang, Yuma Ichikawa, Sakina Fatima, Koichi Shirahata
- 식별자: `arxiv:2607.25066`

## 요약·초록

Long-horizon LLM agents accumulate reasoning traces, actions, and tool observations that can eventually exceed a model's fixed context window. Existing compaction methods address this limitation by discarding, summarizing, or retrieving earlier information, but they may remove task-critical details or fail to recover them reliably. We propose ARC (Addressable Recall Compaction), a context-management framework that separates archival storage from active-context presentation. ARC stores tool observations in an append-only, ID-addressable log and replaces older observations with compact citations when compaction is required. The agent can subsequently use these identifiers to request stored content without re-executing the corresponding tools or depending solely on similarity-based retrieval. We evaluate ARC using Qwen3-8B with a 16k context window and Qwen3-32B with a 32k context window. On the Needle-in-a-Haystack evaluation, ARC achieves an average exact-answer accuracy of 99.40%, compared with 88.12% for the best-performing baseline in our evaluation. ARC also reduces estimated serving time and HBM traffic under our hardware-cost model. On the LongBench-v2 Hard subset, ARC obtains an average accuracy of 29.97%, compared with 28.25% for the best-performing baseline. These results indicate that explicit, address-based recall can improve information retention and serving efficiency relative to the evaluated context-management baselines under the tested settings.

## 내 메모


