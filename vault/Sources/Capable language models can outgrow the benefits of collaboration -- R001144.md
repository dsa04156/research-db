---
type: research-source
item_id: 1144
title: "Capable language models can outgrow the benefits of collaboration"
source: "openalex"
published: "2026-07-24"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1038/s42256-026-01268-y"
url: "https://doi.org/10.1038/s42256-026-01268-y"
generated_by: codex-research-db
aliases:
  - "Capable language models can outgrow the benefits of collaboration"
topics:
  - "ai-agents"
---

# Capable language models can outgrow the benefits of collaboration

[원문 열기](https://doi.org/10.1038/s42256-026-01268-y)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`2SXTJFSN`)
- 발행일: 2026-07-24
- 저자: Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Liu Y, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu
- 식별자: `doi:10.1038/s42256-026-01268-y`

## 요약·초록

Agents, language model-based systems that can reason, plan and act with tools to accomplish tasks, are widely deployed, yet it remains unclear when multi-agent coordination outperforms a strong single agent. Here we conduct a controlled experiment that holds task prompts, tools and compute budgets constant while varying only coordination structure and model capability. Across 260 configurations spanning six benchmarks, five architectures and three LLM families, we derive a predictive model using empirical coordination metrics. Across benchmarks, single-agent baseline performance emerges as the most robust predictor of whether coordination improves or decreases performance. In particular, we identify an empirical capability-saturation threshold beyond which additional agents are unlikely to improve performance. This threshold correctly predicts the effect of multi-agent coordination on performance in 94% of validation configurations on SWE-bench Verified and Terminal-Bench. We therefore interpret this threshold as a practical selection rule rather than a universal scaling principle. A second effect, baseline-scaled error amplification, survives cluster-robust inference (Probust = 0.030) and supports the failure-mode taxonomy. The fitted model achieves cross-validated R2 = 0.373 (0.413 with a task-grounded capability metric) and selects the best architecture in 87% of held-out configurations. These results provide a quantitative framework for within-domain architecture selection and for estimating when multi-agent coordination is likely to improve performance or add overhead. A controlled study of large language model agents across 260 configurations shows when multi-agent collaboration helps or hurts performance, and introduces a predictive model that selects the best architecture in 87% of held-out within-domain configurations.

## 내 메모


