---
type: research-source
item_id: 60
title: "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning"
source: "arxiv"
published: "2026-07-01T19:20:46Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.01415"
url: "https://arxiv.org/abs/2607.01415v1"
generated_by: codex-research-db
aliases:
  - "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning"
topics:
  - "kubernetes"
---

# The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2607.01415v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`I3AAGE7Z`)
- 발행일: 2026-07-01T19:20:46Z
- 저자: Daniel Thi Graviet, Lovre Pesut, Ivan Dagelic, Vedran Jukic, Ivan Burazin
- 식별자: `arxiv:2607.01415`

## 요약·초록

Coding-agent reinforcement learning treats execution infrastructure as a background implementation detail, despite relying on large numbers of interactive software rollouts. This is a missed opportunity: measuring infrastructure overhead can reveal practical efficiency gains for RL post-training, where small per-rollout savings compound at scale. We present a comparative study of four execution substrates: single containers, hosted sandboxes, Kubernetes-orchestrated containers, and cloud virtual machines. We find up to $110\times$ variation in cold-start latency and a $1.8\times$ spread in projected worker-hours for one million 150-step trajectories. Our results suggest that future coding-agent RL systems should optimize execution substrates as part of the training system itself, not merely as deployment plumbing.

## 내 메모


