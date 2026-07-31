---
type: research-source
item_id: 516
title: "David and Goliath: An Empirical Evaluation of Attacks and Defenses for QNNs at the Deep Edge"
source: "arxiv"
published: "2024-04-08T17:14:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2404.05688"
url: "https://arxiv.org/abs/2404.05688v2"
generated_by: codex-research-db
aliases:
  - "David and Goliath: An Empirical Evaluation of Attacks and Defenses for QNNs at the Deep Edge"
topics:
  - "edge-computing"
---

# David and Goliath: An Empirical Evaluation of Attacks and Defenses for QNNs at the Deep Edge

[원문 열기](https://arxiv.org/abs/2404.05688v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3NC2928C`)
- 발행일: 2024-04-08T17:14:32Z
- 저자: Miguel Costa, Sandro Pinto
- 식별자: `arxiv:2404.05688`

## 요약·초록

ML is shifting from the cloud to the edge. Edge computing reduces the surface exposing private data and enables reliable throughput guarantees in real-time applications. Of the panoply of devices deployed at the edge, resource-constrained MCUs, e.g., Arm Cortex-M, are more prevalent, orders of magnitude cheaper, and less power-hungry than application processors or GPUs. Thus, enabling intelligence at the deep edge is the zeitgeist, with researchers focusing on unveiling novel approaches to deploy ANNs on these constrained devices. Quantization is a well-established technique that has proved effective in enabling the deployment of neural networks on MCUs; however, it is still an open question to understand the robustness of QNNs in the face of adversarial examples. To fill this gap, we empirically evaluate the effectiveness of attacks and defenses from (full-precision) ANNs on (constrained) QNNs. Our evaluation includes three QNNs targeting TinyML applications, ten attacks, and six defenses. With this study, we draw a set of interesting findings. First, quantization increases the point distance to the decision boundary and leads the gradient estimated by some attacks to explode or vanish. Second, quantization can act as a noise attenuator or amplifier, depending on the noise magnitude, and causes gradient misalignment. Regarding adversarial defenses, we conclude that input pre-processing defenses show impressive results on small perturbations; however, they fall short as the perturbation increases. At the same time, train-based defenses increase the average point distance to the decision boundary, which holds after quantization. However, we argue that train-based defenses still need to smooth the quantization-shift and gradient misalignment phenomenons to counteract adversarial example transferability to QNNs. All artifacts are open-sourced to enable independent validation of results.

## 내 메모


