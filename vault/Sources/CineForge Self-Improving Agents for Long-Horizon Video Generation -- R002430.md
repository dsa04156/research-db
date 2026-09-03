---
type: research-source
item_id: 2430
title: "CineForge: Self-Improving Agents for Long-Horizon Video Generation"
source: "arxiv"
published: "2026-08-30T07:29:46Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.29621"
url: "https://arxiv.org/abs/2608.29621v1"
generated_by: codex-research-db
aliases:
  - "CineForge: Self-Improving Agents for Long-Horizon Video Generation"
topics:
  - "self-evolving-harness"
---

# CineForge: Self-Improving Agents for Long-Horizon Video Generation

[원문 열기](https://arxiv.org/abs/2608.29621v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`B84QFSIB`)
- 발행일: 2026-08-30T07:29:46Z
- 저자: Junxiang Liu, Lin Wang, Haiyu Shi, Hongxu Ma, Xiaoyu Yang, Chunjie Chen, Xiaoxiao Xu, Kaiqiao Zhan, Boao Wang, Shuizhou Shi, Tianyun Zhu, Jie Li, Jiangtong Li
- 식별자: `arxiv:2608.29621`

## 요약·초록

Long-horizon story-driven video generation requires a production agent to coordinate narrative decomposition, state tracking, shot design, prompt construction, rendering, and revision across interdependent scenes. Existing adaptive video systems primarily refine requests or reusable skills, leaving recurring production failures disconnected from persistent, stage-targeted improvements across stories. We introduce CineForge, a self-evolving video-production agent framework that couples CineForge-Produce for video generation with CineForge-Evolve for cross-story policy evolution. CineForge-Produce organizes each source story into typed narrative, character, spatial, and cinematic states, uses them to coordinate asset and clip generation, and records the process as a canonical production trajectory. CineForge-Evolve applies Case-to-Pattern-to-Policy Evolution (CPPE) to review trajectory evidence, consolidate recurrent findings into bounded stage-local patches, and deploy validated updates through structural replay and confidence-controlled paired evaluation. To measure complete story realization, we introduce CineScope, which combines a 100-script CineScope-Data suite with a human-aligned, multiscale CineScope-Metric spanning causal state, directorial orchestration, pacing and resource allocation, and character arc. Across CineScope-Data and two public benchmarks, the evolved CineForge policy improves CineScope-Metric from 4.024 to 4.380, outperforms three long-video baselines with consistent gains under ScriptAgent, and reduces review LLM calls by 37.0% on new stories. These results establish production trajectories as actionable experience for video agents that improve cumulatively across long-form storytelling tasks.

## 내 메모


