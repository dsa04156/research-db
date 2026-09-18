---
type: research-source
item_id: 2895
title: "FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA"
source: "arxiv"
published: "2026-09-17T04:25:17Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.19680"
url: "https://arxiv.org/abs/2609.19680v1"
generated_by: codex-research-db
aliases:
  - "FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA"
topics:
  - "ai-agents"
---

# FINSKILLOPS: A Self-Evolving Multi-Agent System for SEC Filing QA

[원문 열기](https://arxiv.org/abs/2609.19680v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TWKTWB2B`)
- 발행일: 2026-09-17T04:25:17Z
- 저자: Yanzhang Ma, Zhenghan Tai, Hanwei Wu, Sizhe Guan, Jianliang Lei, Hailin He, Chaolong Jiang, Jijun Chi, Tung Sum Thomas Kwok, Bohuai Xiao, Jingrui Tian, Xinlu Wu, Xingao Zhan, Peng Lu, Muzhi Li, Yihong Wu, Liheng Ma, Sicheng Lyu, Tianshuo Yan, Junhao Zhu, Yaqian Xu, Lei Ding, Yufei Cui, Ziquan Liu, Boyu Han, Hengli Liu, Ling Zhou, Xinyu Wang
- 식별자: `arxiv:2609.19680`

## 요약·초록

Financial QA systems are typically improved before deployment through better retrieval, prompting, or agent coordination, leaving their reliability behavior fixed thereafter. In practice, new SEC-filing questions repeatedly expose heterogeneous errors in period, entity, evidence use, and calculation. Existing self-improvement methods can turn failures into new behaviors, but offer limited control over where a correction should apply or which previously correct answers it may break. We therefore frame post-deployment improvement as controlled behavioral maintenance: recurring failures should become scoped skill patches, and each patch should earn deployment with- out introducing regressions. We instantiate this view in FINSKILLOPS, a multi-agent system for SEC filing QA. FINSKILLOPS derives reusable skills from evidence-grounded, typed failure diagnoses and governs them through targeted validation, protected-case regression checks, negative controls, and versioned replacement or retirement. Across six financial QA benchmarks, a single frozen skill registry achieves the highest verdict-weighted correctness and reference consistency among the evaluated systems. Evolved skills raise correctness from 3.70 to 4.55 on our enhanced benchmark. In a separate 12-round operational study, only six of 33 proposed skills are promoted, while the monitoring non-correct rate falls from 20.0% to 12.5%. These results establish controlled skill scope, admission, and lifecycle management as the foundation for reliable self-improvement.

## 내 메모


