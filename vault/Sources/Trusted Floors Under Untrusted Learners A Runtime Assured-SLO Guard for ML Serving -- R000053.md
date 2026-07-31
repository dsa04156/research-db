---
type: research-source
item_id: 53
title: "Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving"
source: "arxiv"
published: "2026-07-10T21:35:48Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.09992"
url: "https://arxiv.org/abs/2607.09992v2"
generated_by: codex-research-db
aliases:
  - "Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving"
topics:
  - "kubernetes"
---

# Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving

[원문 열기](https://arxiv.org/abs/2607.09992v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`37P869HK`)
- 발행일: 2026-07-10T21:35:48Z
- 저자: Hsiu-Chi Tsai
- 식별자: `arxiv:2607.09992`

## 요약·초록

Modern ML serving increasingly lets learned, unverified components (routers, latency-SLO admitters, admit ladders) decide a tenant's quality of service; when one is wrong, the assured SLO can silently break, and the Kubernetes layers beneath (Kueue, DRA, the Gateway-API Inference Extension, GAIE) add cross-layer surprises. Rather than trust the learner to be right, we bound the damage a wrong one can do: a small trusted guard wraps the untrusted learner (learned proposes, the guard disposes). A tenant's assured-SLO obligation splits into two parts with different epistemics. Its safety projection, a per-class, per-window assured floor (with an optional drop rule, doom-sound only under an assumed service lower envelope), is a controllable obligation a guard enforces at runtime, holding it regardless of a learned admitter that is arbitrarily wrong within a bounded proposal interface. The admission floor is enforced structurally; given the stated assumptions, the service floor follows as a conditional response-time implication. Its aggregate obligation (the population tail-latency percentile) has no per-request enforcement point, so we treat it as a statistical residual and screen it. On real 2xV100 the guard (a Simplex-style assured-floor gate plus assured-first priority) holds assured-class miss 0.0 across every tested miscalibration of a learned admitter that, unguarded, misses 0.86-0.94; against a live deployment of the GAIE Flow Control, an injected mapping fault (emulating an untrusted mapper) flips the same assured requests from miss 0.0 to 1.0 (a mechanism-level trust-boundary test, not a head-to-head), while our guard reserves by the true class. As a Frontiers submission we evaluate the stance on commodity 2xV100 and a serving simulator, scoping datacenter scale, real-model Flow Control, and a closed worst-case theorem as the agenda.

## 내 메모


