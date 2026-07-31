---
type: research-source
item_id: 690
title: "SuperSONIC: Cloud-Native Infrastructure for ML Inferencing"
source: "arxiv"
published: "2025-06-25T17:52:26Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3708035.3736049"
url: "https://arxiv.org/abs/2506.20657v1"
generated_by: codex-research-db
aliases:
  - "SuperSONIC: Cloud-Native Infrastructure for ML Inferencing"
topics:
  - "kubernetes"
---

# SuperSONIC: Cloud-Native Infrastructure for ML Inferencing

[원문 열기](https://arxiv.org/abs/2506.20657v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`A5D6CPHR`)
- 발행일: 2025-06-25T17:52:26Z
- 저자: Dmitry Kondratyev, Benedikt Riedel, Yuan-Tang Chou, Miles Cochran-Branson, Noah Paladino, David Schultz, Mia Liu, Javier Duarte, Philip Harris, Shih-Chieh Hsu
- 식별자: `doi:10.1145/3708035.3736049`

## 요약·초록

The increasing computational demand from growing data rates and complex machine learning (ML) algorithms in large-scale scientific experiments has driven the adoption of the Services for Optimized Network Inference on Coprocessors (SONIC) approach. SONIC accelerates ML inference by offloading it to local or remote coprocessors to optimize resource utilization. Leveraging its portability to different types of coprocessors, SONIC enhances data processing and model deployment efficiency for cutting-edge research in high energy physics (HEP) and multi-messenger astrophysics (MMA). We developed the SuperSONIC project, a scalable server infrastructure for SONIC, enabling the deployment of computationally intensive tasks to Kubernetes clusters equipped with graphics processing units (GPUs). Using NVIDIA Triton Inference Server, SuperSONIC decouples client workflows from server infrastructure, standardizing communication, optimizing throughput, load balancing, and monitoring. SuperSONIC has been successfully deployed for the CMS and ATLAS experiments at the CERN Large Hadron Collider (LHC), the IceCube Neutrino Observatory (IceCube), and the Laser Interferometer Gravitational-Wave Observatory (LIGO) and tested on Kubernetes clusters at Purdue University, the National Research Platform (NRP), and the University of Chicago. SuperSONIC addresses the challenges of the Cloud-native era by providing a reusable, configurable framework that enhances the efficiency of accelerator-based inference deployment across diverse scientific domains and industries.

## 내 메모


