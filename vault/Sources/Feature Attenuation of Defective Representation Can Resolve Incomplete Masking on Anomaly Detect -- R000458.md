---
type: research-source
item_id: 458
title: "Feature Attenuation of Defective Representation Can Resolve Incomplete Masking on Anomaly Detection"
source: "arxiv"
published: "2024-07-05T15:44:53Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.04597"
url: "https://arxiv.org/abs/2407.04597v1"
generated_by: codex-research-db
aliases:
  - "Feature Attenuation of Defective Representation Can Resolve Incomplete Masking on Anomaly Detection"
topics:
  - "edge-computing"
---

# Feature Attenuation of Defective Representation Can Resolve Incomplete Masking on Anomaly Detection

[원문 열기](https://arxiv.org/abs/2407.04597v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JGZM6KGE`)
- 발행일: 2024-07-05T15:44:53Z
- 저자: YeongHyeon Park, Sungho Kang, Myung Jin Kim, Hyeong Seok Kim, Juneho Yi
- 식별자: `arxiv:2407.04597`

## 요약·초록

In unsupervised anomaly detection (UAD) research, while state-of-the-art models have reached a saturation point with extensive studies on public benchmark datasets, they adopt large-scale tailor-made neural networks (NN) for detection performance or pursued unified models for various tasks. Towards edge computing, it is necessary to develop a computationally efficient and scalable solution that avoids large-scale complex NNs. Motivated by this, we aim to optimize the UAD performance with minimal changes to NN settings. Thus, we revisit the reconstruction-by-inpainting approach and rethink to improve it by analyzing strengths and weaknesses. The strength of the SOTA methods is a single deterministic masking approach that addresses the challenges of random multiple masking that is inference latency and output inconsistency. Nevertheless, the issue of failure to provide a mask to completely cover anomalous regions is a remaining weakness. To mitigate this issue, we propose Feature Attenuation of Defective Representation (FADeR) that only employs two MLP layers which attenuates feature information of anomaly reconstruction during decoding. By leveraging FADeR, features of unseen anomaly patterns are reconstructed into seen normal patterns, reducing false alarms. Experimental results demonstrate that FADeR achieves enhanced performance compared to similar-scale NNs. Furthermore, our approach exhibits scalability in performance enhancement when integrated with other single deterministic masking methods in a plug-and-play manner.

## 내 메모


