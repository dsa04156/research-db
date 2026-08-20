---
type: research-source
item_id: 2151
title: "Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL"
source: "kurate"
published: "2026-08-18T01:16:02Z"
first_seen: "2026-08-20"
review_status: "pending"
canonical_key: "arxiv:2608.17253"
url: "http://arxiv.org/abs/2608.17253v1"
generated_by: codex-research-db
aliases:
  - "Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL"
topics:
  - "ai-agents"
---

# Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL

[원문 열기](http://arxiv.org/abs/2608.17253v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-20|2026-08-20]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- 발행일: 2026-08-18T01:16:02Z
- 저자: Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, Ziang Xiao, Nuno Vasconcelos
- 식별자: `arxiv:2608.17253`

## 요약·초록

Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning capabilities advance beyond what humans can reliably evaluate. Self-rewarding RL reduces this dependence by enabling models to derive reward signals from their own completions. However, training solely on self-generated feedback can reinforce existing biases and suboptimal behaviors, reduce response diversity, and ultimately lead to homogenized responses and training collapse. In this work, we show that unsupervised reasoning can emerge through cooperative multi-agent training. We introduce Co-RL, a framework in which multiple decoupled models, sharing no parameters, are simultaneously optimized through RL using rewards derived from their peers. We further show that increasing cohort diversity, through heterogeneous model families, sizes, and rephrased training samples, reduces the correlated errors that drive self-reinforcing feedback loops. This diversity consistently improves reasoning performance, maintains behavioral diversity, and mitigates training collapse. Across text-only and multimodal domains, Co-RL consistently outperforms the base models and prior label-free approaches, while matching or surpassing supervised methods, without access to any ground-truth labels. Concretely, Co-RL yields average gains of 3.0-8.6% across seven text-only benchmarks for LLMs and 2.3-7.2% across four multimodal benchmarks for VLMs. Code is available at https://github.com/DrStranded/Co-RL.

## 내 메모


