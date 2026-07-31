---
type: research-source
item_id: 1156
title: "Predicting Lakehouse Performance in Clouds: An Empirical Exploration of Query Runtime Variance"
source: "arxiv"
published: "2026-06-02T10:45:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.03464"
url: "https://arxiv.org/abs/2606.03464v1"
generated_by: codex-research-db
aliases:
  - "Predicting Lakehouse Performance in Clouds: An Empirical Exploration of Query Runtime Variance"
topics:
  - "kubernetes"
---

# Predicting Lakehouse Performance in Clouds: An Empirical Exploration of Query Runtime Variance

[원문 열기](https://arxiv.org/abs/2606.03464v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6IW49U8I`)
- 발행일: 2026-06-02T10:45:14Z
- 저자: James Nurdin, Wei Liu, Richard Mccreadie, Lauritz Thamsen
- 식별자: `arxiv:2606.03464`

## 요약·초록

Data analytics increasingly runs on distributed lakehouse systems, where platform operators must optimise monetary, resource, and environmental costs. Query Performance Prediction (QPP) helps to balance these costs and supports workload management techniques, such as adaptive resource scaling and low-carbon scheduling. However, runtimes in lakehouses can vary substantially, and the impact of runtime variance on QPP accuracy and workload orchestration has not previously been systematically studied for lakehouse systems. This paper addresses this gap by investigating the runtime variance observed for distributed lakehouse analytical queries and its impact on QPP. First, we quantify the run-to-run variance using Kubernetes deployments across three public clouds and one private cloud, spanning multiple database scales and three analytical benchmarks. Our results demonstrate that repeated executions of the same query can vary in runtime by nearly twofold. Second, we conduct a factor analysis study assessing key sources of this runtime variance such as data locality, co-tenant load, and caching effects. Third, we examine how variance influences state-of-the-art QPP models, revealing that addressing key sources of variance can reduce prediction error up to 80%. Finally, we demonstrate the downstream implications for low-carbon scheduling as an example of a workload management technique that relies on performance prediction, showing that accounting for runtime variance can lead to a significant reduction in carbon costs.

## 내 메모


