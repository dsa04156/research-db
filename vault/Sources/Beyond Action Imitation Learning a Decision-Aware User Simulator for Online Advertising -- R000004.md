---
type: research-source
item_id: 4
title: "Beyond Action Imitation: Learning a Decision-Aware User Simulator for Online Advertising"
source: "arxiv"
published: "2026-07-29T13:25:30Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26893"
url: "https://arxiv.org/abs/2607.26893v1"
generated_by: codex-research-db
aliases:
  - "Beyond Action Imitation: Learning a Decision-Aware User Simulator for Online Advertising"
topics:
  - "self-evolving-harness"
---

# Beyond Action Imitation: Learning a Decision-Aware User Simulator for Online Advertising

[원문 열기](https://arxiv.org/abs/2607.26893v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2AXMQKZB`)
- 발행일: 2026-07-29T13:25:30Z
- 저자: Zipeng Chen, Jiaer Zheng, Xiangyang Xu, Xinyu Lin, Zhaobin Wang, Zhaohui Liu, Qianjin Xiang, Xiaoyu Zhao, Zhuozhen Yu, Guangshuo Wang, Daxing Chen, Junwei Pan, Zhangbin Zhu, Chengguo Yin, Hao Chen, Tat-Seng Chua, Haijie Gu, Jie Jiang
- 식별자: `arxiv:2607.26893`

## 요약·초록

Recent advances in LLM-based user simulation have shown promise for offline evaluation of recommendation and advertising systems. However, existing simulators typically infer user preferences from single-domain interaction histories and are primarily optimized to reproduce observable actions such as clicks. Consequently, they capture only a partial view of user preferences, while action-only prediction easily induces model shortcuts and limits both the fidelity and diagnostic value of simulation. To address these challenges, we propose DASH, a decision-aware user simulator that jointly generates thinking traces and predicts behavioral actions from heterogeneous cross-domain histories. DASH first introduces a Context Engineering stage that folds heterogeneous cross-domain histories into decision-relevant context, together with prompt optimization for effective reasoning over the folded context. To train a user simulator, DASH distills thinking trajectories from strong LLMs as SFT data, and further tailors a rubric-based reward model that evaluates thinking traces along form, content, and logic for RL training. Combined with the action reward, these signals jointly improve action prediction and thinking quality. Extensive experiments on real-world Tencent advertising data spanning five heterogeneous content domains demonstrate the effectiveness, efficiency, fidelity, and diagnostic value of DASH.

## 내 메모


