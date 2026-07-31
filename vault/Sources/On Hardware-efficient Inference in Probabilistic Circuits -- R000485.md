---
type: research-source
item_id: 485
title: "On Hardware-efficient Inference in Probabilistic Circuits"
source: "arxiv"
published: "2024-05-22T13:38:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.13639"
url: "https://arxiv.org/abs/2405.13639v1"
generated_by: codex-research-db
aliases:
  - "On Hardware-efficient Inference in Probabilistic Circuits"
topics:
  - "edge-computing"
---

# On Hardware-efficient Inference in Probabilistic Circuits

[원문 열기](https://arxiv.org/abs/2405.13639v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZAQPGSAF`)
- 발행일: 2024-05-22T13:38:47Z
- 저자: Lingyun Yao, Martin Trapp, Jelin Leslin, Gaurav Singh, Peng Zhang, Karthekeyan Periasamy, Martin Andraud
- 식별자: `arxiv:2405.13639`

## 요약·초록

Probabilistic circuits (PCs) offer a promising avenue to perform embedded reasoning under uncertainty. They support efficient and exact computation of various probabilistic inference tasks by design. Hence, hardware-efficient computation of PCs is highly interesting for edge computing applications. As computations in PCs are based on arithmetic with probability values, they are typically performed in the log domain to avoid underflow. Unfortunately, performing the log operation on hardware is costly. Hence, prior work has focused on computations in the linear domain, resulting in high resolution and energy requirements. This work proposes the first dedicated approximate computing framework for PCs that allows for low-resolution logarithm computations. We leverage Addition As Int, resulting in linear PC computation with simple hardware elements. Further, we provide a theoretical approximation error analysis and present an error compensation mechanism. Empirically, our method obtains up to 357x and 649x energy reduction on custom hardware for evidence and MAP queries respectively with little or no computational error.

## 내 메모


