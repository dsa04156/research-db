---
type: research-source
item_id: 1161
title: "When Does Deep RL Beat Calibrated Baselines? A Benchmark Study on Adaptive Resource Control"
source: "arxiv"
published: "2026-05-26T01:07:42Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.26418"
url: "https://arxiv.org/abs/2605.26418v3"
generated_by: codex-research-db
aliases:
  - "When Does Deep RL Beat Calibrated Baselines? A Benchmark Study on Adaptive Resource Control"
topics:
  - "kubernetes"
---

# When Does Deep RL Beat Calibrated Baselines? A Benchmark Study on Adaptive Resource Control

[원문 열기](https://arxiv.org/abs/2605.26418v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3KKVKBD7`)
- 발행일: 2026-05-26T01:07:42Z
- 저자: Guilin Zhang, Chuanyi Sun, Kai Zhao, Xu Chu, Shahryar Sarkani, John Fossaceca
- 식별자: `arxiv:2605.26418`

## 요약·초록

A properly calibrated rule-based autoscaler can beat every one of six mainstream deep reinforcement learning (DRL) algorithms on cost across every workload we test - so when, if ever, does DRL actually help? We study this in RLScale-Bench, a reproducible benchmark and evaluation protocol for DRL on adaptive resource control, where an agent allocates compute to a dynamic workload under cost and service-level constraints. We evaluate PPO, DQN, A2C, SAC, TD3, and DDPG under matched architectures, training budgets, and reward functions against a calibrated rule-based baseline across six workload patterns and five seeds (240 runs), instantiate the benchmark on Kubernetes Horizontal Pod Autoscaling, and probe distribution-shift generalization. Three findings challenge common assumptions: (i) the calibrated controller achieves the lowest cost on all six workloads, though it trails the best RL agents on bursty and flash traffic; (ii) discrete-action algorithms outperform continuous-action ones by one to two orders of magnitude in constraint violations due to action-space mismatch; and (iii) no single algorithm dominates across workloads, with rankings shifting by up to four positions. The bottleneck in RL-based resource control is not algorithm selection but baseline calibration, reward engineering, and realistic evaluation protocols.

## 내 메모


