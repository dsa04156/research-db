---
type: research-source
item_id: 1772
title: "Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints"
source: "arxiv"
published: "2026-08-06T16:56:44Z"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "arxiv:2608.06265"
url: "https://arxiv.org/abs/2608.06265v1"
generated_by: codex-research-db
aliases:
  - "Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints"
topics:
  - "ai-agents"
---

# Improving the Realism of Synthetic Clinical Benchmarks Under Utility Constraints

[원문 열기](https://arxiv.org/abs/2608.06265v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-06T16:56:44Z
- 저자: Omid Bazgir, Md Nasir, Jacob Hoffman, Yang Yang, Manu Agrawal, Anusua Trivedi, Vinay Rao Dandin, Chris Gibbons, Christine Swisher
- 식별자: `arxiv:2608.06265`

## 요약·초록

Synthetic clinical benchmarks for enterprise AI agents can pass existing utility checks and still remain structurally unrealistic, especially in privacy-sensitive healthcare settings where operational data are hard to access. We study how to improve such benchmarks without breaking the downstream utility checks already used in practice. We formulate benchmark revision as utility-constrained realism improvement: dataset changes should increase realism while staying above an operational utility floor. We instantiate this idea on a care-gap benchmark derived from Synthea-generated patients exercised through demonstration electronic health record workflows and then processed by the same downstream pipeline as operational data. Realism is measured through missingness structure, simplicity, structural plausibility, and population alignment. The baseline benchmark is extremely thin: sampled-pair missingness is 79.44%, only 12.75% of rows are actionable, 38.94% of patients have zero actionable measures, and top-three token concentration reaches 100.0%. Two deterministic revisions improve these panels while remaining above the current utility floor, whereas a naive densification control preserves unrealistic templating. We further show that internal benchmark realism and source fidelity to an aggregate operational reference are related but distinct objectives. These results suggest that synthetic benchmark quality should be optimized explicitly, with utility treated as one constraint rather than as sufficient evidence of realism.

## 내 메모


