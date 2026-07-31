---
type: research-source
item_id: 543
title: "Prometheus: Towards Long-Horizon Codebase Navigation for Repository-Level Problem Solving"
source: "arxiv"
published: "2025-07-26T13:13:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.19942"
url: "https://arxiv.org/abs/2507.19942v2"
generated_by: codex-research-db
aliases:
  - "Prometheus: Towards Long-Horizon Codebase Navigation for Repository-Level Problem Solving"
topics:
  - "ai-agents"
---

# Prometheus: Towards Long-Horizon Codebase Navigation for Repository-Level Problem Solving

[원문 열기](https://arxiv.org/abs/2507.19942v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DWP6KW2Z`)
- 발행일: 2025-07-26T13:13:22Z
- 저자: Yue Pan, Zimin Chen, Siyu Lu, Zhaoyang Chu, Xiang Li, Han Li, Yang Feng, Claire Le Goues, Federica Sarro, Martin Monperrus, He Ye
- 식별자: `arxiv:2507.19942`

## 요약·초록

Large Language Models (LLMs) have shown remarkable capabilities in automating software engineering tasks, spurring the emergence of coding agents that scaffold LLMs with external tools to resolve repository-level problems. However, existing agents still struggle to navigate large-scale codebases, as the Needle-in-a-Haystack problem persists even with million-token context windows, where relevant evidence is often overwhelmed by large volumes of irrelevant code and documentation. Prior codebase navigation approaches, including embedding-based retrieval, file-system exploration, and graph-based retrieval, address parts of this challenge but fail to capture the temporal continuity of agent reasoning, rendering agents stateless and causing repeated repository traversals that hinder scalable planning and reasoning. To address these limitations, we present Prometheus, a memory-centric coding agent framework for long-horizon codebase navigation. Prometheus represents the repository as a unified knowledge graph to encode semantic dependencies and employs a context engine augmented with working memory that retains and reuses previously explored contexts to ensure continuity across reasoning steps. Built upon this engine, Prometheus integrates memory-enhanced navigation into a multi-agent system for automated issue resolution, encompassing issue classification, bug reproduction, patch generation, and verification. Comprehensive experiments are conducted on two widely used issue resolution benchmarks, i.e., SWE-bench Verified and SWE-PolyBench Verified. Powered by GPT-5, Prometheus achieves state-of-the-art performance with 74.4% and 33.8% resolution rates on the two benchmarks, ranking Top-6 and Top-1 among open-source agent systems, respectively. Our data and code are available at https://github.com/EuniAI/Prometheus.

## 내 메모


