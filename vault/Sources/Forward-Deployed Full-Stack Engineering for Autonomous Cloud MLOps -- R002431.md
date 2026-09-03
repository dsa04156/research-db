---
type: research-source
item_id: 2431
title: "Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps"
source: "arxiv"
published: "2026-08-30T07:13:10Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.29615"
url: "https://arxiv.org/abs/2608.29615v1"
generated_by: codex-research-db
aliases:
  - "Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps"
topics:
  - "self-evolving-harness"
---

# Forward-Deployed Full-Stack Engineering for Autonomous Cloud MLOps

[원문 열기](https://arxiv.org/abs/2608.29615v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZKKFXGUI`)
- 발행일: 2026-08-30T07:13:10Z
- 저자: Sagar Srinivas Sakhinana, Venkataramana Runkana
- 식별자: `arxiv:2608.29615`

## 요약·초록

Across industries, machine-learning systems support applications ranging from prediction and anomaly detection to forecasting, optimization, and scheduling, yet operationalizing these systems requires coordinating application development, model pipelines, cloud infrastructure, security, deployment, monitoring, retraining, recovery, and rollback. We present an evidence-gated multi-agent framework for transforming a natural-language MLOps cloud engineering task into a verified repository and operational cloud deployment. The framework combines graph engineering, loop engineering, and agent harness engineering. A stateful Graph Orchestrator coordinates specialized agents for repository generation, review, execution, verification, release, and monitoring while governing workflow dependencies, evidence gates, retry bounds, recovery paths, and termination. Consequential lifecycle transitions proceed only when their required predicates are supported by verifiable execution or runtime evidence. Verification failures activate bounded reflection, repair, and re-verification, while runtime evidence of failure, drift, degradation, or policy violation can trigger bounded adaptation, recovery, or rollback. Agent harness engineering constrains repository generation, review, and repair, artifact execution, and cloud operations through controlled capabilities and isolated execution environments. We realize the framework on Google Cloud Platform and evaluate repository completeness, controlled execution, evidence-gated transitions, cloud promotion, and bounded recovery. Our experimental results show that the framework prevents unsupported lifecycle transitions and drives each run toward either a verified operational deployment or an auditable terminal failure.

## 내 메모


