---
type: research-source
item_id: 93
title: "Emulated Integrity Replica: Enabling Self-Healing on FPGA SoCs via Hierarchical Twins"
source: "arxiv"
published: "2026-07-14T03:14:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.12298"
url: "https://arxiv.org/abs/2607.12298v1"
generated_by: codex-research-db
aliases:
  - "Emulated Integrity Replica: Enabling Self-Healing on FPGA SoCs via Hierarchical Twins"
topics:
  - "edge-computing"
---

# Emulated Integrity Replica: Enabling Self-Healing on FPGA SoCs via Hierarchical Twins

[원문 열기](https://arxiv.org/abs/2607.12298v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`E6NVITR3`)
- 발행일: 2026-07-14T03:14:00Z
- 저자: Arsalan Ali Malik, Ali Suvizi, Guru Venkataramani, Aydin Aysu
- 식별자: `arxiv:2607.12298`

## 요약·초록

Convolutional neural networks (CNNs) are increasingly being deployed on system-on-chip (SoC) platforms, where hardware-accelerated inference enables low-latency edge computing. Achieving fault tolerance on these devices remains challenging because conventional redundancy (dual/triple modular redundancy, DMR/TMR) incurs high resource cost, while software-centric methods (e.g., algorithm-based fault tolerance (ABFT), checkpoint-restart, instruction-level duplication, and software watchdogs/assertions) introduce nontrivial latency/energy overheads, reduce model accuracy, or provide inadequate coverage for accelerator-induced faults. In this paper, we propose Emulated Integrity Replica (EIR), a hierarchical digital-twin framework for FPGA SoCs that provides autonomous fault detection and recovery. Unlike DMR/TMR, which replicates hardware logic and incurs proportional area and power overheads, EIR avoids fabric-level duplication by exploiting temporal slack in the processing system (PS). During accelerator execution in the programmable logic (PL), the PS typically remains underutilized; EIR capitalizes on these idle cycles to host two complementary twins: (i) Rabbit: a coarse-grained behavioral model for rapid fault detection and (ii) Tortoise: a fine-grained gate-level model that performs precise recovery from checkpointed states. The accelerator state is captured periodically, leveraging the accelerator's execution-speed profiling to balance performance overhead and resilience. Experiments on representative workloads show that EIR achieves high empirical fault coverage relative to a DMR baseline while reducing energy and area under the evaluated fault model and workload assumptions, indicating a practical path to resilient edge-AI deployments under strict resource budgets.

## 내 메모


