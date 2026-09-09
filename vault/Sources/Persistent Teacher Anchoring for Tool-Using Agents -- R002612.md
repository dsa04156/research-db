---
type: research-source
item_id: 2612
title: "Persistent Teacher Anchoring for Tool-Using Agents"
source: "arxiv"
published: "2026-09-04T06:09:50Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04773"
url: "https://arxiv.org/abs/2609.04773v1"
generated_by: codex-research-db
aliases:
  - "Persistent Teacher Anchoring for Tool-Using Agents"
topics:
  - "ai-agents"
---

# Persistent Teacher Anchoring for Tool-Using Agents

[원문 열기](https://arxiv.org/abs/2609.04773v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KPHCKN5S`)
- 발행일: 2026-09-04T06:09:50Z
- 저자: Hyun Bin Park, Kyungho Song, Sangmin Lee, Du-Seong Chang
- 식별자: `arxiv:2609.04773`

## 요약·초록

Distillation is common in LLM post-training, where on-policy knowledge distillation (OPKD) uses student-generated trajectories to prepare the student for downstream RL. At each state, the student matches a next-token distribution supplied by the teacher. As the rollout enters states the teacher would not visit, the teacher-student distribution gap can accumulate. In tool use, this gap becomes consequential because student-written calls execute before supervision and their observations shape later prefixes. Proposer-verifier generation addresses this drift by letting the teacher decide which student-proposed text is retained during generation. Existing formulations govern text but leave tool execution outside their scope. We propose Persistent Teacher Anchoring (PTA), a student-induced but teacher-committed rollout construction. PTA retains chunk-level verification and adds turn-level commitment, allowing a call to reach the environment only after the teacher has verified the entire turn. Treating verified chunks as atomic generation units, we introduce persistent lookahead, which fills idle rollout capacity by advancing future samples and carrying unfinished ones across student updates under the fixed verifier. Across Search-R1-style retrieval and DeepEyes-style perception RL, applying PTA before downstream RL improves macro best@4 by 2.5 and 2.8 points over OPKD under the same downstream RL budget, while lookahead improves throughput by 24%.

## 내 메모


