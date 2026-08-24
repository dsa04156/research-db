---
type: research-source
item_id: 2201
title: "A reinforcement learning-driven adaptive hybrid PLC-RF communication architecture for IoT-based smart metering systems"
source: "openalex"
published: "2026-08-22"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-65952-0"
url: "https://doi.org/10.1038/s41598-026-65952-0"
generated_by: codex-research-db
aliases:
  - "A reinforcement learning-driven adaptive hybrid PLC-RF communication architecture for IoT-based smart metering systems"
topics:
  - "edge-computing"
---

# A reinforcement learning-driven adaptive hybrid PLC-RF communication architecture for IoT-based smart metering systems

[원문 열기](https://doi.org/10.1038/s41598-026-65952-0)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-08-22
- 저자: Noor El-Deen M. Mohamed, Mahmoud A. Shafea, Alaa M. Yousry, Mohamed M. El-Dakroury
- 식별자: `doi:10.1038/s41598-026-65952-0`

## 요약·초록

With the rapid expansion of smart grid infrastructure, robust and scalable communication is essential to support Advanced Metering Infrastructure (AMI). This paper presents a hybrid communication architecture that combines Power Line Communication (PLC) and Radio Frequency (RF) technologies to enable reliable, adaptive data transmission in smart metering networks. The proposed system employs a PLC-based mesh topology that utilizes existing electrical wiring to relay meter data to a Data Concentrator Unit (DCU), alongside an RF-based star topology that provides direct wireless links between smart meters and the DCU. A cloud-based web application is integrated for real-time visualization of power consumption, network health, and active communication paths. To dynamically select the optimal channel based on real-time latency, packet loss, and Signal-to-Noise Ratio (SNR), a Proximal Policy Optimization (PPO) reinforcement learning agent is implemented and benchmarked against tabular Q-Learning, Double Deep Q-Network (DDQN), and Deep Deterministic Policy Gradient (DDPG). The system is validated through hardware prototyping and subjected to multi-seed training, reward function sensitivity analysis, edge microcontroller profiling, and network-scale simulation to assess deployment viability. Evaluated over 5, 000 deterministic test cases against a reward-derived oracle, the PPO agent achieved an accuracy of [Formula: see text] and an F1 score of [Formula: see text], attaining the highest single-run performance among all evaluated agents, with statistically significant advantages over Q-Learning and, for F1 score, over DDPG. Multi-seed training across ten initializations confirmed superior convergence stability with an accuracy standard deviation of only [Formula: see text], mitigating policy collapse. Edge AI profiling on an Arm Cortex-M4 platform demonstrated that INT8 quantization compresses the model by [Formula: see text] to 64.7 KB while preserving [Formula: see text] of baseline accuracy at a 1.93 ms on-device latency. A reward sensitivity sweep across 16 coefficient perturbations verified policy robustness under varying weight configurations. Finally, a network-scale simulation across 500 to 5, 000 nodes confirmed scale-invariant performance with a Packet Delivery Ratio above [Formula: see text] and consistent resilience under node outages, traffic overload, and channel degradation, providing simulation-based evidence of the scalability and resilience of AI-driven adaptive communication for large-scale smart grid deployments.

## 내 메모


