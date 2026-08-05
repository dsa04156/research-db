---
type: research-source
item_id: 1663
title: "Extended KAFR: A kinematic-adaptive paradigm for the efficient analysis of surgical video"
source: "arxiv"
published: "2026-08-02T07:48:48Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.01058"
url: "https://arxiv.org/abs/2608.01058v1"
generated_by: codex-research-db
aliases:
  - "Extended KAFR: A kinematic-adaptive paradigm for the efficient analysis of surgical video"
topics:
  - "self-evolving-harness"
---

# Extended KAFR: A kinematic-adaptive paradigm for the efficient analysis of surgical video

[원문 열기](https://arxiv.org/abs/2608.01058v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7AB7B9AE`)
- 발행일: 2026-08-02T07:48:48Z
- 저자: Huu Phong Nguyen, Shekhar Madhav Khairnar, Ganesh Sankaranarayanan
- 식별자: `arxiv:2608.01058`

## 요약·초록

Artificial Intelligence is increasingly applied to surgical video analysis for phase segmentation, skill assessment, and workflow optimization. A key challenge is the length of surgical recordings, often one to several hours, creating substantial computational burden. We previously developed Kinematics-Adaptive Frame Recognition (KAFR) for robotic surgery, showing that tracking tool motion effectively identifies informative frames while filtering redundant content. However, laparoscopic surgery introduces additional challenges: manual camera control causes frequent motion artifacts, and image quality is generally lower than robotic systems. This study evaluates whether KAFR generalizes to laparoscopic surgery using the Cholec80 benchmark, comprising 80 laparoscopic cholecystectomy procedures annotated for seven surgical phases. KAFR operates in three stages: a fine-tuned YOLO model detects and segments surgical tools; frames are adaptively selected based on tool displacement or velocity variation; and an X3D model classifies selected frames into surgical phases. KAFR achieved a 91.0\% F1 score using only 0.58\% of frames for phase classification, representing an approximately seven-fold reduction compared to typical 4\% frame sampling, while maintaining performance comparable to LoViT (90.2\%) and Trans-SVNet (89.7\%). These results demonstrate that kinematics-based frame selection transfers effectively to the challenging laparoscopic environment.

## 내 메모


