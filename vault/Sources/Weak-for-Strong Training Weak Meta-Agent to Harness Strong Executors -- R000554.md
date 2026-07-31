---
type: research-source
item_id: 554
title: "Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors"
source: "arxiv"
published: "2025-04-07T07:27:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2504.04785"
url: "https://arxiv.org/abs/2504.04785v1"
generated_by: codex-research-db
aliases:
  - "Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors"
topics:
  - "self-evolving-harness"
---

# Weak-for-Strong: Training Weak Meta-Agent to Harness Strong Executors

[원문 열기](https://arxiv.org/abs/2504.04785v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VI4652I4`)
- 발행일: 2025-04-07T07:27:31Z
- 저자: Fan Nie, Lan Feng, Haotian Ye, Weixin Liang, Pan Lu, Huaxiu Yao, Alexandre Alahi, James Zou
- 식별자: `arxiv:2504.04785`

## 요약·초록

Efficiently leveraging of the capabilities of contemporary large language models (LLMs) is increasingly challenging, particularly when direct fine-tuning is expensive and often impractical. Existing training-free methods, including manually or automated designed workflows, typically demand substantial human effort or yield suboptimal results. This paper proposes Weak-for-Strong Harnessing (W4S), a novel framework that customizes smaller, cost-efficient language models to design and optimize workflows for harnessing stronger models. W4S formulates workflow design as a multi-turn markov decision process and introduces reinforcement learning for agentic workflow optimization (RLAO) to train a weak meta-agent. Through iterative interaction with the environment, the meta-agent learns to design increasingly effective workflows without manual intervention. Empirical results demonstrate the superiority of W4S that our 7B meta-agent, trained with just one GPU hour, outperforms the strongest baseline by 2.9% ~ 24.6% across eleven benchmarks, successfully elevating the performance of state-of-the-art models such as GPT-3.5-Turbo and GPT-4o. Notably, W4S exhibits strong generalization capabilities across both seen and unseen tasks, offering an efficient, high-performing alternative to directly fine-tuning strong models.

## 내 메모


