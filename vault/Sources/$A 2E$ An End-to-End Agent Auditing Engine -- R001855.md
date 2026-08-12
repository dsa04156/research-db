---
type: research-source
item_id: 1855
title: "$A^2E$ : An End-to-End Agent Auditing Engine"
source: "arxiv"
published: "2026-08-07T15:44:12Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.07346"
url: "https://arxiv.org/abs/2608.07346v2"
generated_by: codex-research-db
aliases:
  - "$A^2E$ : An End-to-End Agent Auditing Engine"
topics:
  - "self-evolving-harness"
---

# $A^2E$ : An End-to-End Agent Auditing Engine

[원문 열기](https://arxiv.org/abs/2608.07346v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`H4F42HB3`)
- 발행일: 2026-08-07T15:44:12Z
- 저자: Haoning Wang, Mingxun Zhang, Chenyue Yu, Yingjun Shang, Xia Hu, Guanchu Wang, Na Zou
- 식별자: `arxiv:2608.07346`

## 요약·초록

With the rapid advancement of large language models (LLMs), harnesses have become essential infrastructure for deploying agents across a wide range of domains. The fast-evolving harness ecosystem has also made rigorous capability evaluation increasingly important. However, efficiently building an end-to-end, systematic, and comprehensive evaluation pipeline remains a significant challenge. To address this challenge, we introduce $A^2E$ (Agent Auditing Engine), an end-to-end evaluation engine designed for agent harnesses. $A^2E$ leverages our newly proposed Agent Task Protocol (ATP) to enable the rapid integration of evaluation tasks with different harnesses. Through an automatically instrumented Monitor, it captures and generates standardized execution traces during experiments. In the Evaluation stage, $A^2E$ systematically assesses harness capabilities using a suite of multidimensional metrics. Compared with correctness alone, these metrics provide a more fine-grained characterization of differences among harnesses in execution efficiency, tool use, task planning, and error recovery. Experiments conducted with $A^2E$ further reveal that model-harness combinations exhibit substantial performance variation across different types of tasks, and that no single combination consistently outperforms all others across every task. These findings not only demonstrate the necessity of systematic evaluation but also provide useful guidance for the co-evolving of models and harnesses. Our code is available at https://github.com/datamllab/A2E.

## 내 메모


