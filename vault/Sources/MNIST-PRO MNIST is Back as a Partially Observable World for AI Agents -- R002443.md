---
type: research-source
item_id: 2443
title: "MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents"
source: "arxiv"
published: "2026-08-31T16:05:39Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.31022"
url: "https://arxiv.org/abs/2608.31022v1"
generated_by: codex-research-db
aliases:
  - "MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents"
topics:
  - "ai-agents"
---

# MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents

[원문 열기](https://arxiv.org/abs/2608.31022v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9JS2IP2K`)
- 발행일: 2026-08-31T16:05:39Z
- 저자: Vernon Toh, Navonil Majumder, Zhengyuan Liu, Nancy F. Chen, Soujanya Poria
- 식별자: `arxiv:2608.31022`

## 요약·초록

AI agents in partially observable environments need to coordinate active sensing with working memory to maintain an evolving perceptual state. However, existing benchmarks struggle to isolate this perceptual-state construction and interpretation capability because they introduce physical and control complexities. We address this with MNIST-PRO, a benchmark that isolates agentic perception by converting MNIST digit recognition into a sequential, glimpse-based search task with lookback constraints. We evaluate ten multimodal models across four memory representations, including raw visual history, textual states, structured metric grid maps, and a consolidated visual canvas. While models excel under full observability, partial observability exposes a clear performance gap. We identify three distinct bottlenecks. First, perceptual-state construction and interpretation present a challenge, as agents struggle to integrate fragmented glimpses. Second, agents often stop exploring before they see the full sequence. Third, models often fail to revise early, incorrect beliefs even when faced with subsequent contradictory evidence. These results show that simply acquiring visual evidence is not enough. Agents must also be able to build and update a reliable perceptual state.

## 내 메모


