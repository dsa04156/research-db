---
type: research-source
item_id: 904
title: "Lorica: A Synergistic Fine-Tuning Framework for Advancing Personalized Adversarial Robustness"
source: "arxiv"
published: "2025-06-04T03:31:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2506.05402"
url: "https://arxiv.org/abs/2506.05402v3"
generated_by: codex-research-db
aliases:
  - "Lorica: A Synergistic Fine-Tuning Framework for Advancing Personalized Adversarial Robustness"
topics:
  - "edge-computing"
---

# Lorica: A Synergistic Fine-Tuning Framework for Advancing Personalized Adversarial Robustness

[원문 열기](https://arxiv.org/abs/2506.05402v3)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`U5762SQE`)
- 발행일: 2025-06-04T03:31:32Z
- 저자: Tianyu Qi, Lei Xue, Yufeng Zhan, Xiaobo Ma
- 식별자: `arxiv:2506.05402`

## 요약·초록

The growing use of large pre-trained models in edge computing has made model inference on mobile clients both feasible and popular. Yet these devices remain vulnerable to adversarial attacks, threatening model robustness and security. Federated adversarial training (FAT) offers a promising solution by enhancing robustness while preserving client privacy. However, FAT often yields a generalized global model that struggles with heterogeneous client data, leading to limited personalization and significant communication overhead. In this paper, we propose \textit{Lorica}, a personalized synergistic adversarial training framework that delivers customized defense models through a two-phase process. In Phase 1, \textit{Lorica} applies LoRA-FA for local adversarial fine-tuning, enabling personalized robustness while reducing communication by uploading only LoRA-FA parameters. In Phase 2, a forward-gating selection strategy improves benign accuracy, further refining the personalized model. This yields tailored defense models that effectively balance robustness and accuracy. Extensive experiments on benchmark datasets demonstrate that \textit{Lorica} can achieve up to 68$\times$ improvements in communication efficiency compared to state-of-the-art algorithms, while achieving up to 29.9\% and 52.2\% enhancements in adversarial robustness and benign accuracy, respectively.

## 내 메모


