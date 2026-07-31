---
type: research-source
item_id: 1170
title: "Enabling Adversarial Robustness in AI Models through Kubeflow MLOps"
source: "arxiv"
published: "2026-05-14T12:45:36Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.15249"
url: "https://arxiv.org/abs/2605.15249v1"
generated_by: codex-research-db
aliases:
  - "Enabling Adversarial Robustness in AI Models through Kubeflow MLOps"
topics:
  - "kubernetes"
---

# Enabling Adversarial Robustness in AI Models through Kubeflow MLOps

[원문 열기](https://arxiv.org/abs/2605.15249v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZKG3F3E7`)
- 발행일: 2026-05-14T12:45:36Z
- 저자: Stavros Bouras, Ioannis Korontanis, Antonios Makris, Konstantinos Tserpes
- 식별자: `arxiv:2605.15249`

## 요약·초록

AI models are increasingly deployed in cloud-native environments to support scalable and automated services. However, while platforms such as Kubernetes provide strong infrastructure orchestration, security mechanisms specifically designed to protect deployed AI models remain limited. This paper presents security measures for AI models deployed in Kubernetes clusters. The proposed architecture integrates Kubeflow-based MLOps to automatically detect adversarial attacks during the inference phase and trigger defense mechanisms that preserve the model's accuracy and reliability. Specifically, a Fast Gradient Sign Method (FGSM) attack is applied at inference time, and a Projected Gradient Descent (PGD)-based adversarial training defense is automatically deployed when a degradation in accuracy is detected. The experimental results indicate that the deployed defense robustifies the model, significantly recovering accuracy relative to the degradation caused by the attack.

## 내 메모


