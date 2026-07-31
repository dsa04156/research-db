---
type: research-source
item_id: 34
title: "Conformal Changepoint Localization and Root Cause Analysis with Corrupted Observations"
source: "arxiv"
published: "2026-07-29T05:16:59Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26481"
url: "https://arxiv.org/abs/2607.26481v1"
generated_by: codex-research-db
aliases:
  - "Conformal Changepoint Localization and Root Cause Analysis with Corrupted Observations"
topics:
  - "ai-agents"
---

# Conformal Changepoint Localization and Root Cause Analysis with Corrupted Observations

[원문 열기](https://arxiv.org/abs/2607.26481v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6D4S4CET`)
- 발행일: 2026-07-29T05:16:59Z
- 저자: Seunghun Yu, Meiyi Zhu, Petar Popovski, Joonhyuk Kang, Osvaldo Simeone
- 식별자: `arxiv:2607.26481`

## 요약·초록

Detecting when the statistical behavior of an engineered system changes, and identifying which component is responsible, are core problems in the monitoring of telecommunication networks, robotic platforms, security infrastructure, and multi-agent systems. In safety- and mission-critical deployments, such decisions must be accompanied by statistical reliability guarantees rather than by point estimates alone. Conformal changepoint localization (CONCH) and conformal root cause analysis (CROC) meet this need by returning confidence sets that contain the true changepoint, or the true root-cause stream, with a user-specified probability, without parametric assumptions on the data-generating process. In practice, however, observations are frequently corrupted, e.g., by outliers, sensor faults, or adversarial perturbations. While the finite-sample coverage of these procedures is preserved under contamination, the resulting confidence sets can become uninformatively large. Adopting a Huber-type contamination model, this paper proposes weighted CONCH (W-CONCH) and weighted CROC (W-CROC), which downweight observations that are likely to be corrupted with the goal of reducing confidence set size when data may be corrupted. The weighting mechanism, derived from a formal bound on the unknown corrupted data densities, leverages pre-existing second-order classifier-based uncertainty signals, such as those produced by evidential deep learning or Bayesian learning. W-CONCH and W-CROC are further generalized by introducing a meta-learning procedure for the weights that optimizes a differentiable surrogate of the confidence set size. Experiments on image-based and real-world changepoint and root-cause benchmarks show that uncertainty-based weighting substantially reduces confidence set size while maintaining the target coverage.

## 내 메모


