---
type: research-source
item_id: 2261
title: "Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction"
source: "arxiv"
published: "2026-08-23T02:22:31Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.22176"
url: "https://arxiv.org/abs/2608.22176v1"
generated_by: codex-research-db
aliases:
  - "Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction"
topics:
  - "ai-agents"
---

# Role-Specialized Mixture-of-Agents with Open-Weight LLMs for Clinical Prediction

[원문 열기](https://arxiv.org/abs/2608.22176v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`86J5N3Z9`)
- 발행일: 2026-08-23T02:22:31Z
- 저자: Jun Hou, Yi Fang, Xuan Wang
- 식별자: `arxiv:2608.22176`

## 요약·초록

Large Language Models (LLMs) are increasingly applied to clinical prediction tasks such as in-hospital mortality and readmission from electronic health records (EHRs). Privacy and compliance constraints motivate systems that can be deployed locally, which has increased interest in open-weight multi-agent designs. However, most medical multi-agent systems are evaluated as a single block, leaving unclear which agent role contributes to prediction and whether retrieval drives observed gains. We study a role-specialized Mixture-of-Agents (MoA) that combines medical knowledge retrieval with contrastive similar-patient reasoning. By varying the role design while holding the retrieval setup fixed, we localize the main effect to the final integrator. Pairing large open-weight analysts with a small open-weight integrator matches closed-model prompting on F1 for mortality prediction while flagging substantially more true high-risk patients. Mechanism analysis shows the role assignment directly yields a high-recall operating point without threshold tuning. The effect is task-dependent, with smaller gains for readmission because the available records correlate weakly with this longer-horizon outcome. These results position role design as a key factor in privacy-constrained, training-free clinical LLM prediction.

## 내 메모


