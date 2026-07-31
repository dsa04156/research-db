---
type: research-source
item_id: 508
title: "Rapid Deployment of DNNs for Edge Computing via Structured Pruning at Initialization"
source: "arxiv"
published: "2024-04-22T10:57:54Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/ccgrid59990.2024.00044"
url: "https://arxiv.org/abs/2404.16877v1"
generated_by: codex-research-db
aliases:
  - "Rapid Deployment of DNNs for Edge Computing via Structured Pruning at Initialization"
topics:
  - "edge-computing"
---

# Rapid Deployment of DNNs for Edge Computing via Structured Pruning at Initialization

[원문 열기](https://arxiv.org/abs/2404.16877v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`S8V9QRP2`)
- 발행일: 2024-04-22T10:57:54Z
- 저자: Bailey J. Eccles, Leon Wong, Blesson Varghese
- 식별자: `doi:10.1109/ccgrid59990.2024.00044`

## 요약·초록

Edge machine learning (ML) enables localized processing of data on devices and is underpinned by deep neural networks (DNNs). However, DNNs cannot be easily run on devices due to their substantial computing, memory and energy requirements for delivering performance that is comparable to cloud-based ML. Therefore, model compression techniques, such as pruning, have been considered. Existing pruning methods are problematic for edge ML since they: (1) Create compressed models that have limited runtime performance benefits (using unstructured pruning) or compromise the final model accuracy (using structured pruning), and (2) Require substantial compute resources and time for identifying a suitable compressed DNN model (using neural architecture search). In this paper, we explore a new avenue, referred to as Pruning-at-Initialization (PaI), using structured pruning to mitigate the above problems. We develop Reconvene, a system for rapidly generating pruned models suited for edge deployments using structured PaI. Reconvene systematically identifies and prunes DNN convolution layers that are least sensitive to structured pruning. Reconvene rapidly creates pruned DNNs within seconds that are up to 16.21x smaller and 2x faster while maintaining the same accuracy as an unstructured PaI counterpart.

## 내 메모


