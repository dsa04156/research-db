---
type: research-source
item_id: 2994
title: "TERMon: Detecting Persistent Behavioral Threats in Edge AI via Hardware-Native Ternary Runtime Monitor"
source: "kurate"
published: "2026-09-18T12:49:50Z"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "arxiv:2609.21713"
url: "http://arxiv.org/abs/2609.21713v1"
generated_by: codex-research-db
aliases:
  - "TERMon: Detecting Persistent Behavioral Threats in Edge AI via Hardware-Native Ternary Runtime Monitor"
topics:
  - "edge-computing"
---

# TERMon: Detecting Persistent Behavioral Threats in Edge AI via Hardware-Native Ternary Runtime Monitor

[원문 열기](http://arxiv.org/abs/2609.21713v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- 발행일: 2026-09-18T12:49:50Z
- 저자: Arish Sateesan, Edlira Dushku
- 식별자: `arxiv:2609.21713`

## 요약·초록

Edge AI accelerators are increasingly deployed in safety-critical environments, where model outputs may control physical actuators, make access-control decisions, or trigger alarms. In these settings, runtime failures often remain undetected because model corruption, distribution shift, and adversarial inputs can still produce well-formed, confident predictions. This paper presents TERMon, a lightweight hardware runtime monitor that detects such anomalies by observing inference behavior rather than re-executing or formally verifying the model. TERMon represents class-conditional trusted behavior as hardware-efficient ternary patterns that are matched in parallel against a thermometer-encoded fingerprint. The ternary encoding reproduces the corresponding unquantized range decision exactly. TERMon detects harmful weight corruptions in proportion to their behavioral impact, while out-of-distribution and adversarial inputs are largely not separable using the monitored features at a strict false-positive operating point. We implemented TERMon on a PYNQ-Z2 FPGA, and the pipelined design requires no on-chip block RAM or DSPs and has a two-cycle decision latency.

## 내 메모
