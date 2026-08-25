---
type: research-source
item_id: 2234
title: "The Lazy Pod That Lies: Deferred Cost and Failure Semantics of Lazy Container Image Pulling for Model Serving on Kubernetes"
source: "kurate"
published: "2026-08-19T19:50:56Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.19412"
url: "http://arxiv.org/abs/2608.19412v1"
generated_by: codex-research-db
aliases:
  - "The Lazy Pod That Lies: Deferred Cost and Failure Semantics of Lazy Container Image Pulling for Model Serving on Kubernetes"
topics:
  - "kubernetes"
---

# The Lazy Pod That Lies: Deferred Cost and Failure Semantics of Lazy Container Image Pulling for Model Serving on Kubernetes

[원문 열기](http://arxiv.org/abs/2608.19412v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`BBFH8ICP`)
- 발행일: 2026-08-19T19:50:56Z
- 저자: Georgii Kliukovkin
- 식별자: `arxiv:2608.19412`

## 요약·초록

Lazy container-image pulling promises to eliminate the dominant cost of starting a model-serving pod by mounting the image immediately and fetching content on demand. We evaluate this promise for model delivery on Kubernetes, using KServe with two production lazy-pulling systems -- eStargz/stargz-snapshotter and AWS SOCI -- against eager baselines, on artifacts from 2 to 140 GB including real fp16 weights. Lazy pulling delivers its headline: cold time-to-first-prediction becomes size-independent (16.9--17.6s, versus 24.5--573.0s eager). But the cost is deferred, not eliminated: a full read of a 14 GB model through the lazy mount takes 105.3s, slower than the 72.4s eager pull it replaced, and the two systems pay at opposite lifecycle ends (SOCI prefetches nearly the full image before Ready; eStargz defers nearly everything to first read). More consequentially, we characterize a failure mode eager pulling structurally cannot exhibit: under sustained legitimate reads with default configuration, the snapshotter's node-level cache exhausts its finite volume and already-running pods begin failing reads of model files. At the earliest stage of exhaustion, an instrumented serving pod passed every Kubernetes-visible and application-level check for 196s while its snapshotter was already logging real failures; under heavier pressure, 67--94% of model files fail, scaling monotonically with residual cache occupancy. A live pod self-heals if cache space is freed under it, but a snapshotter-daemon restart under a live pod leaves permanently stale file handles in a pod still reported Running. We derive placement, monitoring, and cache-sizing guidance for serving platforms and operators.

## 내 메모


