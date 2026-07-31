---
type: research-source
item_id: 303
title: "EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning"
source: "arxiv"
published: "2024-06-11T15:08:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.07342"
url: "https://arxiv.org/abs/2406.07342v1"
generated_by: codex-research-db
aliases:
  - "EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning"
topics:
  - "edge-computing"
  - "kubernetes"
---

# EdgeTimer: Adaptive Multi-Timescale Scheduling in Mobile Edge Computing with Deep Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2406.07342v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`CR8NFB48`)
- 발행일: 2024-06-11T15:08:14Z
- 저자: Yijun Hao, Shusen Yang, Fang Li, Yifan Zhang, Shibo Wang, Xuebin Ren
- 식별자: `arxiv:2406.07342`

## 요약·초록

In mobile edge computing (MEC), resource scheduling is crucial to task requests' performance and service providers' cost, involving multi-layer heterogeneous scheduling decisions. Existing schedulers typically adopt static timescales to regularly update scheduling decisions of each layer, without adaptive adjustment of timescales for different layers, resulting in potentially poor performance in practice. We notice that the adaptive timescales would significantly improve the trade-off between the operation cost and delay performance. Based on this insight, we propose EdgeTimer, the first work to automatically generate adaptive timescales to update multi-layer scheduling decisions using deep reinforcement learning (DRL). First, EdgeTimer uses a three-layer hierarchical DRL framework to decouple the multi-layer decision-making task into a hierarchy of independent sub-tasks for improving learning efficiency. Second, to cope with each sub-task, EdgeTimer adopts a safe multi-agent DRL algorithm for decentralized scheduling while ensuring system reliability. We apply EdgeTimer to a wide range of Kubernetes scheduling rules, and evaluate it using production traces with different workload patterns. Extensive trace-driven experiments demonstrate that EdgeTimer can learn adaptive timescales, irrespective of workload patterns and built-in scheduling rules. It obtains up to 9.1x more profit than existing approaches without sacrificing the delay performance.

## 내 메모


