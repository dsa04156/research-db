---
type: research-source
item_id: 1381
title: "Heterogeneous Mean Field Game Framework for LEO Satellite-Assisted V2X Networks"
source: "arxiv"
published: "2026-04-01T08:27:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.00621"
url: "https://arxiv.org/abs/2604.00621v2"
generated_by: codex-research-db
aliases:
  - "Heterogeneous Mean Field Game Framework for LEO Satellite-Assisted V2X Networks"
topics:
  - "edge-computing"
---

# Heterogeneous Mean Field Game Framework for LEO Satellite-Assisted V2X Networks

[원문 열기](https://arxiv.org/abs/2604.00621v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HRHFR4WT`)
- 발행일: 2026-04-01T08:27:52Z
- 저자: Kangkang Sun, Jianhua Li, Xiuzhen Chen, Mingzhe Chen, Minyi Guo
- 식별자: `arxiv:2604.00621`

## 요약·초록

Coordinating mixed fleets of massive vehicles under stringent delay constraints is a central scalability bottleneck in next-generation mobile computing networks, especially when passenger cars, freight trucks, and autonomous vehicles share the same radio and multi-access edge computing (MEC) infrastructure. Heterogeneous mean field games (HMFG) are a principled framework for this setting, but a fundamental design question remains open: how many agent types should be used for a fleet of size $N$? The difficulty is a two-sided trade-off that existing theory does not resolve: using more types improves heterogeneity representation, but it reduces per-class sample size and weakens the mean-field approximation accuracy. This paper resolves that trade-off through an explicit $\varepsilon$-Nash error decomposition, a closed-form type-selection law, a heterogeneity-aware equilibrium solver, and a robust extension to time-varying LEO backhaul dynamics. For the 1D queue state space, the optimal type count satisfies $K^*(N)=Θ(N^{1/3})$; for the joint queue-channel model ($d=2$), the scaling becomes $K^*(N)=Θ(N^{1/5})$ with logarithmic correction. The unified formula $K^*(N)=Θ(N^{α/(α+β)})$ provides dimension-dependent design guidance, reducing type granularity to a principled, set-once system parameter rather than a per-deployment tuning burden. Experiments validate the 1D scaling law with empirical slope $0.334 \pm 0.004$, achieve $2.3\times$ faster PDHG convergence at $K=5$, and deliver up to $29.5\%$ lower delay and $60\%$ higher throughput than homogeneous baselines. Unlike model-free DRL methods whose training complexity scales with the state-action space, the proposed HMFG solver has per-iteration complexity $O(K^2 N_q N_t)$ independent of fleet size $N$, making it suitable for large-scale mobile edge computing deployment.

## 내 메모


