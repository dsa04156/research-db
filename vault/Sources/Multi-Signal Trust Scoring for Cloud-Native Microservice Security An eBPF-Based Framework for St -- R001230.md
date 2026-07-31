---
type: research-source
item_id: 1230
title: "Multi-Signal Trust Scoring for Cloud-Native Microservice Security: An eBPF-Based Framework for Stealth Attack Detection Without Sidecar Proxies"
source: "openalex"
published: "2026-07-03"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.21275/sr26629100308"
url: "https://doi.org/10.21275/sr26629100308"
generated_by: codex-research-db
aliases:
  - "Multi-Signal Trust Scoring for Cloud-Native Microservice Security: An eBPF-Based Framework for Stealth Attack Detection Without Sidecar Proxies"
topics:
  - "kubernetes"
---

# Multi-Signal Trust Scoring for Cloud-Native Microservice Security: An eBPF-Based Framework for Stealth Attack Detection Without Sidecar Proxies

[원문 열기](https://doi.org/10.21275/sr26629100308)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`PHVKSGFX`)
- 발행일: 2026-07-03
- 저자: Umashankara Kalaiah
- 식별자: `doi:10.21275/sr26629100308`

## 요약·초록

Cloud-native microservice environments generate extensive east-west service communication that existing eBPF-based security tools-including Cilium Tetragon and Falco-cannot adequately detect stealth trust-boundary violations due to their reliance on single-signal detection. This work proposes Context-Aware eBPF Trust Boundary Evaluation (CA-eBPF), a sidecar-less detection framework that computes adaptive trust scores by continuously correlating five contextual dimensions-workload identity, behavioral consistency, network telemetry, process integrity, and distributed trace correlation-from kernel-level eBPF telemetry without requiring payload decryption. The framework is evaluated against four single- and dual-signal baselines through a controlled simulation study of 5,000 communication events, complemented by a real-cluster validation on AWS EC2 in which Cilium Tetragon captured 58,186 genuine kernel-level eBPF events confirming framework deployability and telemetry capture. In the simulation study, CA-eBPF achieved an F1-score of 92.42%, accuracy of 96.24%, and AUC-ROC of 0.995, with stealth attack detection of 89.20% compared to 65.20% for the best-performing baseline-a 24 percentage-point improvement attributable to multi-signal contextual scoring. An integrated eBPF-based enforcement design is presented; end-to-end enforcement validation and quantitative performance benchmarking against sidecar-based service meshes are identified as future work.

## 내 메모


