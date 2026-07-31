---
type: research-source
item_id: 1004
title: "Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing"
source: "arxiv"
published: "2026-07-09T13:55:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.08497"
url: "https://arxiv.org/abs/2607.08497v1"
generated_by: codex-research-db
aliases:
  - "Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing"
topics:
  - "self-evolving-harness"
---

# Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, and Editing

[원문 열기](https://arxiv.org/abs/2607.08497v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VGPGDWGW`)
- 발행일: 2026-07-09T13:55:55Z
- 저자: Feng Wang, Canmiao Fu, Zhipeng Huang, Chen Li, Jing Lyu, Ge Li
- 식별자: `arxiv:2607.08497`

## 요약·초록

Recent unified multimodal models show a single architecture can jointly perform vision/language understanding and image generation/editing. However, they repeatedly feed all historical visual and textual inputs into a shared context window, limiting long-horizon multimodal dialogue due to visual token explosion and unreliable cross-turn referencing. We propose a Cognitive-structured Multimodal Agent that externalizes visual information into an Episodic Visual Memory and selectively reactivates relevant episodes during reasoning. The agent consists of a Perceptual Abstraction Engine for structured visual abstraction, a Cognitive Retrieval Engine for cross-turn memory retrieval, and a Multimodal Executive Controller for autonomous task inference and action planning. To address the lack of turn-level retrieval supervision in existing datasets, we develop a Unified Scenario Engine that programmatically generates structured multi-turn conversations with fine-grained retrieval annotations, enabling reinforcement learning to optimize abstraction and retrieval policies. We also construct a long-horizon visual-dialogue benchmark stratified by difficulty to evaluate episodic visual recall. Our 8B agent achieves 91.4% retrieval accuracy over 20-turn sessions, surpassing 32B baselines by +8.2% while nearly halving per-turn inference time (23.1s -> 12.7s). We further present the Cognitive-structured Multimodal Agent Harness (CMA-Harness), a tool-augmented deployment of the same cognitive structure integrating persistent multimodal memory, web access, image generation/editing/composition tools, and OpenAI-compatible serving. Structured memory and modular decision-making offer a more scalable, efficient paradigm for long-horizon multimodal agents than monolithic parameter scaling. Code: https://github.com/caseclose/cma-harness ; Project page: https://caseclose.github.io/cma-harness/

## 내 메모


