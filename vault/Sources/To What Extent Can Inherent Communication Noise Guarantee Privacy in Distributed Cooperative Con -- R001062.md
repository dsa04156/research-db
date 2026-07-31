---
type: research-source
item_id: 1062
title: "To What Extent Can Inherent Communication Noise Guarantee Privacy in Distributed Cooperative Control?"
source: "arxiv"
published: "2026-07-28T10:52:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25564"
url: "https://arxiv.org/abs/2607.25564v1"
generated_by: codex-research-db
aliases:
  - "To What Extent Can Inherent Communication Noise Guarantee Privacy in Distributed Cooperative Control?"
topics:
  - "ai-agents"
---

# To What Extent Can Inherent Communication Noise Guarantee Privacy in Distributed Cooperative Control?

[원문 열기](https://arxiv.org/abs/2607.25564v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JWH3T9IM`)
- 발행일: 2026-07-28T10:52:32Z
- 저자: Yuwen Ma, Sarah Spurgeon, Tao Li, Boli Chen
- 식별자: `arxiv:2607.25564`

## 요약·초록

This paper proposes a differentially private distributed cooperative control scheme for multi-agent systems (MAS). Unlike conventional approaches that actively inject artificial noise for privacy protection, this work investigates whether inherent communication noise can itself serve as a natural privacy mechanism. A physically motivated communication-noise model is developed for mobile MAS by incorporating transmitter perturbation, receiver noise, path-loss attenuation, and log-normal shadowing. The resulting effective noise variance depends on inter-agent state differences, thereby capturing the distance-dependent signal perturbation arising in practice. Based on this model, a distributed finite-horizon Linear Quadratic Regulator (LQR) mechanism is designed to achieve formation tracking while protecting agents' private control preferences. Rather than protecting the full local cost function, the proposed privacy formulation focuses on the ratio of the LQR weighting matrices, which captures the trade-off between tracking accuracy and control effort when the quadratic cost structure is publicly known. A set-theoretic sensitivity analysis shows that this weighting-ratio adjacency formulation yields less conservative privacy bounds than gradient-based protection under the considered addition/removal adjacency relation. Theoretical analysis demonstrates that, under suitable design conditions, the proposed mechanism provides bounded cumulative (ε,δ)-differential privacy guarantees for the weighting ratios over an infinite horizon without artificial noise injection. Meanwhile, the cooperative tracking error is shown to converge almost surely and in mean square to a finite random limit, with its expectation remaining bounded. Numerical examples validate the theoretical results and illustrate the resulting privacy-performance trade-off.

## 내 메모


