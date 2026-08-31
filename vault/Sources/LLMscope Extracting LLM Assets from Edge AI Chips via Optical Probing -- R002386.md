---
type: research-source
item_id: 2386
title: "LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing"
source: "kurate"
published: "2026-08-26T03:06:12Z"
first_seen: "2026-08-28"
review_status: "pending"
canonical_key: "arxiv:2608.25321"
url: "http://arxiv.org/abs/2608.25321v1"
generated_by: codex-research-db
aliases:
  - "LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing"
topics:
  - "edge-computing"
---

# LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing

[원문 열기](http://arxiv.org/abs/2608.25321v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-28|2026-08-28]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`ZW9T2E4P`)
- 발행일: 2026-08-26T03:06:12Z
- 저자: Dev Mehta, Lily Dukette, William Folan, Olivia Kochol, Noah Solomon, Shahin Tajik, Fatemeh Ganji
- 식별자: `arxiv:2608.25321`

## 요약·초록

The move of LLM inference to edge AI accelerators introduces new physical vulnerabilities. During execution, model parameters and intermediate inference states are repeatedly loaded into and processed on the chip, making them suscep- tible to physical side-channel attacks. In this work, by deploying laser voltage imaging, we show that one can extract LLM assets during inference, namely embeddings, attention, and quantized MLP weights, activations, and other inference states, from localized memories and compute subcircuits. To validate our claims, we perform an attack on an FPGA-based LLM accelerator. Since such accelerators reuse the same buffers and compute subcircuits across addresses, tiles, modules, and layers, reading asset values comes down to probing different memories during inference. We demonstrate full recovery of the targeted values; however, we also establish a methodology to recover asset values even if some weights or bits remain unread. We further derive lower bounds that relate imaging effort to asset dimensions and show that even direct recovery scales linearly with the size of the targeted asset

## 내 메모


