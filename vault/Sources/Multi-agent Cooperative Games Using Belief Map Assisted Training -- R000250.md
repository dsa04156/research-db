---
type: research-source
item_id: 250
title: "Multi-agent Cooperative Games Using Belief Map Assisted Training"
source: "arxiv"
published: "2024-06-27T18:40:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.3233/faia230444"
url: "https://arxiv.org/abs/2406.19477v1"
generated_by: codex-research-db
aliases:
  - "Multi-agent Cooperative Games Using Belief Map Assisted Training"
topics:
  - "ai-agents"
---

# Multi-agent Cooperative Games Using Belief Map Assisted Training

[원문 열기](https://arxiv.org/abs/2406.19477v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZI293Z3E`)
- 발행일: 2024-06-27T18:40:55Z
- 저자: Qinwei Huang, Chen Luo, Alex B. Wu, Simon Khan, Hai Li, Qinru Qiu
- 식별자: `doi:10.3233/faia230444`

## 요약·초록

In a multi-agent system, agents share their local observations to gain global situational awareness for decision making and collaboration using a message passing system. When to send a message, how to encode a message, and how to leverage the received messages directly affect the effectiveness of the collaboration among agents. When training a multi-agent cooperative game using reinforcement learning (RL), the message passing system needs to be optimized together with the agent policies. This consequently increases the model's complexity and poses significant challenges to the convergence and performance of learning. To address this issue, we propose the Belief-map Assisted Multi-agent System (BAMS), which leverages a neuro-symbolic belief map to enhance training. The belief map decodes the agent's hidden state to provide a symbolic representation of the agent's understanding of the environment and other agent's status. The simplicity of symbolic representation allows the gathering and comparison of the ground truth information with the belief, which provides an additional channel of feedback for the learning. Compared to the sporadic and delayed feedback coming from the reward in RL, the feedback from the belief map is more consistent and reliable. Agents using BAMS can learn a more effective message passing network to better understand each other, resulting in better performance in a cooperative predator and prey game with varying levels of map complexity and compare it to previous multi-agent message passing models. The simulation results showed that BAMS reduced training epochs by 66\%, and agents who apply the BAMS model completed the game with 34.62\% fewer steps on average.

## 내 메모


