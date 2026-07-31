---
type: research-source
item_id: 1372
title: "When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano"
source: "arxiv"
published: "2026-04-18T15:52:05Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.17040"
url: "https://arxiv.org/abs/2604.17040v1"
generated_by: codex-research-db
aliases:
  - "When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano"
topics:
  - "edge-computing"
---

# When Spike Sparsity Does Not Translate to Deployed Cost: VS-WNO on Jetson Orin Nano

[원문 열기](https://arxiv.org/abs/2604.17040v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5TR7JKE5`)
- 발행일: 2026-04-18T15:52:05Z
- 저자: Jason Yoo, Shailesh Garg, Souvik Chakraborty, Syed Bahauddin Alam
- 식별자: `arxiv:2604.17040`

## 요약·초록

Spiking neural operators are appealing for neuromorphic edge computing because event-driven substrates can, in principle, translate sparse activity into lower latency and energy. Whether that advantage survives deployment on commodity edge-GPU software stacks, however, remains unclear. We study this question on a Jetson Orin Nano 8 GB using five pretrained variable-spiking wavelet neural operator (VS-WNO) checkpoints and five matched dense wavelet neural operator (WNO) checkpoints on the Darcy rectangular benchmark. On a reference-aligned path, VS-WNO exhibits substantial algorithmic sparsity, with mean spike rates decreasing from 54.26% at the first spiking layer to 18.15% at the fourth. On a deployment-style request path, however, this sparsity does not reduce deployed cost: VS-WNO reaches 59.6 ms latency and 228.0 mJ dynamic energy per inference, whereas dense WNO reaches 53.2 ms and 180.7 mJ, while also achieving slightly lower reference-path error (1.77% versus 1.81%). Nsight Systems indicates that the request path remains launch-dominated and dense rather than sparsity-aware: for VS-WNO, cudaLaunchKernel accounts for 81.6% of CUDA API time within the latency window, and dense convolution kernels account for 53.8% of GPU kernel time; dense WNO shows the same pattern. On this Jetson-class GPU stack, spike sparsity is measurable but does not reduce deployed cost because the runtime does not suppress dense work as spike activity decreases.

## 내 메모


