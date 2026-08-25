---
type: research-source
item_id: 2204
title: "A closed-loop authentication-detection security framework for edge computing environments integrating trusted computing and distilled pre-trained language models"
source: "openalex"
published: "2026-08-21"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-66120-0"
url: "https://doi.org/10.1038/s41598-026-66120-0"
generated_by: codex-research-db
aliases:
  - "A closed-loop authentication-detection security framework for edge computing environments integrating trusted computing and distilled pre-trained language models"
topics:
  - "edge-computing"
---

# A closed-loop authentication-detection security framework for edge computing environments integrating trusted computing and distilled pre-trained language models

[원문 열기](https://doi.org/10.1038/s41598-026-66120-0)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`9ERFUMBR`)
- 발행일: 2026-08-21
- 저자: J Y Zhao, Chia S. LIM, Rui Wu, ﻿Lei Shi
- 식별자: `doi:10.1038/s41598-026-66120-0`

## 요약·초록

Edge computing environments hosting tens of thousands of nodes face concurrent threats including node spoofing, data tampering, and distributed denial-of-service attacks, yet existing security solutions address authentication, intrusion detection, and resource scheduling in isolation. This paper proposes a closed-loop authentication-detection security framework integrating three tightly coupled modules. The Detection-Feedback-driven Adaptive Authentication module combines Trusted Platform Module hardware attestation with a Bayesian-decay composite trust metric and three-level adaptive credential verification. The Trust-Guided Distilled Multi-modal Intrusion Detection System applies contrastive knowledge distillation from SecureBERT to a lightweight student model with cross-modal attention fusion across network traffic, system log, and system-call streams, conditioned on trust scores received through the bidirectional Trust-Feedback Token channel. A MAB-UCB1 adaptive scheduler co-optimizes resource allocation across both workloads simultaneously, achieving 91.7% of the theoretical optimal cumulative reward by round 200 against a random baseline of 70.4%. Experiments spanning 20 comparison groups, 10 ablation conditions, 6 attack scenarios, 3 public datasets, node scales from 1,000 to 50,000, and 30 repeated trials with Wilcoxon and Friedman statistical validation confirm that the proposed framework demonstrates competitive performance across six performance dimensions captured by the Security Performance Utility score, including authentication latency of 239.4 ms at 10,000 nodes, detection F1-score of 0.968, mean resource utilization of 38.2%, and system stability of 0.871 under DDoS conditions, outperforming all evaluated baseline methods under the tested conditions with statistical significance.

## 내 메모


