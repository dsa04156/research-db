---
type: research-source
item_id: 2754
title: "MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis"
source: "arxiv"
published: "2026-09-08T12:59:46Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.08696"
url: "https://arxiv.org/abs/2609.08696v1"
generated_by: codex-research-db
aliases:
  - "MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis"
topics:
  - "ai-agents"
---

# MorphoOrgaAgent: A Foundation-Model-Based Multi-Agent System for Autonomous Organoid Analysis

[원문 열기](https://arxiv.org/abs/2609.08696v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6PDVPXKS`)
- 발행일: 2026-09-08T12:59:46Z
- 저자: Hanyi Zhang, Maximilian Hoermann, Lion J. Gleiter, Yiling Xu, Bettina Katalin Budai, Hans-Ulrich Kauczor, Carsten Marr, Tingying Peng
- 식별자: `arxiv:2609.08696`

## 요약·초록

Organoids are three-dimensional tissue models whose morphology provides important insights into tumor development, disease progression, and drug testing. Extracting these morphological features relies heavily on manual segmentation, which is time-consuming and labor-intensive. Furthermore, performing quantitative statistical analysis typically requires custom coding skills and a mathematical background, presenting a major barrier for experimental biologists. To address these challenges, we introduce MorphoOrgaAgent, a multi-agent framework that achieves zero-shot organoid segmentation, automated data analysis, and report generation based on natural language input. The framework consists mainly of three core components: a TaskUnderstandingAgent that identifies requested measurements and visualization types; a hybrid segmentation module that combines Cellpose-derived geometric prompts with text prompts to guide SAM3 for zero-shot organoid instance segmentation; and a ReportAgent that computes quantitative metrics and compiles them alongside generated visualizations into a structured report. We further introduce MorphoOrgaVQA, a benchmark designed for quantitative evaluation of agent systems in organoid morphology analysis. Experimental results demonstrate that MorphoOrgaAgent handles both explicit and descriptive user requests, produces measurements closely matching ground truth, and generates complete analysis reports without requiring manual programming. The complete source code and MorphoOrgaVQA benchmark are publicly available at https://github.com/peng-lab/MorphoOrgaAgent.

## 내 메모


