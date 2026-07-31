---
type: research-source
item_id: 1015
title: "Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference"
source: "arxiv"
published: "2026-07-03T02:28:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.02882"
url: "https://arxiv.org/abs/2607.02882v1"
generated_by: codex-research-db
aliases:
  - "Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference"
topics:
  - "self-evolving-harness"
---

# Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference

[원문 열기](https://arxiv.org/abs/2607.02882v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EJE9PJ75`)
- 발행일: 2026-07-03T02:28:32Z
- 저자: Xuyan Ma, Yawen Wang, Junjie Wang, Xiaofei Xie, Boyu Wu, Mingyang Li, Dandan Wang, Qing Wang
- 식별자: `arxiv:2607.02882`

## 요약·초록

Platform-orchestrated agentic workflows have become a popular paradigm for developing LLM-based applications. However, their reliability remains a major challenge due to the uncertainty of LLM outputs, complex inter-node dependencies, and heterogeneous tool interactions. Existing agentic workflow optimization and agent enhancement methods primarily rely on trajectory-level feedback. Without explicitly identifying the underlying failure root causes, their resulting repair plans are often insufficiently targeted. We propose FlowFixer, a diagnosis-driven automated repair framework for agentic workflows. FlowFixer first transforms workflow executions into unified symbolic traces and performs symbolic inference to derive executable behavioral specifications that capture node correctness, temporal dependencies, and causal relationships. Based on specification verification, it conducts failure attribution and root cause analysis, and then generates targeted repair patches. To reduce verification costs, FlowFixer further employs a multi-dimensional pre-execution assessment to filter infeasible repairs before dynamic verification. We evaluate FlowFixer on workflow failures collected from three popular development platforms: Dify, Coze and n8n. Results show that FlowFixer achieves a repair success rate of 71.3%, outperforming state-of-the-art baselines by 11.9% to 27.6%. It also improves failure attribution accuracy by 4.8% to 33.1% and root cause analysis accuracy by 15.3% to 38.8%. This work offers a new perspective on reliable diagnosis and repair of agentic workflows through symbolic modeling and inference.

## 내 메모


