---
type: research-source
item_id: 2563
title: "HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?"
source: "arxiv"
published: "2026-09-01T15:45:33Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.01437"
url: "https://arxiv.org/abs/2609.01437v1"
generated_by: codex-research-db
aliases:
  - "HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?"
topics:
  - "self-evolving-harness"
---

# HarnessDev: Can LLMs Create and Evolve Their Own Agent Harness?

[원문 열기](https://arxiv.org/abs/2609.01437v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-01T15:45:33Z
- 저자: Yuhao Wu, Jingyuan Zhang, Jiajun Shi, Xinping Lei, Qingshui Gu, Yuxuan Zhang, Zexuan Wang, Chen He, Chen Huang, Maojia Song, Zhiyuan Zeng, Shaowen Wang, Jinkai Liu, Yunfeng Shi, Jiaheng Liu, Shen Yan, Wenhao Huang, Ge Zhang, Wenxuan Zhang
- 식별자: `arxiv:2609.01437`

## 요약·초록

As agents move from research prototypes to deployed tools, their capability increasingly depends on model-external execution infrastructure, commonly termed the agent harness. Changing this harness while holding model weights fixed can substantially alter task performance. Current agent evaluations typically report downstream performance under a chosen harness, leaving a model's ability to develop the harness itself comparatively underexplored. We introduce HarnessDev, a benchmark that shifts the unit of evaluation from task outputs to runnable infrastructure. HarnessDev covers two stages. In Creation, the agent starts from a minimal seed and a small number of cases, then builds a complete execution system. In Evolution, it starts from its own created harness and iteratively revises it using downstream execution feedback, with the goal of improving benchmark performance. We then evaluate each constructed harness on capability (task success on held-out benchmarks) and efficiency (execution-token cost). The reported Creation results cover six creator LLMs, four domains, and five downstream benchmarks totaling 2,207 unique downstream instances, with hidden evaluation tasks withheld from development. We find that generated harnesses remain substantially behind mature human-engineered references on code and on search and research, while matching or exceeding the selected references on writing and machine-learning experimentation, with large variation in execution cost. Evolution produces some performance gains, but they are unstable and transfer only partially to held-out tasks. Experiments with a fixed runtime model further show that the gains depend strongly on the model executing the harness, indicating limited transfer across models.

## 내 메모


