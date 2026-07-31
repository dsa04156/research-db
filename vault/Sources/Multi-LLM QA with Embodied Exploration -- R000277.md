---
type: research-source
item_id: 277
title: "Multi-LLM QA with Embodied Exploration"
source: "arxiv"
published: "2024-06-16T12:46:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.10918"
url: "https://arxiv.org/abs/2406.10918v5"
generated_by: codex-research-db
aliases:
  - "Multi-LLM QA with Embodied Exploration"
topics:
  - "ai-agents"
---

# Multi-LLM QA with Embodied Exploration

[원문 열기](https://arxiv.org/abs/2406.10918v5)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NABK3XCP`)
- 발행일: 2024-06-16T12:46:40Z
- 저자: Bhrij Patel, Vishnu Sashank Dorbala, Amrit Singh Bedi, Dinesh Manocha
- 식별자: `arxiv:2406.10918`

## 요약·초록

Large language models (LLMs) have grown in popularity due to their natural language interface and pre trained knowledge, leading to rapidly increasing success in question-answering (QA) tasks. More recently, multi-agent systems with LLM-based agents (Multi-LLM) have been utilized increasingly more for QA. In these scenarios, the models may each answer the question and reach a consensus or each model is specialized to answer different domain questions. However, most prior work dealing with Multi-LLM QA has focused on scenarios where the models are asked in a zero-shot manner or are given information sources to extract the answer. For question answering of an unknown environment, embodied exploration of the environment is first needed to answer the question. This skill is necessary for personalizing embodied AI to environments such as households. There is a lack of insight into whether a Multi-LLM system can handle question-answering based on observations from embodied exploration. In this work, we address this gap by investigating the use of Multi-Embodied LLM Explorers (MELE) for QA in an unknown environment. Multiple LLM-based agents independently explore and then answer queries about a household environment. We analyze different aggregation methods to generate a single, final answer for each query: debating, majority voting, and training a central answer module (CAM). Using CAM, we observe a $46\%$ higher accuracy compared against the other non-learning-based aggregation methods. We provide code and the query dataset for further research.

## 내 메모


