---
type: research-source
item_id: 1246
title: "An intelligent drug supply chain management and recommendation framework using blockchain and TRPO-driven multi-agent learning"
source: "openalex"
published: "2026-06-11"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-56991-8"
url: "https://doi.org/10.1038/s41598-026-56991-8"
generated_by: codex-research-db
aliases:
  - "An intelligent drug supply chain management and recommendation framework using blockchain and TRPO-driven multi-agent learning"
topics:
  - "ai-agents"
---

# An intelligent drug supply chain management and recommendation framework using blockchain and TRPO-driven multi-agent learning

[원문 열기](https://doi.org/10.1038/s41598-026-56991-8)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`R4CBAMQ9`)
- 발행일: 2026-06-11
- 저자: Shahrzad Bastani Alahabadi
- 식별자: `doi:10.1038/s41598-026-56991-8`

## 요약·초록

Pharmaceutical companies increasingly face difficulties in tracking products across the supply chain, enabling counterfeiters to introduce fake medicines that cause substantial economic losses and serious health risks. A mechanism capable of tracing and monitoring drug movement at every stage is therefore essential. Blockchain offers a promising foundation for secure and transparent supply chain tracking. This paper introduces a two-module framework. It integrates a blockchain-based drug supply chain management (DSCM) system with a multi-agent recommendation model driven by trust region policy optimization (TRPO). The first module employs a customized blockchain to continuously record, monitor, and verify drug movement within a simulated smart pharmaceutical environment. The second module is a sentiment analysis (SA) that operates with two TRPO agents in a blockchain-secured setting. To enhance policy performance, the TRPO agents incorporate entropy regularization. This setup specifically addresses key SA challenges, including handling unlabeled data, feature selection, and class imbalance mitigation. The first agent applies semi-supervised learning (SSL) with pseudo-labels on high-confidence unlabeled samples to expand the training set. The second agent performs SA, applies Shapley additive explanations (SHAP) for feature ranking, and uses reward mechanisms to improve performance on underrepresented classes. The framework was evaluated on two large real-world drug review datasets, Drugs.com and Druglib.com. For Drugs.com, the blockchain module achieved 3.015-second latency and 172.322 tps throughput, while the SA model reached 93.250% accuracy and 94.329% F-measure. For Druglib.com, latency was 2.930 s, throughput was 189.538 tps, accuracy was 95.192%, and F-measure was 96.257%. These results demonstrate the effectiveness of the framework in analyzing patient reviews. It successfully provides secure supply chain recording and sentiment-based insights within controlled experimental conditions.

## 내 메모


