---
type: research-source
item_id: 7
title: "Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation"
source: "arxiv"
published: "2026-07-28T18:00:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26148"
url: "https://arxiv.org/abs/2607.26148v1"
generated_by: codex-research-db
aliases:
  - "Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation"
topics:
  - "self-evolving-harness"
---

# Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation

[원문 열기](https://arxiv.org/abs/2607.26148v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VBUIMTWE`)
- 발행일: 2026-07-28T18:00:34Z
- 저자: Jian Zhou, Xunyi Zhao, Gengze Zhou, Zerui Li, Sihao Lin, Jiajun Liu, Qi Wu
- 식별자: `arxiv:2607.26148`

## 요약·초록

Autonomous embodied agents must sustain a long decision-making loop that involves perceiving, acting, verifying, and self-correcting over many steps. Current systems sustain this loop through task-specific workflows or embodied policies. We study a third form, agentic embodied control, in which a general-purpose agent holds the loop itself. Using zero-shot navigation as a controlled testbed, we evaluate three software-engineering agent harnesses given only a monocular RGB camera and discrete actions. Under this strictly minimal condition, replicated default-effort configurations reach 70.7$\pm$3.5% success (opus-5, mean over three runs), and fable-5 reaches 78% at maximum effort. When a trained waypoint tool is exposed alongside primitives as an optional capability, the hybrid fable-5 agent reaches 76.7$\pm$0.6% at default effort, using half the environment steps and less than one quarter of the wall time of the maximum-effort primitive run. Controlled interventions show that capability is primarily model-centered: model choice strongly changes success, harness effects are descriptive, and a forced waypoint interface helps weaker models but can hinder stronger ones. Performance nevertheless falls sharply on longer-horizon tasks, while latency and context growth limit sustained operation. These results show that agentic control is already competitive in zero-shot navigation and that models, harnesses, and interfaces offer complementary paths toward autonomous embodied agents.

## 내 메모


