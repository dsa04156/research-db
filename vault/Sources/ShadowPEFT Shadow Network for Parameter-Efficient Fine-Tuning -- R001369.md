---
type: research-source
item_id: 1369
title: "ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning"
source: "arxiv"
published: "2026-04-21T09:17:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.19254"
url: "https://arxiv.org/abs/2604.19254v1"
generated_by: codex-research-db
aliases:
  - "ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning"
topics:
  - "edge-computing"
---

# ShadowPEFT: Shadow Network for Parameter-Efficient Fine-Tuning

[원문 열기](https://arxiv.org/abs/2604.19254v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W22T2DHQ`)
- 발행일: 2026-04-21T09:17:35Z
- 저자: Xianming Li, Zongxi Li, Tsz-fung Andrew Lee, Jing Li, Haoran Xie, Qing Li
- 식별자: `arxiv:2604.19254`

## 요약·초록

Parameter-efficient fine-tuning (PEFT) reduces the training cost of full-parameter fine-tuning for large language models (LLMs) by training only a small set of task-specific parameters while freezing the pretrained backbone. However, existing approaches, such as Low-Rank Adaptation (LoRA), achieve adaptation by inserting independent low-rank perturbations directly to individual weights, resulting in a local parameterization of adaptation. We propose ShadowPEFT, a centralized PEFT framework that instead performs layer-level refinement through a depth-shared shadow module. At each transformer layer, ShadowPEFT maintains a parallel shadow state and evolves it repeatedly for progressively richer hidden states. This design shifts adaptation from distributed weight-space perturbations to a shared layer-space refinement process. Since the shadow module is decoupled from the backbone, it can be reused across depth, independently pretrained, and optionally deployed in a detached mode, benefiting edge computing scenarios. Experiments on generation and understanding benchmarks show that ShadowPEFT matches or outperforms LoRA and DoRA under comparable trainable-parameter budgets. Additional analyses on shadow pretraining, cross-dataset transfer, parameter scaling, inference latency, and system-level evaluation suggest that centralized layer-space adaptation is a competitive and flexible alternative to conventional low-rank PEFT.

## 내 메모


