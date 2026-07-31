---
type: research-source
item_id: 180
title: "Couler: Unified Machine Learning Workflow Optimization in Cloud"
source: "arxiv"
published: "2024-03-12T12:47:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2403.07608"
url: "https://arxiv.org/abs/2403.07608v1"
generated_by: codex-research-db
aliases:
  - "Couler: Unified Machine Learning Workflow Optimization in Cloud"
topics:
  - "self-evolving-harness"
---

# Couler: Unified Machine Learning Workflow Optimization in Cloud

[원문 열기](https://arxiv.org/abs/2403.07608v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`G2J45HN8`)
- 발행일: 2024-03-12T12:47:32Z
- 저자: Xiaoda Wang, Yuan Tang, Tengda Guo, Bo Sang, Jingji Wu, Jian Sha, Ke Zhang, Jiang Qian, Mingjie Tang
- 식별자: `arxiv:2403.07608`

## 요약·초록

Machine Learning (ML) has become ubiquitous, fueling data-driven applications across various organizations. Contrary to the traditional perception of ML in research, ML workflows can be complex, resource-intensive, and time-consuming. Expanding an ML workflow to encompass a wider range of data infrastructure and data types may lead to larger workloads and increased deployment costs. Currently, numerous workflow engines are available (with over ten being widely recognized). This variety poses a challenge for end-users in terms of mastering different engine APIs. While efforts have primarily focused on optimizing ML Operations (MLOps) for a specific workflow engine, current methods largely overlook workflow optimization across different engines. In this work, we design and implement Couler, a system designed for unified ML workflow optimization in the cloud. Our main insight lies in the ability to generate an ML workflow using natural language (NL) descriptions. We integrate Large Language Models (LLMs) into workflow generation, and provide a unified programming interface for various workflow engines. This approach alleviates the need to understand various workflow engines' APIs. Moreover, Couler enhances workflow computation efficiency by introducing automated caching at multiple stages, enabling large workflow auto-parallelization and automatic hyperparameters tuning. These enhancements minimize redundant computational costs and improve fault tolerance during deep learning workflow training. Couler is extensively deployed in real-world production scenarios at Ant Group, handling approximately 22k workflows daily, and has successfully improved the CPU/Memory utilization by more than 15% and the workflow completion rate by around 17%.

## 내 메모


