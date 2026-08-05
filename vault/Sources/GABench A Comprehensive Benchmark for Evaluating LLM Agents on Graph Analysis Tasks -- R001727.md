---
type: research-source
item_id: 1727
title: "GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks"
source: "arxiv"
published: "2026-08-03T04:18:31Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01684"
url: "https://arxiv.org/abs/2608.01684v1"
generated_by: codex-research-db
aliases:
  - "GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks"
topics:
  - "self-evolving-harness"
---

# GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks

[원문 열기](https://arxiv.org/abs/2608.01684v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UPCB425Q`)
- 발행일: 2026-08-03T04:18:31Z
- 저자: Jiarui Tan, Zhongjian Zhang, YaBo Guo, Jiawei Liu, Yujie Xing, Muhan Zhang, Cheng Yang, Chuan Shi
- 식별자: `arxiv:2608.01684`

## 요약·초록

Large language model (LLM) agents are increasingly capable of planning, using tools, and interacting with external environments. They are typically supported by harnesses, which manage state and coordinate multi-step execution. Graph analysis provides a promising setting for evaluating their agentic capabilities, because it requires agents to access data and execute operations in a graph environment. However, existing graph benchmarks for LLMs provide limited coverage of graph tasks and graph types, making it difficult to comprehensively evaluate LLM agents. Moreover, they typically formulate graph analysis as text-based question answering, where graph information is directly provided in the prompt, limiting the evaluation of end-to-end agentic capabilities. To address these limitations, we introduce GABench, a comprehensive benchmark for agentic graph analysis. GABench spans three graph types and covers four graph analysis task categories: graph retrieval, graph theory, graph machine learning, and graph open-ended question answering. GABench also provides 84 executable tools for accessing graph data and performing diverse graph operations. Building on these tools, we develop an agentic graph analysis task generation pipeline and construct 10,400 tasks with verifiable ground truth.Using GABench, we evaluate a range of frontier LLMs and agent harnesses. Our experiments reveal three key findings: (1) Existing LLM agents still struggle with complex graph analysis tasks. (2) Harness choice significantly affects performance, yet existing harnesses remain limited on complex graph tasks. (3) Graph analysis depends more on tool-call quality than quantity. Our findings provide practical insights into the development and evaluation of LLM agents for graph analysis.

## 내 메모


