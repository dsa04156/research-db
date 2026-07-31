---
type: research-source
item_id: 191
title: "REAPER: Reasoning based Retrieval Planning for Complex RAG Systems"
source: "arxiv"
published: "2024-07-26T07:05:54Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2407.18553"
url: "https://arxiv.org/abs/2407.18553v2"
generated_by: codex-research-db
aliases:
  - "REAPER: Reasoning based Retrieval Planning for Complex RAG Systems"
topics:
  - "ai-agents"
---

# REAPER: Reasoning based Retrieval Planning for Complex RAG Systems

[원문 열기](https://arxiv.org/abs/2407.18553v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JMEBTUSQ`)
- 발행일: 2024-07-26T07:05:54Z
- 저자: Ashutosh Joshi, Sheikh Muhammad Sarwar, Samarth Varshney, Sreyashi Nag, Shrivats Agrawal, Juhi Naik
- 식별자: `doi:10.48550/arxiv.2407.18553`

## 요약·초록

Complex dialog systems often use retrieved evidence to facilitate factual responses. Such RAG (Retrieval Augmented Generation) systems retrieve from massive heterogeneous data stores that are usually architected as multiple indexes or APIs instead of a single monolithic source. For a given query, relevant evidence needs to be retrieved from one or a small subset of possible retrieval sources. Complex queries can even require multi-step retrieval. For example, a conversational agent on a retail site answering customer questions about past orders will need to retrieve the appropriate customer order first and then the evidence relevant to the customer's question in the context of the ordered product. Most RAG Agents handle such Chain-of-Thought (CoT) tasks by interleaving reasoning and retrieval steps. However, each reasoning step directly adds to the latency of the system. For large models this latency cost is significant -- in the order of multiple seconds. Multi-agent systems may classify the query to a single Agent associated with a retrieval source, though this means that a (small) classification model dictates the performance of a large language model. In this work we present REAPER (REAsoning-based PlannER) - an LLM based planner to generate retrieval plans in conversational systems. We show significant gains in latency over Agent-based systems and are able to scale easily to new and unseen use cases as compared to classification-based planning. Though our method can be applied to any RAG system, we show our results in the context of a conversational shopping assistant.

## 내 메모


