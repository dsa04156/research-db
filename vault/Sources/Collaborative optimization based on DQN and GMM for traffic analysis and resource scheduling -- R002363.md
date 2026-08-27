---
type: research-source
item_id: 2363
title: "Collaborative optimization based on DQN and GMM for traffic analysis and resource scheduling"
source: "crossref"
published: "2026-08-28"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "doi:10.1108/ijwis-05-2026-0237"
url: "https://doi.org/10.1108/ijwis-05-2026-0237"
generated_by: codex-research-db
aliases:
  - "Collaborative optimization based on DQN and GMM for traffic analysis and resource scheduling"
topics:
  - "cloud-infrastructure"
---

# Collaborative optimization based on DQN and GMM for traffic analysis and resource scheduling

[원문 열기](https://doi.org/10.1108/ijwis-05-2026-0237)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `crossref`
- 검토 상태: `pending`
- 발행일: 2026-08-28
- 저자: Zhengxu Chen, Xiaoyan Sun, Weiqiang Feng, Yunbiao Zhang
- 식별자: `doi:10.1108/ijwis-05-2026-0237`

## 요약·초록

Purpose With the rapid development of 5G, the Internet of Things, cloud computing and edge computing, modern network environments have become increasingly dynamic, heterogeneous and complex, posing significant challenges to traffic understanding and resource management. Because traffic analysis and resource scheduling are inherently coupled, a major challenge lies in jointly modeling traffic perception and adaptive decision-making within a unified framework. This paper aims to address the challenges of high-dimensional traffic, encryption and strong dynamics in modern networks. Design/methodology/approach This paper proposes deep Q-network with Gaussian mixture model cooperative optimization (DQN-GCO), a collaborative optimization framework integrating Gaussian mixture model (GMM)-based probabilistic traffic modeling with DQN-based adaptive resource scheduling. Specifically, GMM is used to capture latent traffic distributions and generate posterior probability vectors, which are then used as compact and informative state representations for DQN. Findings The proposed framework improves state abstraction, preserves uncertainty information and enhances policy learning stability. Extensive experiments on real-world traffic data and a simulated software-defined networking environment demonstrate that DQN-GCO consistently outperforms traditional methods and representative baselines across multiple evaluation metrics. Originality/value Unlike traditional hard clustering methods (e.g. K-means), the proposed model avoids strong assumptions about cluster geometry and data distribution. Instead, it adopts the Gaussian mixture MRefer to previous literatureodel to conduct probabilistic soft clustering of network traffic, enabling the model to capture multimodal, nonconvex and overlapping traffic distributions. The posterior probability vector produced by the GMM is used as the DQN state representation, which maps high-dimensional traffic features into a compact semantic state space. This design improves convergence speed, decision accuracy and policy robustness.

## 내 메모
