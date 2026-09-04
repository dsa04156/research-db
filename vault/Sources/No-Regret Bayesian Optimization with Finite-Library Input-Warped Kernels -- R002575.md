---
type: research-source
item_id: 2575
title: "No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels"
source: "arxiv"
published: "2026-09-02T16:04:07Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.02993"
url: "https://arxiv.org/abs/2609.02993v1"
generated_by: codex-research-db
aliases:
  - "No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels"
topics:
  - "ai-agents"
---

# No-Regret Bayesian Optimization with Finite-Library Input-Warped Kernels

[원문 열기](https://arxiv.org/abs/2609.02993v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-02T16:04:07Z
- 저자: Edvin Ketabati Augustinsson, Robert A. Bridges
- 식별자: `arxiv:2609.02993`

## 요약·초록

Gaussian-process Bayesian optimization (GP-BO) excels at black-box optimization of costly functions, e.g., hyperparameter optimization (HPO) and multi-agent system (MAS) design. Convergence-rate guarantees exist for select methods, notably GP upper confidence bound (GP-UCB), but require a fixed kernel. Critically, the kernel encodes how input proximity affects objective value similarity. When raw coordinates poorly match this geometry - as with log-scaled hyperparameters or localized peaks - input warping can greatly improve sample efficiency, yet known GP-UCB proofs require a fixed kernel. We propose Finite-Library Input-Warped Bayesian Optimization (FLIWBO), which selects warps from a finite library of smooth input maps by any history-dependent rule. It adapts the input geometry to accelerate learning while retaining high-probability convergence guarantees under mild hypotheses, with an explicit $\sqrt(N_\varepsilon)$ library-size cost. Controlled diagnostics show that finite-library warping repairs planted geometry mismatches and identify FLIWBO failure cases. Across four repeated benchmarks - warped synthetic objectives, a confidence-fence trap, and Fashion-MNIST HPO - FLIWBO-UCB beats raw-coordinate GP-UCB under misspecified geometry, escapes traps that defeat even oracle-warp expected improvement, and recovers much of the gain from manual log scaling, while leading the tested methods that admit a matching regret guarantee. A 20-dimensional MAS design study further shows feasibility under costly noisy evaluations. Code for experiments is available: https://github.com/edvin-ketabati/bogp-paper-experiments.

## 내 메모


