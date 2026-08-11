---
type: research-source
item_id: 1849
title: "ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents"
source: "arxiv"
published: "2026-08-10T11:45:03Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.09476"
url: "https://arxiv.org/abs/2608.09476v1"
generated_by: codex-research-db
aliases:
  - "ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents"
topics:
  - "self-evolving-harness"
---

# ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents

[원문 열기](https://arxiv.org/abs/2608.09476v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-10T11:45:03Z
- 저자: Hongwei Yao, Yiming Liu, Meihui Chen, Jieling Chen, Zikun Chen, Yiling He, Wangze Ni, Cong Wang, Kui Ren
- 식별자: `arxiv:2608.09476`

## 요약·초록

Cowork agents may complete benign tasks while disclosing protected data, manipulating unauthorized state, invocate unauthorized API. We define behavioral safety and introduce ActBench, a self-evolving benchmark that evaluates such behavior risk from execution trajectories rather than final responses. Each case pairs a benign task with an adversarial variant that preserves its instruction, configuration, initial state, rating model, and trusted records while injecting a task-reachable payload. ActBench contains 600 cases from 213 scenarios, spanning 15 risk behaviors, six execution spaces, and 48 web-service APIs.To move beyond static payloads, we propose a reward-guided beam search method that jointly optimizes attack effectiveness and task utility, while reflection diagnoses failed execution checkpoint and guides payload revision. Besides, we propose a dual evidence verification mechanism that verifies agent execution safety and utility through log evidence and LLM-based trajectory evidence.We evaluate 15 LLMs and 6 open-source cowork agents over 24,000 trajectories. Under a fixed harness, attack success rates ranges from 10.1% to 94.4% across models, while under a fixed base model, they range from 73.7% to 94.4% across agents.These results show greater variation across models than agent harness, while attacks remain highly successful across all tested harnesses.Our benchmark is released at: https://github.com/zjuicsr/ActBench.

## 내 메모


