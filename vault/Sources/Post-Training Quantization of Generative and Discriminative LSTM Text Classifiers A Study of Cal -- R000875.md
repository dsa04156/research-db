---
type: research-source
item_id: 875
title: "Post-Training Quantization of Generative and Discriminative LSTM Text Classifiers: A Study of Calibration, Class Balance, and Robustness"
source: "arxiv"
published: "2025-07-13T15:48:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.09687"
url: "https://arxiv.org/abs/2507.09687v1"
generated_by: codex-research-db
aliases:
  - "Post-Training Quantization of Generative and Discriminative LSTM Text Classifiers: A Study of Calibration, Class Balance, and Robustness"
topics:
  - "edge-computing"
---

# Post-Training Quantization of Generative and Discriminative LSTM Text Classifiers: A Study of Calibration, Class Balance, and Robustness

[원문 열기](https://arxiv.org/abs/2507.09687v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BZRUWT2Q`)
- 발행일: 2025-07-13T15:48:16Z
- 저자: Md Mushfiqur Rahaman, Elliot Chang, Tasmiah Haque, Srinjoy Das
- 식별자: `arxiv:2507.09687`

## 요약·초록

Text classification plays a pivotal role in edge computing applications like industrial monitoring, health diagnostics, and smart assistants, where low latency and high accuracy are both key requirements. Generative classifiers, in particular, have been shown to exhibit robustness to out-of-distribution and noisy data, which is an extremely critical consideration for deployment in such real-time edge environments. However, deploying such models on edge devices faces computational and memory constraints. Post Training Quantization (PTQ) reduces model size and compute costs without retraining, making it ideal for edge deployment. In this work, we present a comprehensive comparative study of generative and discriminative Long Short Term Memory (LSTM)-based text classification models with PTQ using the Brevitas quantization library. We evaluate both types of classifier models across multiple bitwidths and assess their robustness under regular and noisy input conditions. We find that while discriminative classifiers remain robust, generative ones are more sensitive to bitwidth, calibration data used during PTQ, and input noise during quantized inference. We study the influence of class imbalance in calibration data for both types of classifiers, comparing scenarios with evenly and unevenly distributed class samples including their effect on weight adjustments and activation profiles during PTQ. Using test statistics derived from nonparametric hypothesis testing, we identify that using class imbalanced data during calibration introduces insufficient weight adaptation at lower bitwidths for generative LSTM classifiers, thereby leading to degraded performance. This study underscores the role of calibration data in PTQ and when generative classifiers succeed or fail under noise, aiding deployment in edge environments.

## 내 메모


