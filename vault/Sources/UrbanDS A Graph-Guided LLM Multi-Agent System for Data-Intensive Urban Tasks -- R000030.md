---
type: research-source
item_id: 30
title: "UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks"
source: "arxiv"
published: "2026-07-29T10:14:02Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26724"
url: "https://arxiv.org/abs/2607.26724v1"
generated_by: codex-research-db
aliases:
  - "UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks"
topics:
  - "ai-agents"
---

# UrbanDS: A Graph-Guided LLM Multi-Agent System for Data-Intensive Urban Tasks

[원문 열기](https://arxiv.org/abs/2607.26724v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`THBXHHAE`)
- 발행일: 2026-07-29T10:14:02Z
- 저자: Zhilun Zhou, Jianghao Yu, Yuming Lin, yongjun yang, Sun Yongquan, Depeng Jin, Yong Li
- 식별자: `arxiv:2607.26724`

## 요약·초록

Large language model (LLM) agents have been widely applied in automating data science tasks. However, existing methods typically rely on a limited set of provided datasets, and they face challenges in data-intensive scenarios that require discovering and leveraging relevant information from large-scale and heterogeneous data repositories. Urban tasks are representative examples of such scenarios, as urban data are not only large-scale and multi-sourced, but also exhibit complex spatial, temporal, and semantic relationships. To address these challenges, we propose UrbanDS, a graph-guided LLM multi-agent system for data-intensive urban tasks. We first construct a unified dataset graph to organize reusable dataset skills and the relationships among datasets. Specifically, we develop a Data Profiling Agent that constructs a skill for each dataset. Moreover, a Relation Agent identifies relationships among datasets and integrates these relationships into the dataset graph. At runtime, a Planner Agent retrieves task-relevant datasets from the graph and generates execution plans. Multiple Execution Agents then perform data processing and analysis, while their execution progress and intermediate results are shared through a common memory. Finally, a Report Agent synthesizes the experimental logs into a report, which can be further refined based on user feedback. To systematically evaluate the capability of agents in handling data-intensive urban scenarios, we further construct UrbanDS-Bench, an urban data science benchmark covering representative data analysis and modeling tasks. Experiments on both general and urban benchmarks demonstrate that UrbanDS consistently outperforms existing data science agents on data-intensive tasks. Furthermore, UrbanDS has been deployed on the urban operations platform of Dongxihu District, Wuhan, demonstrating its effectiveness in real-world urban applications.

## 내 메모


