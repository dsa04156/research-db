---
type: research-source
item_id: 1148
title: "Incentives and Evidence in Learned Service Orchestration"
source: "arxiv"
published: "2026-06-15T10:57:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.16555"
url: "https://arxiv.org/abs/2606.16555v1"
generated_by: codex-research-db
aliases:
  - "Incentives and Evidence in Learned Service Orchestration"
topics:
  - "kubernetes"
---

# Incentives and Evidence in Learned Service Orchestration

[원문 열기](https://arxiv.org/abs/2606.16555v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4HU8GV58`)
- 발행일: 2026-06-15T10:57:10Z
- 저자: Syed Izhan Khilji, Alireza Furutanpey, Schahram Dustdar
- 식별자: `arxiv:2606.16555`

## 요약·초록

Reinforcement learning for service orchestration has been the subject of sustained research for over a decade, yet it is not used in production at scale. The usual explanation is that learned controllers degrade under delayed and noisy telemetry, workload shifts, and uncontrolled tenants. We test whether existing evidence supports that explanation. We evaluate three highly influential RL-based orchestration systems spanning resource allocation, DAG scheduling, and autoscaling, using pre-registered predictions about comparative degradation under production-relevant perturbations and paired inference with family-wise error correction. Across the tests, most predicted performance reversals do not occur. Diagnostic analyses show that these outcomes often reflect comparator collapse, artefact limitations, or evaluation choices rather than evidence that learned controllers tolerate the perturbations. One apparent advantage under observation lag is roughly fortyfold compared to a Kubernetes HPA-equivalent controller. Another widely cited result cannot be reconstructed from its released artefact, and the strongest reproducible margin is far smaller than the published results. Conclusions also reverse under changes in perturbation magnitude and evaluation mode. Based on these results and broader patterns in the literature, we identify an institutional problem. Publication and review incentives favour benchmark gains against convenient comparators, even when those gains provide little evidence of deployment performance. We argue that the problem is not solely technical. Rather, it is institutional, so learned orchestration needs production-grade comparators, registered perturbation models, separate operational metrics, and publication criteria that reward reproducible operational evidence. Without these changes, the literature can grow without establishing whether learning improves orchestration.

## 내 메모


