---
type: research-source
item_id: 2248
title: "Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner"
source: "arxiv"
published: "2026-08-24T13:56:01Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.23268"
url: "https://arxiv.org/abs/2608.23268v1"
generated_by: codex-research-db
aliases:
  - "Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner"
topics:
  - "ai-agents"
---

# Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic Learner

[원문 열기](https://arxiv.org/abs/2608.23268v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`R8I4AIHE`)
- 발행일: 2026-08-24T13:56:01Z
- 저자: Jieke Wang, Tiancheng Shen, Yibo Yang, Ming-Hsuan Yang
- 식별자: `arxiv:2608.23268`

## 요약·초록

Frontier multimodal large language models (MLLMs) deliver impressive perception yet still falter on scientific and mathematical reasoning. Parameter-level adaptation is unavailable for closed-weight or on-device backbones, and stateless prompting forfeits any compounding benefit from problems already solved. We propose \textbf{DG-Mem}, a dual-grained agentic memory framework that augments a frozen MLLM with a non-parametric, externally stored memory built once from training-time rollouts and consulted read-only at test time. Motivated by the Complementary Learning Systems (CLS) account of human memory, DG-Mem factors its store into an instance-grounded exemplar memory and a category-level schema memory of IF-THEN rules, with a transient reflection store mediating their construction so that schemas are synthesized only from abstract reflections, never from exemplar text. Two design choices distinguish DG-Mem: an online concept categorizer that grows the category space incrementally during training rather than committing to a predefined taxonomy, and a Shapley context attribution procedure that decomposes correctness across the entire retrieved rule set and yields a per-rule utility that re-weights retrieval at test time. The pipeline introduces no gradient updates and is deployable on closed-weight or on-device backbones. Across MathVista, MMMU, and MMMU-Pro on four open-weight and proprietary backbones (Qwen3.5-27B, Qwen3.5-122B-A10B, GPT-5-Nano, Gemini-3-Flash), DG-Mem improves consistently over no-memory and competitive memory baselines.

## 내 메모


