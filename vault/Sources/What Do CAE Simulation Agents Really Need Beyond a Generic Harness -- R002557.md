---
type: research-source
item_id: 2557
title: "What Do CAE Simulation Agents Really Need Beyond a Generic Harness?"
source: "arxiv"
published: "2026-09-03T11:53:17Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03718"
url: "https://arxiv.org/abs/2609.03718v1"
generated_by: codex-research-db
aliases:
  - "What Do CAE Simulation Agents Really Need Beyond a Generic Harness?"
topics:
  - "self-evolving-harness"
---

# What Do CAE Simulation Agents Really Need Beyond a Generic Harness?

[원문 열기](https://arxiv.org/abs/2609.03718v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T11:53:17Z
- 저자: Jiasheng Shi, Tianhan Zhang
- 식별자: `arxiv:2609.03718`

## 요약·초록

Computer-aided engineering (CAE) simulation is among the largest and most demanding areas of engineering, where setting up a solver such as OpenFOAM, FEniCS, or COMSOL takes real expertise. Large language model (LLM) agents promise to turn a natural-language request into a working simulation, and recent CAE agents add simulation-specific machinery: multi-agent decomposition, domain retrieval, and scripted reflection. That machinery suited weak base models; modern harnesses already supply multi-turn reasoning, tool use, and execution feedback. We ask what a CAE simulation agent still needs beyond a generic harness. With information access and repair budget held fixed, a single-agent harness matches or beats multi-agent specialized systems (FoamBench 96.4\% vs.\ 88.2\%). Ablations trace this to capabilities the harness already provides: execution-feedback repair lifts FoamBench from 71.8\% with no repair round to 96.4\%, while scripted reflection adds nothing. The one input that still helps is domain knowledge supplied as solver tutorials, our largest measured gain (80.9\% to 96.4\%).

## 내 메모


