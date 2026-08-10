---
type: research-source
item_id: 1767
title: "DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces"
source: "arxiv"
published: "2026-08-04T10:48:11Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.03451"
url: "https://arxiv.org/abs/2608.03451v1"
generated_by: codex-research-db
aliases:
  - "DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces"
topics:
  - "self-evolving-harness"
---

# DataSpace: Benchmarking Data Agents for Verifiable Analytics over Heterogeneous Workspaces

[원문 열기](https://arxiv.org/abs/2608.03451v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-04T10:48:11Z
- 저자: Boyan Li, Zhuowen Liang, Yupeng Xie, Xiaotian Lin, Tianqi Luo, Xinyu Liu, Yizhang Zhu, Zhangyang Peng, Yuan Li, Zhengxuan Zhang, Jiayi Zhang, Nan Tang, Guoliang Li, Yuyu Luo
- 식별자: `arxiv:2608.03451`

## 요약·초록

Data agents enable natural-language analytics over organizational workspaces, where relevant evidence may be scattered across databases, structured files, long documents, and multimedia. Existing benchmarks largely isolate structured querying, retrieval, or open-ended analysis, leaving heterogeneous evidence discovery, complete tabular outputs, and deterministic evaluation insufficiently unified. We introduce DataSpace, a benchmark in which data agents produce verifiable tabular results from task-local heterogeneous workspaces. It contains 410 cross-language tasks and 7,439 artifacts totaling 15.01 GB across CSV, JSON, SQLite, Markdown, PDF, and video. DataSpace also served as the official evaluation benchmark for the KDD Cup 2026 Data Agents for Complex Data Analysis competition. Each agent receives only a question and workspace and returns the complete requested tabular result. We construct DataSpace with DataSpace-Builder, an execution-grounded framework comprising cross-language transformation, constraint-aware relational sampling, modality routing and artifact rendering, and human review and task repair by 11 domain experts. A deterministic evaluator performs header-invariant column alignment, type- and precision-aware normalization, and order-aware row comparison. Across six recently released frontier multimodal models and five widely used agent harnesses, the best accuracy reaches 66.34%, while harness choice creates a 15.36-point spread with the backbone fixed. Multimodal evidence integration and joins consistently reduce accuracy across all six backbones. These results show that DataSpace remains unsaturated and identify key challenges for improving data-agent reliability.

## 내 메모


