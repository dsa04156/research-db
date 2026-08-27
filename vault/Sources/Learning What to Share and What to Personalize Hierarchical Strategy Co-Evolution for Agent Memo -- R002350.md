---
type: research-source
item_id: 2350
title: "Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory"
source: "arxiv"
published: "2026-08-26T03:24:52Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25329"
url: "https://arxiv.org/abs/2608.25329v1"
generated_by: codex-research-db
aliases:
  - "Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory"
topics:
  - "ai-agents"
---

# Learning What to Share and What to Personalize: Hierarchical Strategy Co-Evolution for Agent Memory

[원문 열기](https://arxiv.org/abs/2608.25329v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-26T03:24:52Z
- 저자: Yupeng Han, Shuochen Liu, Kai Zhang, Ze Liu, Zhihong Pan, Xianquan Wang
- 식별자: `arxiv:2608.25329`

## 요약·초록

Memory-augmented agents maintain compact user profiles throughout extended conversations, enabling personalized and consistent responses without the need to process the entire dialogue history. The quality of these user profiles relies on the underlying memory management strategy: at each step, the agent must determine what to retain, compress, or discard. However, existing methods typically employ a static, one-size-fits-all strategy established before training. In practice, the optimal memory decision is inherently user-specific and dynamically evolves alongside policy optimization. To address this, we propose \textbf{HiPS} (\textbf{Hi}erarchical \textbf{P}ersonalized \textbf{S}trategy), a framework that decouples memory management into a globally shared foundation and a user-specific adaptive tier. Specifically, HiPS employs \textbf{Universal Strategy} to extract shared principles from cross-persona trajectories, alongside \textbf{Persona Delta Distillation} to generate tailored rules for users whose behaviors diverge from general patterns. \textbf{Cross-Level Rule Flow} dynamically calibrates their boundary by promoting broadly validated personal rules and demoting contradicted global ones. The architecture establishes a co-evolution loop where a mechanism guarantees that all strategy refinements are anchored to task outcomes. Extensive experiments demonstrate consistent improvements over memory-augmented baselines.

## 내 메모
