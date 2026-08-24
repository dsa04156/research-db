---
type: research-source
item_id: 2193
title: "CUSTOS: Toward Forensic-Ready Zero Trust at the Capture-Containment Boundary"
source: "arxiv"
published: "2026-08-17T19:17:15Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.17068"
url: "https://arxiv.org/abs/2608.17068v2"
generated_by: codex-research-db
aliases:
  - "CUSTOS: Toward Forensic-Ready Zero Trust at the Capture-Containment Boundary"
topics:
  - "kubernetes"
---

# CUSTOS: Toward Forensic-Ready Zero Trust at the Capture-Containment Boundary

[원문 열기](https://arxiv.org/abs/2608.17068v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-17T19:17:15Z
- 저자: Avinash Srinivasan, John Paramadilok
- 식별자: `arxiv:2608.17068`

## 요약·초록

Zero Trust (ZT) replaces implicit trust with continuous verification, but mutual TLS, ephemeral workloads, identity-centric control, and automated remediation reduce payload visibility, weaken IP-based attribution, and shrink the window for acquiring volatile evidence. We propose CUSTOS, a forensic-ready ZT reference architecture centered on a Forensic Management Point (FMP) that coordinates tiered capture, identity- and policy-linked reconstruction, telemetry orchestration, and ZT-controlled investigative access. We evaluate a composed, component-level prototype using a live enforcement gateway plus separate runtime and orchestrator experiments. An always-on decision record is captured and hash-chained on the gateway at a 1.9-3.0\% throughput cost on in-process policy engines, preserving decision provenance outside the monitored workload under stated trust assumptions. Reactive checkpointing (about 65 ms) precedes seconds-scale defender-routed eviction but loses to unsequenced direct SIGKILL (about 9 ms), in-kernel enforcement, and adversarial self-destruction, producing the forensic shredder effect. On a real container, concurrent capture and SIGKILL recovered the planted secret in 0/1000 trials; sequencing SIGKILL behind the FMP barrier recovered it in 1000/1000. The primary integrated single-node Kubernetes race checkpoints an FMP-controlled process; container-memory capture is evaluated separately and was unavailable in the managed-Kubernetes configuration. Across five public benchmark datasets and a synthetic schema reference, identity-oriented telemetry populates 64-75\% of the decision-record schema against 18-30\% for network-oriented, while rate limiting bounds the full-memory admission ceiling. These results show that forensic-ready ZT requires both an always-on evidentiary floor and bounded reactive capture, while identifying where volatile evidence remains unrecoverable.

## 내 메모


