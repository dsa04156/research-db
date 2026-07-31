---
type: research-source
item_id: 457
title: "AdaPI: Facilitating DNN Model Adaptivity for Efficient Private Inference in Edge Computing"
source: "arxiv"
published: "2024-07-08T05:58:49Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.05633"
url: "https://arxiv.org/abs/2407.05633v1"
generated_by: codex-research-db
aliases:
  - "AdaPI: Facilitating DNN Model Adaptivity for Efficient Private Inference in Edge Computing"
topics:
  - "edge-computing"
---

# AdaPI: Facilitating DNN Model Adaptivity for Efficient Private Inference in Edge Computing

[원문 열기](https://arxiv.org/abs/2407.05633v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IS354TQ2`)
- 발행일: 2024-07-08T05:58:49Z
- 저자: Tong Zhou, Jiahui Zhao, Yukui Luo, Xi Xie, Wujie Wen, Caiwen Ding, Xiaolin Xu
- 식별자: `arxiv:2407.05633`

## 요약·초록

Private inference (PI) has emerged as a promising solution to execute computations on encrypted data, safeguarding user privacy and model parameters in edge computing. However, existing PI methods are predominantly developed considering constant resource constraints, overlooking the varied and dynamic resource constraints in diverse edge devices, like energy budgets. Consequently, model providers have to design specialized models for different devices, where all of them have to be stored on the edge server, resulting in inefficient deployment. To fill this gap, this work presents AdaPI, a novel approach that achieves adaptive PI by allowing a model to perform well across edge devices with diverse energy budgets. AdaPI employs a PI-aware training strategy that optimizes the model weights alongside weight-level and feature-level soft masks. These soft masks are subsequently transformed into multiple binary masks to enable adjustments in communication and computation workloads. Through sequentially training the model with increasingly dense binary masks, AdaPI attains optimal accuracy for each energy budget, which outperforms the state-of-the-art PI methods by 7.3\% in terms of test accuracy on CIFAR-100. The code of AdaPI can be accessed via https://github.com/jiahuiiiiii/AdaPI.

## 내 메모


