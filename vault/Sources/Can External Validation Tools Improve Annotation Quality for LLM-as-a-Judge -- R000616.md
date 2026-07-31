---
type: research-source
item_id: 616
title: "Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?"
source: "arxiv"
published: "2025-07-22T20:57:09Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.17015"
url: "https://arxiv.org/abs/2507.17015v1"
generated_by: codex-research-db
aliases:
  - "Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?"
topics:
  - "ai-agents"
---

# Can External Validation Tools Improve Annotation Quality for LLM-as-a-Judge?

[원문 열기](https://arxiv.org/abs/2507.17015v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`Q9FGN75Z`)
- 발행일: 2025-07-22T20:57:09Z
- 저자: Arduin Findeis, Floris Weers, Guoli Yin, Ke Ye, Ruoming Pang, Tom Gunter
- 식별자: `arxiv:2507.17015`

## 요약·초록

Pairwise preferences over model responses are widely collected to evaluate and provide feedback to large language models (LLMs). Given two alternative model responses to the same input, a human or AI annotator selects the "better" response. This approach can provide feedback for domains where other hard-coded metrics are difficult to obtain (e.g., chat response quality), thereby helping model evaluation or training. However, for some domains high-quality pairwise comparisons can be tricky to obtain - from AI and humans. For example, for responses with many factual statements, annotators may disproportionately weigh writing quality rather than underlying facts. In this work, we explore augmenting standard AI annotator systems with additional tools to improve performance on three challenging response domains: long-form factual, math and code tasks. We propose a tool-using agentic system to provide higher quality feedback on these domains. Our system uses web-search and code execution to ground itself based on external validation, independent of the LLM's internal knowledge and biases. We provide extensive experimental results evaluating our method across the three targeted response domains as well as general annotation tasks, using RewardBench (incl. AlpacaEval and LLMBar), RewardMath, as well as three new datasets for domains with saturated pre-existing datasets. Our results indicate that external tools can indeed improve performance in many, but not all, cases. More generally, our experiments highlight the sensitivity of performance to simple parameters (e.g., prompt) and the need for improved (non-saturated) annotator benchmarks. We share our code at https://github.com/apple/ml-agent-evaluator.

## 내 메모


