---
type: research-source
item_id: 1287
title: "SlsReuse: LLM-Powered Serverless Function Reuse"
source: "arxiv"
published: "2025-11-21T14:08:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2511.17262"
url: "https://arxiv.org/abs/2511.17262v1"
generated_by: codex-research-db
aliases:
  - "SlsReuse: LLM-Powered Serverless Function Reuse"
topics:
  - "cloud-infrastructure"
---

# SlsReuse: LLM-Powered Serverless Function Reuse

[원문 열기](https://arxiv.org/abs/2511.17262v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VMXQB9BM`)
- 발행일: 2025-11-21T14:08:12Z
- 저자: Jinfeng Wen, Yuehan Sun
- 식별자: `arxiv:2511.17262`

## 요약·초록

Serverless computing has rapidly emerged as a popular cloud computing paradigm. It enables developers to implement function-level tasks, i.e., serverless functions, without managing infrastructure. While reducing operational overhead, it poses challenges, especially for novice developers. Developing functions from scratch requires adapting to heterogeneous, platform-specific programming styles, making the process time-consuming and error-prone. Function reuse offers a promising solution to address these challenges. However, research on serverless computing lacks a dedicated approach for function recommendation. Existing techniques from traditional contexts remain insufficient due to the semantic gap between task descriptions and heterogeneous function implementations. Advances in large language models (LLMs), pre-trained on large-scale corpora, create opportunities to bridge this gap by aligning developer requirements with function semantics. This paper presents SlsReuse, the first LLM-powered framework for serverless function reuse. Specifically, SlsReuse first constructs a reusable function repository serving as a foundational knowledge base. Then, it learns unified semantic-enhanced representations of heterogeneous functions through effective prompt engineering with few-shot prompting, capturing implicit code intent, target platforms, programming languages, and cloud services. Finally, given a natural language task query, SlsReuse performs intent-aware discovery combined with a multi-level pruning strategy and similarity matching. We evaluate SlsReuse on a curated dataset of 110 task queries. Built on ChatGPT-4o, one of the most representative LLMs, SlsReuse achieves Recall@10 of 91.20%, exceeding the state-of-the-art baseline by 24.53 percentage points.

## 내 메모


