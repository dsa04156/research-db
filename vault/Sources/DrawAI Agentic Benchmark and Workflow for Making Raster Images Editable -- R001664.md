---
type: research-source
item_id: 1664
title: "DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable"
source: "arxiv"
published: "2026-08-01T09:05:06Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00548"
url: "https://arxiv.org/abs/2608.00548v1"
generated_by: codex-research-db
aliases:
  - "DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable"
topics:
  - "self-evolving-harness"
---

# DrawAI: Agentic Benchmark and Workflow for Making Raster Images Editable

[원문 열기](https://arxiv.org/abs/2608.00548v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6DXBCZ93`)
- 발행일: 2026-08-01T09:05:06Z
- 저자: Pu Cao, Qingye Kong, Xuedan Yin, Xuekun Zhao, Rupeng Yan, Qing Song, Yao Zhang, Lu Yang
- 식별자: `arxiv:2608.00548`

## 요약·초록

Recent image-generation models and multimodal agents can produce high-quality visuals for increasingly complex visual communication tasks. Yet their raster outputs remain difficult to use directly because meaningful content and relationships are flattened into pixels, preventing users from inspecting, modifying, rearranging, or reusing individual components. We formulate image-to-editable reconstruction, which recovers a structured, directly manipulable artifact from a raster image while preserving its visual and semantic content. The central challenge is to jointly satisfy Fidelity and Editability, which often trade off in practice. To study this task, we introduce DrawAI, comprising an agentic benchmark, DrawAI-Bench, and a reconstruction workflow, DrawAI-Flow. DrawAI-Bench spans scientific figures, presentation slides, posters, and diagrams, combining real and AI-generated images to reflect practical visual-creation scenarios. It evaluates Fidelity and Editability through a hybrid protocol of 39 criteria: deterministic rule-based metrics measure properties with direct correspondences, while asset-specific vision-language rubrics capture semantic and perceptual qualities for which exact matching is misleading. Besides, we propose DrawAI-Flow, a two-stage agentic workflow in which a Parser Agent turns extracted elements evidence into an explicit reconstruction plan, and a Reconstruction Agent realizes the plan as executable graphics code through an iterative code-render-validate-revise loop. On DrawAI-Bench, we systematically evaluate thirteen models across five agent harnesses to study the effects of model capability, harness choice, and workflow design. The results show that reconstruction quality and costs vary substantially across model-harness configurations, while DrawAI-Flow consistently improves editable structure.

## 내 메모


