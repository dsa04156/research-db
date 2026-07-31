---
type: research-source
item_id: 585
title: "Deep Reinforcement Learning-based Cell DTX/DRX Configuration for Network Energy Saving"
source: "arxiv"
published: "2025-07-28T23:35:24Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.21385"
url: "https://arxiv.org/abs/2507.21385v1"
generated_by: codex-research-db
aliases:
  - "Deep Reinforcement Learning-based Cell DTX/DRX Configuration for Network Energy Saving"
topics:
  - "ai-agents"
---

# Deep Reinforcement Learning-based Cell DTX/DRX Configuration for Network Energy Saving

[원문 열기](https://arxiv.org/abs/2507.21385v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PSGCVPSP`)
- 발행일: 2025-07-28T23:35:24Z
- 저자: Wei Mao, Lili Wei, Omid Semiari, Shu-ping Yeh, Hosein Nikopour
- 식별자: `arxiv:2507.21385`

## 요약·초록

3GPP Release 18 cell discontinuous transmission and reception (cell DTX/DRX) is an important new network energy saving feature for 5G. As a time-domain technique, it periodically aggregates the user data transmissions in a given duration of time when the traffic load is not heavy, so that the remaining time can be kept silent and advanced sleep modes (ASM) can be enabled to shut down more radio components and save more energy for the cell. However, inevitably the packet delay is increased, as during the silent period no transmission is allowed. In this paper we study how to configure cell DTX/DRX to optimally balance energy saving and packet delay, so that for delay-sensitive traffic maximum energy saving can be achieved while the degradation of quality of service (QoS) is minimized. As the optimal configuration can be different for different network and traffic conditions, the problem is complex and we resort to deep reinforcement learning (DRL) framework to train an AI agent to solve it. Through careful design of 1) the learning algorithm, which implements a deep Q-network (DQN) on a contextual bandit (CB) model, and 2) the reward function, which utilizes a smooth approximation of a theoretically optimal but discontinuous reward function, we are able to train an AI agent that always tries to select the best possible Cell DTX/DRX configuration under any network and traffic conditions. Simulation results show that compared to the case when cell DTX/DRX is not used, our agent can achieve up to ~45% energy saving depending on the traffic load scenario, while always maintaining no more than ~1% QoS degradation.

## 내 메모


