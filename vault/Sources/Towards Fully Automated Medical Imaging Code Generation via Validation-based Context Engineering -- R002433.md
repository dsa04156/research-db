---
type: research-source
item_id: 2433
title: "Towards Fully Automated Medical Imaging Code Generation via Validation-based Context Engineering"
source: "arxiv"
published: "2026-08-29T03:10:00Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.29016"
url: "https://arxiv.org/abs/2608.29016v1"
generated_by: codex-research-db
aliases:
  - "Towards Fully Automated Medical Imaging Code Generation via Validation-based Context Engineering"
topics:
  - "self-evolving-harness"
---

# Towards Fully Automated Medical Imaging Code Generation via Validation-based Context Engineering

[원문 열기](https://arxiv.org/abs/2608.29016v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FUBUFWXZ`)
- 발행일: 2026-08-29T03:10:00Z
- 저자: Zixiao Zhao, Jing Sun, Zhe Hou, Cheng-Hao Cai, Qian Liu, Mengze Li, Zijian Zhang, Jin Song Dong
- 식별자: `arxiv:2608.29016`

## 요약·초록

Large language models (LLMs) have demonstrated considerable promise in program generation for small-scale and conventional application development; however, they remain limited when applied to complex, domain-specific tasks such as medical image processing. General-purpose models lack explicit domain knowledge and robust validation mechanisms to ensure correctness, often requiring substantial human intervention to produce reliable processing pipelines. To address these limitations, we propose AutoMedImg, a multi-agent framework for fully automated medical image processing code generation. AutoMedImg orchestrates specialised agents across two phases: a Planning Phase that performs dataset analysis and architecture design with semantic and formal verification, and a Coding Phase that generates modules in parallel with static checking, execution testing, and assembly validation. This multi-stage validation mitigates error propagation throughout generation, while comprehensive auto-context engineering combining domain-specific knowledge bases, shared memory, and validation feedback automates context construction without manual prompting. A cross-project adaptive pipeline synthesis mechanism further accumulates validated pipelines and retrieves proven components for new tasks based on project similarity, enhancing generation efficiency through cross-project learning. Extensive evaluation across six diverse and well-established medical imaging datasets with five backbone LLMs demonstrates that AutoMedImg achieves zero human intervention, with Dice scores of up to 0.90 for segmentation tasks and 99% accuracy for classification.

## 내 메모


