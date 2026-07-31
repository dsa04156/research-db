---
type: research-source
item_id: 244
title: "BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science"
source: "arxiv"
published: "2024-06-29T15:23:28Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.00466"
url: "https://arxiv.org/abs/2407.00466v1"
generated_by: codex-research-db
aliases:
  - "BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science"
topics:
  - "ai-agents"
---

# BioKGBench: A Knowledge Graph Checking Benchmark of AI Agent for Biomedical Science

[원문 열기](https://arxiv.org/abs/2407.00466v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VT8EKH4C`)
- 발행일: 2024-06-29T15:23:28Z
- 저자: Xinna Lin, Siqi Ma, Junjie Shan, Xiaojing Zhang, Shell Xu Hu, Tiannan Guo, Stan Z. Li, Kaicheng Yu
- 식별자: `arxiv:2407.00466`

## 요약·초록

Pursuing artificial intelligence for biomedical science, a.k.a. AI Scientist, draws increasing attention, where one common approach is to build a copilot agent driven by Large Language Models (LLMs). However, to evaluate such systems, people either rely on direct Question-Answering (QA) to the LLM itself, or in a biomedical experimental manner. How to precisely benchmark biomedical agents from an AI Scientist perspective remains largely unexplored. To this end, we draw inspiration from one most important abilities of scientists, understanding the literature, and introduce BioKGBench. In contrast to traditional evaluation benchmark that only focuses on factual QA, where the LLMs are known to have hallucination issues, we first disentangle "Understanding Literature" into two atomic abilities, i) "Understanding" the unstructured text from research papers by performing scientific claim verification, and ii) Ability to interact with structured Knowledge-Graph Question-Answering (KGQA) as a form of "Literature" grounding. We then formulate a novel agent task, dubbed KGCheck, using KGQA and domain-based Retrieval-Augmented Generation (RAG) to identify the factual errors of existing large-scale knowledge graph databases. We collect over two thousand data for two atomic tasks and 225 high-quality annotated data for the agent task. Surprisingly, we discover that state-of-the-art agents, both daily scenarios and biomedical ones, have either failed or inferior performance on our benchmark. We then introduce a simple yet effective baseline, dubbed BKGAgent. On the widely used popular knowledge graph, we discover over 90 factual errors which provide scenarios for agents to make discoveries and demonstrate the effectiveness of our approach. The code and data are available at https://github.com/westlake-autolab/BioKGBench.

## 내 메모


