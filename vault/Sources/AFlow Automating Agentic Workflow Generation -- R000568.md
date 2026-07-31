---
type: research-source
item_id: 568
title: "AFlow: Automating Agentic Workflow Generation"
source: "arxiv"
published: "2024-10-14T17:40:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2410.10762"
url: "https://arxiv.org/abs/2410.10762v4"
generated_by: codex-research-db
aliases:
  - "AFlow: Automating Agentic Workflow Generation"
topics:
  - "self-evolving-harness"
---

# AFlow: Automating Agentic Workflow Generation

[원문 열기](https://arxiv.org/abs/2410.10762v4)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GIVRI7RP`)
- 발행일: 2024-10-14T17:40:40Z
- 저자: Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xionghui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, Bingnan Zheng, Bang Liu, Yuyu Luo, Chenglin Wu
- 식별자: `arxiv:2410.10762`

## 요약·초록

Large language models (LLMs) have demonstrated remarkable potential in solving complex tasks across diverse domains, typically by employing agentic workflows that follow detailed instructions and operational sequences. However, constructing these workflows requires significant human effort, limiting scalability and generalizability. Recent research has sought to automate the generation and optimization of these workflows, but existing methods still rely on initial manual setup and fall short of achieving fully automated and effective workflow generation. To address this challenge, we reformulate workflow optimization as a search problem over code-represented workflows, where LLM-invoking nodes are connected by edges. We introduce AFlow, an automated framework that efficiently explores this space using Monte Carlo Tree Search, iteratively refining workflows through code modification, tree-structured experience, and execution feedback. Empirical evaluations across six benchmark datasets demonstrate AFlow's efficacy, yielding a 5.7% average improvement over state-of-the-art baselines. Furthermore, AFlow enables smaller models to outperform GPT-4o on specific tasks at 4.55% of its inference cost in dollars. The code is available at https://github.com/FoundationAgents/AFlow.

## 내 메모


