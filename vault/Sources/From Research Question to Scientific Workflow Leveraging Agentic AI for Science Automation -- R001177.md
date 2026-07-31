---
type: research-source
item_id: 1177
title: "From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation"
source: "arxiv"
published: "2026-04-23T17:52:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.21910"
url: "https://arxiv.org/abs/2604.21910v1"
generated_by: codex-research-db
aliases:
  - "From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation"
topics:
  - "ai-agents"
  - "kubernetes"
---

# From Research Question to Scientific Workflow: Leveraging Agentic AI for Science Automation

[원문 열기](https://arxiv.org/abs/2604.21910v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2F5XCWTG`)
- 발행일: 2026-04-23T17:52:52Z
- 저자: Bartosz Balis, Michal Orzechowski, Piotr Kica, Michal Dygas, Michal Kuszewski
- 식별자: `arxiv:2604.21910`

## 요약·초록

Scientific workflow systems automate execution -- scheduling, fault tolerance, resource management -- but not the semantic translation that precedes it. Scientists still manually convert research questions into workflow specifications, a task requiring both domain knowledge and infrastructure expertise. We propose an agentic architecture that closes this gap through three layers: an LLM interprets natural language into structured intents (semantic layer); validated generators produce reproducible workflow DAGs (deterministic layer); and domain experts author ``Skills'': markdown documents encoding vocabulary mappings, parameter constraints, and optimization strategies (knowledge layer). This decomposition confines LLM non-determinism to intent extraction: identical intents always yield identical workflows. We implement and evaluate the architecture on the 1000 Genomes population genetics workflow and Hyperflow WMS running on Kubernetes. In an ablation study on 150 queries, Skills raise full-match intent accuracy from 44% to 83%; skill-driven deferred workflow generation reduces data transfer by 92\%; and the end-to-end pipeline completes queries on Kubernetes with LLM overhead below 15 seconds and cost under $0.001 per query.

## 내 메모


