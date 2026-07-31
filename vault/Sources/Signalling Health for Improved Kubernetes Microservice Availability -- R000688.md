---
type: research-source
item_id: 688
title: "Signalling Health for Improved Kubernetes Microservice Availability"
source: "arxiv"
published: "2025-07-02T21:28:30Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.02158"
url: "https://arxiv.org/abs/2507.02158v1"
generated_by: codex-research-db
aliases:
  - "Signalling Health for Improved Kubernetes Microservice Availability"
topics:
  - "kubernetes"
---

# Signalling Health for Improved Kubernetes Microservice Availability

[원문 열기](https://arxiv.org/abs/2507.02158v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GWS3INGA`)
- 발행일: 2025-07-02T21:28:30Z
- 저자: Jacob Roberts, Blair Archibald, Phil Trinder
- 식별자: `arxiv:2507.02158`

## 요약·초록

Microservices are often deployed and managed by a container orchestrator that can detect and fix failures to maintain the service availability critical in many applications. In Poll-based Container Monitoring (PCM), the orchestrator periodically checks container health. While a common approach, PCM requires careful tuning, may degrade service availability, and can be slow to detect container health changes. An alternative is Signal-based Container Monitoring (SCM), where the container signals the orchestrator when its status changes. We present the design, implementation, and evaluation of an SCM approach for Kubernetes and empirically show that it has benefits over PCM, as predicted by a new mathematical model. We compare the service availability of SCM and PCM over six experiments using the SockShop benchmark. SCM does not require that polling intervals are tuned, and yet detects container failure 86\% faster than PCM and container readiness in a comparable time with limited resource overheads. We find PCM can erroneously detect failures, and this reduces service availability by 4\%. We propose that orchestrators offer SCM features for faster failure detection than PCM without erroneous detections or careful tuning.

## 내 메모


