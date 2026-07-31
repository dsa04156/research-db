---
type: research-source
item_id: 324
title: "ScalO-RAN: Energy-aware Network Intelligence Scaling in Open RAN"
source: "arxiv"
published: "2023-12-08T15:24:26Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2312.05096"
url: "https://arxiv.org/abs/2312.05096v2"
generated_by: codex-research-db
aliases:
  - "ScalO-RAN: Energy-aware Network Intelligence Scaling in Open RAN"
topics:
  - "kubernetes"
---

# ScalO-RAN: Energy-aware Network Intelligence Scaling in Open RAN

[원문 열기](https://arxiv.org/abs/2312.05096v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HCZFEJUI`)
- 발행일: 2023-12-08T15:24:26Z
- 저자: Stefano Maxenti, Salvatore D'Oro, Leonardo Bonati, Michele Polese, Antonio Capone, Tommaso Melodia
- 식별자: `arxiv:2312.05096`

## 요약·초록

Network virtualization, software-defined infrastructure, and orchestration are pivotal elements in contemporary networks, yielding new vectors for optimization and novel capabilities. In line with these principles, O-RAN presents an avenue to bypass vendor lock-in, circumvent vertical configurations, enable network programmability, and facilitate integrated Artificial Intelligence (AI) support. Moreover, modern container orchestration frameworks (e.g., Kubernetes, Red Hat OpenShift) simplify the way cellular base stations, as well as the newly introduced RAN Intelligent Controllers (RICs), are deployed, managed, and orchestrated. While this enables cost reduction via infrastructure sharing, it also makes it more challenging to meet O-RAN control latency requirements, especially during peak resource utilization. To address this problem, we propose ScalO-RAN, a control framework rooted in optimization and designed as an O-RAN rApp that allocates and scales AI-based O-RAN applications (xApps, rApps, dApps) to: (i) abide by application-specific latency requirements, and (ii) monetize the shared infrastructure while reducing energy consumption. We prototype ScalO-RAN on an OpenShift cluster with base stations, RIC, and a set of AI-based xApps deployed as micro-services. We evaluate ScalO-RAN both numerically and experimentally. Our results show that ScalO-RAN can optimally allocate and distribute O-RAN applications within available computing nodes to accommodate even stringent latency requirements. More importantly, we show that scaling O-RAN applications is primarily a time-constrained problem rather than a resource-constrained one, where scaling policies must account for stringent inference time of AI applications, and not only how many resources they consume.

## 내 메모


