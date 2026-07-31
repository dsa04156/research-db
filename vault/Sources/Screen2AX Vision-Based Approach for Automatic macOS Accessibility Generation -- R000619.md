---
type: research-source
item_id: 619
title: "Screen2AX: Vision-Based Approach for Automatic macOS Accessibility Generation"
source: "arxiv"
published: "2025-07-22T15:38:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.16704"
url: "https://arxiv.org/abs/2507.16704v1"
generated_by: codex-research-db
aliases:
  - "Screen2AX: Vision-Based Approach for Automatic macOS Accessibility Generation"
topics:
  - "ai-agents"
---

# Screen2AX: Vision-Based Approach for Automatic macOS Accessibility Generation

[원문 열기](https://arxiv.org/abs/2507.16704v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VBJJ9NCH`)
- 발행일: 2025-07-22T15:38:12Z
- 저자: Viktor Muryn, Marta Sumyk, Mariya Hirna, Sofiya Garkot, Maksym Shamrai
- 식별자: `arxiv:2507.16704`

## 요약·초록

Desktop accessibility metadata enables AI agents to interpret screens and supports users who depend on tools like screen readers. Yet, many applications remain largely inaccessible due to incomplete or missing metadata provided by developers - our investigation shows that only 33% of applications on macOS offer full accessibility support. While recent work on structured screen representation has primarily addressed specific challenges, such as UI element detection or captioning, none has attempted to capture the full complexity of desktop interfaces by replicating their entire hierarchical structure. To bridge this gap, we introduce Screen2AX, the first framework to automatically create real-time, tree-structured accessibility metadata from a single screenshot. Our method uses vision-language and object detection models to detect, describe, and organize UI elements hierarchically, mirroring macOS's system-level accessibility structure. To tackle the limited availability of data for macOS desktop applications, we compiled and publicly released three datasets encompassing 112 macOS applications, each annotated for UI element detection, grouping, and hierarchical accessibility metadata alongside corresponding screenshots. Screen2AX accurately infers hierarchy trees, achieving a 77% F1 score in reconstructing a complete accessibility tree. Crucially, these hierarchy trees improve the ability of autonomous agents to interpret and interact with complex desktop interfaces. We introduce Screen2AX-Task, a benchmark specifically designed for evaluating autonomous agent task execution in macOS desktop environments. Using this benchmark, we demonstrate that Screen2AX delivers a 2.2x performance improvement over native accessibility representations and surpasses the state-of-the-art OmniParser V2 system on the ScreenSpot benchmark.

## 내 메모


