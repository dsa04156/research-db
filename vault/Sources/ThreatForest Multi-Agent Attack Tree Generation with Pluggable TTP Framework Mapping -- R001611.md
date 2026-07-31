---
type: research-source
item_id: 1611
title: "ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping"
source: "arxiv"
published: "2026-07-29T23:46:23Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.27528"
url: "https://arxiv.org/abs/2607.27528v1"
generated_by: codex-research-db
aliases:
  - "ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping"
topics:
  - "ai-agents"
---

# ThreatForest: Multi-Agent Attack Tree Generation with Pluggable TTP Framework Mapping

[원문 열기](https://arxiv.org/abs/2607.27528v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4SJM6P56`)
- 발행일: 2026-07-29T23:46:23Z
- 저자: Cristian Leo, Anton Dykyi, Danny Cortegaca, Daniel Begimher, Prakash Jha
- 식별자: `arxiv:2607.27528`

## 요약·초록

Threat modeling is essential for secure software development, yet manual analysis of cloud-native architectures is slow and demands scarce security expertise. We present ThreatForest, a multi-agent system that generates structured attack trees from source code repositories, maps attack steps to adversary tactics, techniques, and procedures (TTPs) from a pluggable set of frameworks (MITRE ATT&CK, CAPEC, and cloud-specific threat matrices), and synthesizes actionable mitigations. ThreatForest decomposes threat modeling into a multi-stage agent pipeline -- repository analysis, context refinement, threat generation, parallel attack-tree construction with TTP mapping and mitigation synthesis, and report generation -- orchestrated as a directed graph with deterministic verification gates, bounded retries, and three human-in-the-loop validation points. A domain-specific sentence-transformer maps each attack step to candidate techniques by cosine similarity; we show empirically that this embedding stage, not the surrounding pipeline, is the dominant accuracy bottleneck. We evaluate ThreatForest across seven application domains on a sixteen-dimension rubric, scored by a panel of independent LLM raters with an adversarial verification pass and expert review. Panel-measured quality reaches 0.63-0.68 (on a 0-1 scale) for threat statements, attack trees, and mitigations, but only 0.29 for embedding-only TTP mapping -- a gap stable across all seven domains that isolates the binding constraint. A controlled single-call baseline on the same model more than doubles mapping defensibility, pinning the limitation on the embedding encoder rather than the multi-agent design. To our knowledge, ThreatForest is the first end-to-end system that turns a code repository into TTP-mapped attack trees with evidence-based mitigations across adversary frameworks, with a reusable framework for benchmarking such systems.

## 내 메모


