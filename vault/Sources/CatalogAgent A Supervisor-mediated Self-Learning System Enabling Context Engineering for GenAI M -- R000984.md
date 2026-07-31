---
type: research-source
item_id: 984
title: "CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models"
source: "arxiv"
published: "2026-07-15T22:20:59Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14396"
url: "https://arxiv.org/abs/2607.14396v1"
generated_by: codex-research-db
aliases:
  - "CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models"
topics:
  - "self-evolving-harness"
---

# CatalogAgent: A Supervisor-mediated Self-Learning System Enabling Context Engineering for GenAI Models

[원문 열기](https://arxiv.org/abs/2607.14396v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7FXPE7CF`)
- 발행일: 2026-07-15T22:20:59Z
- 저자: Zhu Cheng, Zhenming Wang, Yu, Tang, Dan Liu, Bryan Zhang, Athanasios N. Nikolakopoulos, Pranav Souri Itabada, Jing Zhang, Chih-Chi Chou, Peng Gao, Fatemeh Mansoori, Bharat Bojja, Sarath Chander, Sameer Thombare, Umit Batur, Tarik Arici
- 식별자: `arxiv:2607.14396`

## 요약·초록

Product catalogs are the backbone of e-commerce sites, yet a large number of structured attributes (SAs) -- such as material, color, and shape -- often have missing values. Typically, SA values are extracted from product information, including titles and descriptions. While LLM-based generator-evaluator frameworks have demonstrated effectiveness for SA prediction -- where an LLM generates SA values and another evaluates them -- they face challenges when the Generator and Evaluator produce conflicting outputs, as either component can make mistakes. We introduce \texttt{CatalogAgent}, a novel agentic system that continuously improves Generator and Evaluator models for e-commerce catalog enrichment. When disagreements arise from (1) internal conflicts between the LLM-based Generator and Evaluator, or (2) external feedback from sellers on LLM outputs, a Supervisor Agent intervenes to mediate these conflicts and make final decisions. The system also incorporates a Memory Base and a Memory Summarizer that stores Supervisor Agent activities from individual cases and aggregates patterns into learnings. These learnings are fed back to the worker Generator and Evaluator LLMs, enabling self-improvement without human intervention. Through context engineering -- injecting learnings and insights into worker LLMs' contexts -- the system successfully transfers the Supervisor's capabilities to the Generator and Evaluator, improving their performance by 15.24\% and 13.98\%, respectively. Our experiments demonstrate a new paradigm of Supervisor Agent-mediated self-learning systems for improving generative AI model accuracy.

## 내 메모


