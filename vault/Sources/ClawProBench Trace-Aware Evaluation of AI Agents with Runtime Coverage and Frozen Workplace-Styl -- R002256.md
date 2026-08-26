---
type: research-source
item_id: 2256
title: "ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts"
source: "arxiv"
published: "2026-08-23T17:09:02Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.22510"
url: "https://arxiv.org/abs/2608.22510v1"
generated_by: codex-research-db
aliases:
  - "ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts"
topics:
  - "ai-agents"
---

# ClawProBench: Trace-Aware Evaluation of AI Agents with Runtime Coverage and Frozen Workplace-Style Holdouts

[원문 열기](https://arxiv.org/abs/2608.22510v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4AN3KGW5`)
- 발행일: 2026-08-23T17:09:02Z
- 저자: YuanHang Xiao
- 식별자: `arxiv:2608.22510`

## 요약·초록

Agent benchmarks often evaluate only final answers even when agents run on stateful runtimes. We argue this under-specifies what is being evaluated: the proper unit is a declared model-plus-runtime configuration whose failures can occur in evidence acquisition, runtime routing, safety boundaries, or repeated execution. We present ClawProBench, a trace-aware benchmark for runtime-native agent evaluation instantiated on OpenClaw, a live agent runtime with workspace tools and native surfaces for browsing, memory, messaging, scheduling, skills, and subagents. ClawProBench defines two tracks: a 102-scenario full profile with live workspace and native-runtime routing tasks, and a frozen 68-scenario holdout with closed-world JSON output contracts for robust ranking. Trials are scored from execution traces via a safety-gated formula combining correctness, process quality, and efficiency, preserving failure evidence for audit. Our anonymous artifact includes benchmark definitions, scoring code, manifests and sanitized traces. We evaluate 68 configurations on the full profile and 37 on holdout. The top safety-gated average trace score is 0.7671. Native-runtime tasks underperform workspace-live tasks (0.5238 vs. 0.6415). On holdout, pass@k-any outperforms strict three-trial pass (0.6638 vs. 0.2890), while full-profile and holdout rankings show weak alignment (Spearman 0.1300). Rankings based purely on correctness differ substantially from process-aware, safety-gated and strict-pass views. Final-answer leaderboards may hide native-surface weaknesses, one-off successes and trace-local agent failure modes.

## 내 메모
