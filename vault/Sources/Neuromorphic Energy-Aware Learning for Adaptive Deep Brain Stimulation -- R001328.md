---
type: research-source
item_id: 1328
title: "Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation"
source: "arxiv"
published: "2026-06-26T20:48:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.28600"
url: "https://arxiv.org/abs/2606.28600v1"
generated_by: codex-research-db
aliases:
  - "Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation"
topics:
  - "edge-computing"
---

# Neuromorphic Energy-Aware Learning for Adaptive Deep Brain Stimulation

[원문 열기](https://arxiv.org/abs/2606.28600v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PQ52NZ9B`)
- 발행일: 2026-06-26T20:48:43Z
- 저자: Binh Nguyen, Colleen Josephson, Mircea Teodorescu, Gert Cauwenberghs, Jason Eshraghian
- 식별자: `arxiv:2606.28600`

## 요약·초록

Neuromorphic and edge computing research has focused on reducing the inference cost of neural network controllers, yet in physical closed-loop systems the actuator can rival or exceed an efficient controller in energy. An efficient controller is therefore necessary but not sufficient, because the actuator becomes the cost worth reducing once inference no longer dominates it. Here, we introduce energy-aware learning, an approach that incorporates actuator energy directly into the reinforcement learning reward, and demonstrate it in closed-loop deep brain stimulation (DBS) for Parkinson's disease. A deep spiking Q-network, trained in a biophysical cortico-basal ganglia-thalamic circuit model, learns to suppress pathological alpha-beta oscillations by 45.2% while reducing stimulation charge by 80.0% relative to continuous DBS. Sparsity-constrained knowledge distillation compresses the policy onto the SynSense XyloAudio 3 neuromorphic processor at 0.52 mW inference power, yielding 28.1x lower energy per inference than an equivalent artificial neural network on conventional edge hardware. By co-optimizing stimulation energy and inference efficiency, the framework addresses both major power demands in implantable neuromodulation.

## 내 메모


