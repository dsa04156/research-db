---
type: research-source
item_id: 3049
title: "Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems"
source: "arxiv"
published: "2026-09-21T12:15:28Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24474"
url: "https://arxiv.org/abs/2609.24474v1"
generated_by: codex-research-db
aliases:
  - "Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems"
topics:
  - "ai-agents"
---

# Mixed-integer flow formulations for motion planning and decision-making of networked multi-agent systems

[원문 열기](https://arxiv.org/abs/2609.24474v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T12:15:28Z
- 저자: Angelo Caregnato-Neto, Paul-Louis Delacour, Raf Van de Plas, Tamás Keviczky, Janito Vaqueiro Ferreira
- 식별자: `arxiv:2609.24474`

## 요약·초록

This work investigates the use of flow-based connectivity maintenance constraints in mixed-integer linear programming (MILP) trajectory planning and decision-making models for networked multi-agent systems (MAS). We integrate flow-based encodings for standard and k-hop connectivity into MILP multi-vehicle maneuvering models that are widely used alongside receding horizon planning strategies. Their necessity and sufficiency is demonstrated, guaranteeing full coverage of potential network topologies. The flow formulation for standard connectivity decreases the growth of the required inequality constraints from exponential to polynomial w.r.t. the size of the MAS when compared to the state-of-the-art subtour elimination (SEC) method. The flow-based k-hop connectivity constraints decrease the number of required binary variables and decouple its growth from the number of hops. However, the impact of these formulations in performance is not straightforward due to the introduction of a substantial number of continuous flow optimization variables and, in the case of k-hop connectivity, additional inequality constraints. We investigate this trade-off through a statistical evaluation of costs and optimization times using a conventional branch-and-bound commercial solver and trials performed with randomized environments for increasingly larger MAS. The results show that the flow formulation outperforms SEC in standard connectivity problems, enabling the solutions to be computed for larger MAS considering the imposed optimization time limit. The reduction in number of binary variables enabled by the k-hop flow formulations decreases the theoretical worst-case number of iterations required by the branch-and-bound algorithm to compute the global optimal solution. Our results show that this advantage did not translate into improvements in the average performance when compared to the baseline.

## 내 메모
