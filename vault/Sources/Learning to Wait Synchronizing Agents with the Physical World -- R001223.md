---
type: research-source
item_id: 1223
title: "Learning to Wait: Synchronizing Agents with the Physical World"
source: "arxiv"
published: "2025-12-18T07:24:44Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.16262"
url: "https://arxiv.org/abs/2512.16262v1"
generated_by: codex-research-db
aliases:
  - "Learning to Wait: Synchronizing Agents with the Physical World"
topics:
  - "kubernetes"
---

# Learning to Wait: Synchronizing Agents with the Physical World

[원문 열기](https://arxiv.org/abs/2512.16262v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6RNHT2FV`)
- 발행일: 2025-12-18T07:24:44Z
- 저자: Yifei She, Ping Zhang, He Liu, Yanmin Jia, Yang Jing, Zijun Liu, Peng Sun, Xiangbin Li, Xiaohe Hu
- 식별자: `arxiv:2512.16262`

## 요약·초록

Real-world agentic tasks, unlike synchronous Markov Decision Processes (MDPs), often involve non-blocking actions with variable latencies, creating a fundamental \textit{Temporal Gap} between action initiation and completion. Existing environment-side solutions, such as blocking wrappers or frequent polling, either limit scalability or dilute the agent's context window with redundant observations. In this work, we propose an \textbf{Agent-side Approach} that empowers Large Language Models (LLMs) to actively align their \textit{Cognitive Timeline} with the physical world. By extending the Code-as-Action paradigm to the temporal domain, agents utilize semantic priors and In-Context Learning (ICL) to predict precise waiting durations (\texttt{time.sleep(t)}), effectively synchronizing with asynchronous environment without exhaustive checking. Experiments in a simulated Kubernetes cluster demonstrate that agents can precisely calibrate their internal clocks to minimize both query overhead and execution latency, validating that temporal awareness is a learnable capability essential for autonomous evolution in open-ended environments.

## 내 메모


