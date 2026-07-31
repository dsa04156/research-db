---
type: research-source
item_id: 88
title: "Leveraging ECRAM for Edge Continual Learning"
source: "arxiv"
published: "2026-07-22T02:00:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19661"
url: "https://arxiv.org/abs/2607.19661v1"
generated_by: codex-research-db
aliases:
  - "Leveraging ECRAM for Edge Continual Learning"
topics:
  - "edge-computing"
---

# Leveraging ECRAM for Edge Continual Learning

[원문 열기](https://arxiv.org/abs/2607.19661v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`R8FC4KIJ`)
- 발행일: 2026-07-22T02:00:22Z
- 저자: Nabila Tasnim, Haoran Liu, Qing Cao, Saugata Ghose
- 식별자: `arxiv:2607.19661`

## 요약·초록

Several edge computing platforms, such as autonomous vehicles and smart sensing devices, need to adapt to dynamic environments in real time by learning from new data in the field. Continual learning has emerged as a promising solution for edge training, by incorporating techniques that successfully combine a highly summarized version of previously trained data (to avoid catastrophic forgetting) with recently sensed data. However, as is the case with other ML algorithms, continual learning generates significant data movement between general-purpose CPUs/GPUs and memory, impacting the suitability of continual learning for edge platforms. In-memory computing (IMC; also known as processing-using-memory) can curtail this waste and make continual learning feasible at the edge, but it faces two unique challenges: (1) IMC architectures make use of noisy computation operations that significantly harm training accuracy; and (2) IMC architectures have poor and often incomplete support for resource-efficient training. To address these challenges, we propose CLASP (the Continual Learning Acceleration System Platform), which to our knowledge is the first end-to-end system with IMC acceleration for continual learning. The hardware and software of CLASP are co-designed to support a wide range of continual learning algorithms, through software-visible assembly-level instructions that can be incorporated without constraints into ML-based algorithms. CLASP is designed around a back-end-of-line (BEOL) compatible ECRAM device that we fabricate, which can overcome the challenges of IMC-based training using other emerging memory devices. We show that CLASP with ECRAM approaches the accuracy of in-GPU training, while delivering a speedup of 67x and energy savings of 132x for learning without forgetting and experience replay using MNIST.

## 내 메모


