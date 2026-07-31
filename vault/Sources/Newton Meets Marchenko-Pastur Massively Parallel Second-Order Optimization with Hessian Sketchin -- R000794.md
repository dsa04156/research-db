---
type: research-source
item_id: 794
title: "Newton Meets Marchenko-Pastur: Massively Parallel Second-Order Optimization with Hessian Sketching and Debiasing"
source: "arxiv"
published: "2024-10-02T09:38:04Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2410.01374"
url: "https://arxiv.org/abs/2410.01374v1"
generated_by: codex-research-db
aliases:
  - "Newton Meets Marchenko-Pastur: Massively Parallel Second-Order Optimization with Hessian Sketching and Debiasing"
topics:
  - "cloud-infrastructure"
---

# Newton Meets Marchenko-Pastur: Massively Parallel Second-Order Optimization with Hessian Sketching and Debiasing

[원문 열기](https://arxiv.org/abs/2410.01374v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VFQ5RWQQ`)
- 발행일: 2024-10-02T09:38:04Z
- 저자: Elad Romanov, Fangzhao Zhang, Mert Pilanci
- 식별자: `arxiv:2410.01374`

## 요약·초록

Motivated by recent advances in serverless cloud computing, in particular the "function as a service" (FaaS) model, we consider the problem of minimizing a convex function in a massively parallel fashion, where communication between workers is limited. Focusing on the case of a twice-differentiable objective subject to an L2 penalty, we propose a scheme where the central node (server) effectively runs a Newton method, offloading its high per-iteration cost -- stemming from the need to invert the Hessian -- to the workers. In our solution, workers produce independently coarse but low-bias estimates of the inverse Hessian, using an adaptive sketching scheme. The server then averages the descent directions produced by the workers, yielding a good approximation for the exact Newton step. The main component of our adaptive sketching scheme is a low-complexity procedure for selecting the sketching dimension, an issue that was left largely unaddressed in the existing literature on Hessian sketching for distributed optimization. Our solution is based on ideas from asymptotic random matrix theory, specifically the Marchenko-Pastur law. For Gaussian sketching matrices, we derive non asymptotic guarantees for our algorithm which are essentially dimension-free. Lastly, when the objective is self-concordant, we provide convergence guarantees for the approximate Newton's method with noisy Hessians, which may be of independent interest beyond the setting considered in this paper.

## 내 메모


