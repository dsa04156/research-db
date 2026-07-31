---
type: research-source
item_id: 1000
title: "SimpleWikiSearch: A Clean Offline Wikipedia Environment for Agentic Search"
source: "arxiv"
published: "2026-07-10T13:05:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26070"
url: "https://arxiv.org/abs/2607.26070v1"
generated_by: codex-research-db
aliases:
  - "SimpleWikiSearch: A Clean Offline Wikipedia Environment for Agentic Search"
topics:
  - "self-evolving-harness"
---

# SimpleWikiSearch: A Clean Offline Wikipedia Environment for Agentic Search

[원문 열기](https://arxiv.org/abs/2607.26070v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SPKEU9Q5`)
- 발행일: 2026-07-10T13:05:10Z
- 저자: Guanming Xiong, Penghui Zhang
- 식별자: `arxiv:2607.26070`

## 요약·초록

Large language model (LLM)-based agentic search systems are often evaluated as if the underlying LLM were the only component that matters, yet their measured performance also depends on the surrounding search environment: the Wikipedia snapshot, preprocessing pipeline, chunking policy, retrieval backend, tool schema, observation format, and answer submission rule. These details are frequently under-specified, making it difficult to compare results or reproduce reported baselines. We present SimpleWikiSearch, whose corpus construction, retrieval stack, tool contract, and evaluation protocol are explicit and runnable. The environment starts from a full English Wikipedia dump, cleans and chunks the corpus, builds keyword and dense retrieval indexes, and exposes a minimal tool interface consisting of \texttt{search}, \texttt{open\_url}, and \texttt{submit\_answer}. We report baseline results on six QA datasets using open-source LLMs and provide a random-300 subset for comparisons with closed-source commercial models. SimpleWikiSearch provides a domain-specific agent harness and a controlled offline environment for reproducible agentic-search evaluation. Its contribution is this specified reference setup, rather than a new agent algorithm. Code and data will be available at: https://github.com/JimXiongGM/simple_wiki_search.

## 내 메모


