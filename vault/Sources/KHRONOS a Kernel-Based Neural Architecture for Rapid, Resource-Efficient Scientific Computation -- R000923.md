---
type: research-source
item_id: 923
title: "KHRONOS: a Kernel-Based Neural Architecture for Rapid, Resource-Efficient Scientific Computation"
source: "arxiv"
published: "2025-05-19T16:29:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.13315"
url: "https://arxiv.org/abs/2505.13315v2"
generated_by: codex-research-db
aliases:
  - "KHRONOS: a Kernel-Based Neural Architecture for Rapid, Resource-Efficient Scientific Computation"
topics:
  - "edge-computing"
---

# KHRONOS: a Kernel-Based Neural Architecture for Rapid, Resource-Efficient Scientific Computation

[원문 열기](https://arxiv.org/abs/2505.13315v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`H5JC9XAT`)
- 발행일: 2025-05-19T16:29:07Z
- 저자: Reza T. Batley, Sourav Saha
- 식별자: `arxiv:2505.13315`

## 요약·초록

Contemporary models of high dimensional physical systems are constrained by the curse of dimensionality and a reliance on dense data. We introduce KHRONOS (Kernel Expansion Hierarchy for Reduced Order, Neural Optimized Surrogates), an AI framework for model based, model free and model inversion tasks. KHRONOS constructs continuously differentiable target fields with a hierarchical composition of per-dimension kernel expansions, which are tensorized into modes and then superposed. We evaluate KHRONOS on a canonical 2D, Poisson equation benchmark: across 16 to 512 degrees of freedom (DoFs), it obtained L_2-square errors of 5e-4 down to 6e-11. This represents a greater than 100-fold gain over Kolmogorov Arnold Networks (which itself reports a 100 times improvement on MLPs/PINNs with 100 times fewer parameters) when controlling for the number of parameters. This also represents a 1e6-fold improvement in L_2-square error compared to standard linear FEM at comparable DoFs. Inference complexity is dominated by inner products, yielding sub-millisecond full-field predictions that scale to an arbitrary resolution. For inverse problems, KHRONOS facilitates rapid, iterative level set recovery in only a few forward evaluations, with sub-microsecond per sample latency. KHRONOS's scalability, expressivity, and interpretability open new avenues in constrained edge computing, online control, computer vision, and beyond.

## 내 메모


