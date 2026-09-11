---
type: research-source
item_id: 2750
title: "SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?"
source: "arxiv"
published: "2026-09-08T17:45:09Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.09113"
url: "https://arxiv.org/abs/2609.09113v1"
generated_by: codex-research-db
aliases:
  - "SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?"
topics:
  - "ai-agents"
---

# SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?

[원문 열기](https://arxiv.org/abs/2609.09113v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4DIH9VWX`)
- 발행일: 2026-09-08T17:45:09Z
- 저자: Yuqiao Tan, Shizhu He, Jun Zhao, Kang Liu
- 식별자: `arxiv:2609.09113`

## 요약·초록

While research on recursive self-improvement (RSI) has predominantly automated model training pipelines, reliable autonomous development demands a missing pillar: post-hoc monitoring and auditing to understand what models learn and ensure safe alignment. Mechanistic interpretability tools are essential to bridge this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by isolating interpretable features for model inspection and steering. In this paper, we introduce SAEScientist-Bench to evaluate whether AI agents can act as scientists utilizing SAE tools for autonomous mechanistic discovery. Given a target concept, an agent designs contrastive probes and navigates a Gemma Scope dictionary of 131K+ features in Gemma-2-9B-IT to discover the optimal feature, evaluated against curated expert reference features anchored on Neuronpedia across activation rank, concept selectivity on contrastive texts, and causal steering. Across 10 agent configurations and 20 tasks, frontier agents demonstrate genuine discovery capabilities and lead different evaluation dimensions, but remain well behind the expert baseline, approaching expert levels on separating target concepts from contrastive controls while lagging substantially in causal generation steering. Further analysis reveals that although agents can design contrasts to rule out spurious candidates, they frequently misinterpret experimental measurements. These results establish experimental model understanding as a measurable capability for closed-loop autonomous AI R&D. Our code is available at https://github.com/Trae1ounG/SAEScientist.

## 내 메모


