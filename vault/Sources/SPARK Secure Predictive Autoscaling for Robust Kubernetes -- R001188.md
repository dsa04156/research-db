---
type: research-source
item_id: 1188
title: "SPARK: Secure Predictive Autoscaling for Robust Kubernetes"
source: "arxiv"
published: "2026-03-27T05:23:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.26833"
url: "https://arxiv.org/abs/2603.26833v1"
generated_by: codex-research-db
aliases:
  - "SPARK: Secure Predictive Autoscaling for Robust Kubernetes"
topics:
  - "kubernetes"
---

# SPARK: Secure Predictive Autoscaling for Robust Kubernetes

[원문 열기](https://arxiv.org/abs/2603.26833v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UKVRMCPP`)
- 발행일: 2026-03-27T05:23:10Z
- 저자: Zhijun Jiang, Amin Milani Fard
- 식별자: `arxiv:2603.26833`

## 요약·초록

Achieving high availability and robust security in Kubernetes requires more than reactive scaling and standard perimeter firewalls. Traditional autoscalers, such as HPA, often fail to react quickly to traffic spikes and cannot distinguish between legitimate flash crowds and DDoS attacks. We present an open-source toolchain to provide a traffic-aware autoscaling approach that utilizes an eBPF-based networking layer to enforce security policies at the kernel level while orchestrating scaling decisions based on predictive models. Our results demonstrate that the predictive approach reduces timeout errors by 32% during sudden traffic surges compared to standard reactive scaling, while ensuring immediate network convergence and layer 7 security isolation for newly scaled pods.

## 내 메모


