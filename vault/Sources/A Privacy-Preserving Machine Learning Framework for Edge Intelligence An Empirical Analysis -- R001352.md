---
type: research-source
item_id: 1352
title: "A Privacy-Preserving Machine Learning Framework for Edge Intelligence: An Empirical Analysis"
source: "arxiv"
published: "2026-05-07T06:43:51Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.05751"
url: "https://arxiv.org/abs/2605.05751v1"
generated_by: codex-research-db
aliases:
  - "A Privacy-Preserving Machine Learning Framework for Edge Intelligence: An Empirical Analysis"
topics:
  - "edge-computing"
---

# A Privacy-Preserving Machine Learning Framework for Edge Intelligence: An Empirical Analysis

[원문 열기](https://arxiv.org/abs/2605.05751v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BIH6I2J9`)
- 발행일: 2026-05-07T06:43:51Z
- 저자: Quoc Lap Trieu, Bahman Javadi, Jim Basilakis
- 식별자: `arxiv:2605.05751`

## 요약·초록

As Edge Intelligence (EI) becomes increasingly prevalent in domains such as smart healthcare, manufacturing, and critical infrastructure, ensuring data privacy while maintaining system efficiency is a growing challenge. This paper presents a new privacy-preserving machine learning (PPML) framework tailored for EI applications, including a four-layer system architecture and training and inference algorithms. We focus on three leading approaches: Differential Privacy (DP), Secure Multi-party Computation (SMC), and Fully Homomorphic Encryption (FHE), and assess their impact on key performance metrics, including model accuracy, response time, and energy consumption. Results from real implementation and extensive trace-based simulations of inference tasks show that DP generally preserves throughput and latency close to plaintext baselines, while accuracy drops with model complexity (up to 35 percent on AlexNet and under 18 percent on LeNet for FordA). SMC performance is driven by communication; network bandwidth and round complexity determine end-to-end latency. For AlexNet, increasing link capacity from 250 Mbps to 500 Mbps reduces latency by about 30 percent. FHE is highly sensitive to model structure and numerical precision bit width, with tighter parameters imposing substantial compute overhead; we observe roughly a 1000 times increase in response time compared to DP. Beyond efficiency, DP shifts the privacy-utility-extractability frontier by reducing the attacker's data efficiency in black-box model stealing, whereas SMC and FHE, while protecting inputs and parameters during inference, require complementary output controls to achieve similar resistance to extraction. These findings provide critical insights into the trade-offs between privacy, performance, and resource efficiency in edge computing scenarios.

## 내 메모


