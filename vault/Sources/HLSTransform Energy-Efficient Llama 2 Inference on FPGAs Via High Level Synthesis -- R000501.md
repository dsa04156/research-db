---
type: research-source
item_id: 501
title: "HLSTransform: Energy-Efficient Llama 2 Inference on FPGAs Via High Level Synthesis"
source: "arxiv"
published: "2024-04-29T21:26:06Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.00738"
url: "https://arxiv.org/abs/2405.00738v1"
generated_by: codex-research-db
aliases:
  - "HLSTransform: Energy-Efficient Llama 2 Inference on FPGAs Via High Level Synthesis"
topics:
  - "edge-computing"
---

# HLSTransform: Energy-Efficient Llama 2 Inference on FPGAs Via High Level Synthesis

[원문 열기](https://arxiv.org/abs/2405.00738v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UEGMR8SE`)
- 발행일: 2024-04-29T21:26:06Z
- 저자: Andy He, Darren Key, Mason Bulling, Andrew Chang, Skyler Shapiro, Everett Lee
- 식별자: `arxiv:2405.00738`

## 요약·초록

Graphics Processing Units (GPUs) have become the leading hardware accelerator for deep learning applications and are used widely in training and inference of transformers; transformers have achieved state-of-the-art performance in many areas of machine learning and are especially used in most modern Large Language Models (LLMs). However, GPUs require large amounts of energy, which poses environmental concerns, demands high operational costs, and causes GPUs to be unsuitable for edge computing. We develop an accelerator for transformers, namely, Llama 2, an open-source state-of-the-art LLM, using high level synthesis (HLS) on Field Programmable Gate Arrays (FPGAs). HLS allows us to rapidly prototype FPGA designs without writing code at the register-transfer level (RTL). We name our method HLSTransform, and the FPGA designs we synthesize with HLS achieve up to a 12.75x reduction and 8.25x reduction in energy used per token on the Xilinx Virtex UltraScale+ VU9P FPGA compared to an Intel Xeon Broadwell E5-2686 v4 CPU and NVIDIA RTX 3090 GPU respectively, while increasing inference speeds by up to 2.46x compared to CPU and maintaining 0.53x the speed of an RTX 3090 GPU despite the GPU's 4 times higher base clock rate. With the lack of existing open-source FPGA accelerators for transformers, we open-source our code and document our steps for synthesis. We hope this work will serve as a step in democratizing the use of FPGAs in transformer inference and inspire research into energy-efficient inference methods as a whole. The code can be found on https://github.com/HLSTransform/submission.

## 내 메모


