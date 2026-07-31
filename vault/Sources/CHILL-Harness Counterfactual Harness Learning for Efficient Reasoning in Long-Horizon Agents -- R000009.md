---
type: research-source
item_id: 9
title: "CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents"
source: "arxiv"
published: "2026-07-28T15:06:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25825"
url: "https://arxiv.org/abs/2607.25825v1"
generated_by: codex-research-db
aliases:
  - "CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents

[원문 열기](https://arxiv.org/abs/2607.25825v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`V2PQVZ6P`)
- 발행일: 2026-07-28T15:06:00Z
- 저자: Jiarun Fu, Lizhong Ding, Sida Chen, Honglei Xin, Chunhui Zhang, Pengqi Li, Qiuning Wei, Ye Yuan, Guoren Wang
- 식별자: `arxiv:2607.25825`

## 요약·초록

Agent harnesses have become the operational infrastructure of modern large language model agents, coordinating context, tools, verification, and execution control to translate latent model capability into reliable long-horizon behavior. However, reliable long-horizon behavior requires harness control to adapt to task demands, execution environments, and evolving execution states, whereas current harnesses predominantly rely on hand-crafted or globally fixed policies; this mismatch manifests as unnecessary computational overhead and, in adverse cases, reduced task success. To address this limitation, we formulate the task of enabling adaptive orchestration in harness systems as a causal learning problem and propose Counterfactual Harness Intervention Learning for Long-Horizon Agents (CHILL-Harness). CHILL-Harness intervenes at the orchestration layer to enable advantage-guided workflow adaptation, thereby improving reasoning and execution efficiency while preserving task performance. Specifically, we develop causal intervention effect learning as the effect-estimation component of CHILL-Harness to estimate intervention-relative workflow advantage from confidence-weighted execution evidence and identify advantageous workflow adaptations. We further introduce advantage-realizing causal orchestration as its realization component to adaptively allocate counterfactual reasoning and realize only workflow adjustments supported by sufficient expected advantage. Finally, we incorporate a success-preserving objective and advantage-margin authorization constraints into CHILL-Harness to promote reliable adaptation. Extensive experiments on heterogeneous long-horizon tasks spanning information seeking, software engineering, and terminal interaction show that CHILL-Harness consistently preserves or improves task success while substantially reducing token consumption and execution time.

## 내 메모


