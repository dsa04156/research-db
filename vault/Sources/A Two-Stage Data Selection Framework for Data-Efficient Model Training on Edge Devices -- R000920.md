---
type: research-source
item_id: 920
title: "A Two-Stage Data Selection Framework for Data-Efficient Model Training on Edge Devices"
source: "arxiv"
published: "2025-05-22T11:53:48Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3711896.3736823"
url: "https://arxiv.org/abs/2505.16563v2"
generated_by: codex-research-db
aliases:
  - "A Two-Stage Data Selection Framework for Data-Efficient Model Training on Edge Devices"
topics:
  - "edge-computing"
---

# A Two-Stage Data Selection Framework for Data-Efficient Model Training on Edge Devices

[원문 열기](https://arxiv.org/abs/2505.16563v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NBDCM36A`)
- 발행일: 2025-05-22T11:53:48Z
- 저자: Chen Gong, Rui Xing, Zhenzhe Zheng, Fan Wu
- 식별자: `doi:10.1145/3711896.3736823`

## 요약·초록

The demand for machine learning (ML) model training on edge devices is escalating due to data privacy and personalized service needs. However, we observe that current on-device model training is hampered by the under-utilization of on-device data, due to low training throughput, limited storage and diverse data importance. To improve data resource utilization, we propose a two-stage data selection framework {\sf Titan} to select the most important data batch from streaming data for model training with guaranteed efficiency and effectiveness. Specifically, in the first stage, {\sf Titan} filters out a candidate dataset with potentially high importance in a coarse-grained manner.In the second stage of fine-grained selection, we propose a theoretically optimal data selection strategy to identify the data batch with the highest model performance improvement to current training round. To further enhance time-and-resource efficiency, {\sf Titan} leverages a pipeline to co-execute data selection and model training, and avoids resource conflicts by exploiting idle computing resources. We evaluate {\sf Titan} on real-world edge devices and three representative edge computing tasks with diverse models and data modalities. Empirical results demonstrate that {\sf Titan} achieves up to $43\%$ reduction in training time and $6.2\%$ increase in final accuracy with minor system overhead, such as data processing delay, memory footprint and energy consumption.

## 내 메모


