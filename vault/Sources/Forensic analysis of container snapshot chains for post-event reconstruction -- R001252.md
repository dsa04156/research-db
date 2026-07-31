---
type: research-source
item_id: 1252
title: "Forensic analysis of container snapshot chains for post-event reconstruction"
source: "openalex"
published: "2026-06-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1016/j.fsidi.2026.302114"
url: "https://doi.org/10.1016/j.fsidi.2026.302114"
generated_by: codex-research-db
aliases:
  - "Forensic analysis of container snapshot chains for post-event reconstruction"
topics:
  - "kubernetes"
---

# Forensic analysis of container snapshot chains for post-event reconstruction

[원문 열기](https://doi.org/10.1016/j.fsidi.2026.302114)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`RCWNPSSV`)
- 발행일: 2026-06-01
- 저자: Radostin Stoyanov, Lorena Goldoni, Adrian Reber, Christopher Hargreaves, Rodrigo Bruno
- 식별자: `doi:10.1016/j.fsidi.2026.302114`

## 요약·초록

Container orchestration platforms have become a crucial part of the cloud-native infrastructure for deploying modern applications. The highly dynamic and ephemeral nature of these environments, however, introduces new challenges for digital forensics: malicious code often runs entirely in memory and vanishes when the container terminates, leaving no traces. The absence of forensic data can be just as dangerous as the malicious activity itself, preventing post-incident investigation and adequate response. In this paper, we propose Forensic Snapshot Chains (FSC) – a framework that transparently captures and preserves the state, configurations, and metadata of running containers. These snapshot artifacts allow investigators to accurately reconstruct and analyze the events during a security incident without impacting the running cluster. To achieve this, FSC leverages memory-tracking mechanisms inspired by live-migration optimization techniques that enable high-frequency snapshot capture when a security alert is triggered, while minimizing performance and storage overhead. Our evaluation with real-world cloud-native workloads demonstrates that FSC, with minimal performance overhead, enables accurate temporal reconstruction of memory-resident malicious activity derived from container snapshot chains under both stealthy execution and active attack scenarios.

## 내 메모


