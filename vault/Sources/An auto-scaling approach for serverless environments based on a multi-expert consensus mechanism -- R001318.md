---
type: research-source
item_id: 1318
title: "An auto-scaling approach for serverless environments based on a multi-expert consensus mechanism"
source: "openalex"
published: "2026-06-23"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1177/18761364261459585"
url: "https://doi.org/10.1177/18761364261459585"
generated_by: codex-research-db
aliases:
  - "An auto-scaling approach for serverless environments based on a multi-expert consensus mechanism"
topics:
  - "cloud-infrastructure"
---

# An auto-scaling approach for serverless environments based on a multi-expert consensus mechanism

[원문 열기](https://doi.org/10.1177/18761364261459585)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`MEIUXFR2`)
- 발행일: 2026-06-23
- 저자: Mobina Kashaniyan, Mehrdad Ashtiani, Amirhossein Ghassemi
- 식별자: `doi:10.1177/18761364261459585`

## 요약·초록

Serverless computing offers automatic resource management and pay-per-use execution, but autoscaling remains difficult due to cold-start latency, inter-function dependencies, and highly dynamic workloads. Many existing approaches scale functions independently or rely on a single predictor, which can reduce robustness and cost efficiency. We present a dependency-aware autoscaling framework that unifies bottleneck identification, short-horizon demand forecasting, and cost-aware control in an end-to-end pipeline. We model applications as directed dependency graphs and prioritize high-impact functions using degree centrality. For these bottlenecks, near-term demand is predicted using lightweight supervised models, whose outputs are fused via a performance-weighted probabilistic ensemble inspired by Bayesian model averaging to improve stability under workload variability. The controller also accounts for cold starts and filters candidate actions through a cost-comparison mechanism to balance latency and operational efficiency. Experiments on real workload traces show improved prediction accuracy and more stable scaling decisions than representative baselines; supervised forecasting also consistently outperforms unsupervised clustering for generating autoscaling actions. The primary contribution is a practical system-level design that integrates dependency analysis, ensemble-based prediction, and cost-aware decision-making for robust serverless autoscaling.

## 내 메모


