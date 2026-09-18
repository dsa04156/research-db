---
type: research-source
item_id: 2808
title: "HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness"
source: "arxiv"
published: "2026-09-14T08:15:56Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.15195"
url: "https://arxiv.org/abs/2609.15195v2"
generated_by: codex-research-db
aliases:
  - "HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness"
topics:
  - "self-evolving-harness"
---

# HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness

[원문 열기](https://arxiv.org/abs/2609.15195v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SHX7ZGXW`)
- 발행일: 2026-09-14T08:15:56Z
- 저자: Yang Chen, Lirong Che, Zhenyu Huang, Wenbo Fu, Chuang Wang, Xu Cao, Daqi Liu, Yuzhe Yang, Jian Su, Lan-Zhe Guo
- 식별자: `arxiv:2609.15195`

## 요약·초록

Embodied navigation requires agents to interpret visual observations, accumulate spatial knowledge, and execute actions to follow instructions or locate objects. Training-based methods face generalization challenges, while training-free methods exploit multimodal large language models (MLLMs) but often lack mechanisms to reconcile proposed actions with spatial evidence, task progress, and execution failures. We present HarnessVLN, a zero-shot, training-free framework whose Agent Harness coordinates perception, retrieval, grounding, navigation, recovery, and termination through a unified tool interface. The Harness validates planner proposals against spatial evidence, geometric feasibility, and subgoal consistency, incorporating structured tool feedback into subsequent decisions. Hierarchical event memory tracks task progress and execution history, while a persistent Spatiotemporal Graph maintains reusable spatial evidence and failure annotations for verification and recovery. A replaceable Navigation Executor converts validated targets into executable motions, allowing the same Harness protocol to support instruction-following and object-goal navigation. HarnessVLN achieves success rates of 60.8%, 53.9%, 76.0%, and 59.3% on R2R, RxR, HM3D-v2, and HM3D-OVON, respectively, surpassing prior training-free SOTA results. Humanoid deployment further demonstrates its applicability to both tasks in real-world environments. The project page is: https://harnessvln.netlify.app/.

## 내 메모
