---
type: research-source
item_id: 917
title: "FedSKC: Federated Learning with Non-IID Data via Structural Knowledge Collaboration"
source: "arxiv"
published: "2025-05-25T05:24:49Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.18981"
url: "https://arxiv.org/abs/2505.18981v1"
generated_by: codex-research-db
aliases:
  - "FedSKC: Federated Learning with Non-IID Data via Structural Knowledge Collaboration"
topics:
  - "edge-computing"
---

# FedSKC: Federated Learning with Non-IID Data via Structural Knowledge Collaboration

[원문 열기](https://arxiv.org/abs/2505.18981v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UUQ8GWZH`)
- 발행일: 2025-05-25T05:24:49Z
- 저자: Huan Wang, Haoran Li, Huaming Chen, Jun Yan, Lijuan Wang, Jiahua Shi, Shiping Chen, Jun Shen
- 식별자: `arxiv:2505.18981`

## 요약·초록

With the advancement of edge computing, federated learning (FL) displays a bright promise as a privacy-preserving collaborative learning paradigm. However, one major challenge for FL is the data heterogeneity issue, which refers to the biased labeling preferences among multiple clients, negatively impacting convergence and model performance. Most previous FL methods attempt to tackle the data heterogeneity issue locally or globally, neglecting underlying class-wise structure information contained in each client. In this paper, we first study how data heterogeneity affects the divergence of the model and decompose it into local, global, and sampling drift sub-problems. To explore the potential of using intra-client class-wise structural knowledge in handling these drifts, we thus propose Federated Learning with Structural Knowledge Collaboration (FedSKC). The key idea of FedSKC is to extract and transfer domain preferences from inter-client data distributions, offering diverse class-relevant knowledge and a fair convergent signal. FedSKC comprises three components: i) local contrastive learning, to prevent weight divergence resulting from local training; ii) global discrepancy aggregation, which addresses the parameter deviation between the server and clients; iii) global period review, correcting for the sampling drift introduced by the server randomly selecting devices. We have theoretically analyzed FedSKC under non-convex objectives and empirically validated its superiority through extensive experimental results.

## 내 메모


