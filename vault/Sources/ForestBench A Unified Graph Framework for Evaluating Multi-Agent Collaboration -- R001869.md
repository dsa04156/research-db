---
type: research-source
item_id: 1869
title: "ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration"
source: "arxiv"
published: "2026-08-09T09:38:52Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.08605"
url: "https://arxiv.org/abs/2608.08605v1"
generated_by: codex-research-db
aliases:
  - "ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration"
topics:
  - "ai-agents"
---

# ForestBench: A Unified Graph Framework for Evaluating Multi-Agent Collaboration

[원문 열기](https://arxiv.org/abs/2608.08605v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-09T09:38:52Z
- 저자: Guo Chen, Ziwen Li, Reed Li, Yu Lu, Haibo Shi, Bingbing Xu, Junjie Huang
- 식별자: `arxiv:2608.08605`

## 요약·초록

Multi-agent systems (MAS) built on Large Language Models (LLMs) are proliferating rapidly, but their heterogeneous execution traces provide no common basis for evaluation across methods. Outcome-only benchmarks discard collaborations, whereas LLM-as-Judge evaluation requires additional, model-dependent inference and can vary with the LLM and rubric. We introduce a generalizable evaluation framework that maps native MAS traces into a shared space of unified collaboration graphs, enabling different methods to be evaluated under the same representation, reference set, and metric panel. Candidate graphs are compared with a query-specific reference forest. Each forest is a benchmark-provided collection of verified-success graphs: it records diverse ways in which representative MAS methods can complete the task, rather than prescribing a unique optimal process. Instantiating the framework as ForestBench, we filter $844$ collaboration-necessary queries from seven public datasets, precompute ten successful target-conditioned reference graphs per query, and evaluate six representative MAS frameworks. Controlled backbone, reference-construction, and perturbation studies test the stability and scope of evaluation. Once the benchmark forests are built, ForestBench scores a trace in milliseconds without further LLM inference, providing a reusable structural basis for comparing diverse MAS collaboration traces.

## 내 메모


