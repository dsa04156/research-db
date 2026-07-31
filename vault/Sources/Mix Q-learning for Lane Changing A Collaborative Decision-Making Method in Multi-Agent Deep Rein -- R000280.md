---
type: research-source
item_id: 280
title: "Mix Q-learning for Lane Changing: A Collaborative Decision-Making Method in Multi-Agent Deep Reinforcement Learning"
source: "arxiv"
published: "2024-06-14T06:44:19Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.09755"
url: "https://arxiv.org/abs/2406.09755v2"
generated_by: codex-research-db
aliases:
  - "Mix Q-learning for Lane Changing: A Collaborative Decision-Making Method in Multi-Agent Deep Reinforcement Learning"
topics:
  - "ai-agents"
---

# Mix Q-learning for Lane Changing: A Collaborative Decision-Making Method in Multi-Agent Deep Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2406.09755v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`25DQCRV4`)
- 발행일: 2024-06-14T06:44:19Z
- 저자: Xiaojun Bi, Mingjie He, Yiwen Sun
- 식별자: `arxiv:2406.09755`

## 요약·초록

Lane-changing decisions, which are crucial for autonomous vehicle path planning, face practical challenges due to rule-based constraints and limited data. Deep reinforcement learning has become a major research focus due to its advantages in data acquisition and interpretability. However, current models often overlook collaboration, which affects not only impacts overall traffic efficiency but also hinders the vehicle's own normal driving in the long run. To address the aforementioned issue, this paper proposes a method named Mix Q-learning for Lane Changing(MQLC) that integrates a hybrid value Q network, taking into account both collective and individual benefits for the greater good. At the collective level, our method coordinates the individual Q and global Q networks by utilizing global information. This enables agents to effectively balance their individual interests with the collective benefit. At the individual level, we integrated a deep learning-based intent recognition module into our observation and enhanced the decision network. These changes provide agents with richer decision information and more accurate feature extraction for improved lane-changing decisions. This strategy enables the multi-agent system to learn and formulate optimal decision-making strategies effectively. Our MQLC model, through extensive experimental results, impressively outperforms other state-of-the-art multi-agent decision-making methods, achieving significantly safer and faster lane-changing decisions. The code is available at https:github.com/pku-smart-city/source_code/tree/main/MQLC.

## 내 메모


