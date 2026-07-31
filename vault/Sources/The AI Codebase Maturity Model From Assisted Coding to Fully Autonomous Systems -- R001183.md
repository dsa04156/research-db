---
type: research-source
item_id: 1183
title: "The AI Codebase Maturity Model: From Assisted Coding to Fully Autonomous Systems"
source: "arxiv"
published: "2026-04-10T15:00:59Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.09388"
url: "https://arxiv.org/abs/2604.09388v2"
generated_by: codex-research-db
aliases:
  - "The AI Codebase Maturity Model: From Assisted Coding to Fully Autonomous Systems"
topics:
  - "ai-agents"
  - "kubernetes"
---

# The AI Codebase Maturity Model: From Assisted Coding to Fully Autonomous Systems

[원문 열기](https://arxiv.org/abs/2604.09388v2)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UZEBHGQM`)
- 발행일: 2026-04-10T15:00:59Z
- 저자: Andy Anderson
- 식별자: `arxiv:2604.09388`

## 요약·초록

AI coding tools are widely adopted, but most teams plateau at prompt-and-review without a framework for systematic progression. This paper presents the AI Codebase Maturity Model (ACMM), a 6-level framework describing how codebases evolve from basic AI-assisted coding to fully autonomous systems. Inspired by CMMI, each level is defined by its feedback loop topology - the specific mechanisms that must exist before the next level becomes possible. I validate the model through a 100-day experience report maintaining KubeStellar Console, a CNCF Kubernetes dashboard built from scratch with Claude Code (Opus) and GitHub Copilot, and through the initial production deployment of Hive - an open-source multi-agent orchestration system that realizes Level 6: full autonomy. The system currently operates with 74 CI/CD workflows, 32 nightly test suites, 91% code coverage, and achieves bug-to-fix times under 30 minutes - 24 hours a day. The central finding: the intelligence of an AI-driven development system resides not in the AI model itself, but in the infrastructure of instructions, tests, metrics, and feedback loops that surround it. You cannot skip levels, and at each level, the thing that unlocks the next one is another feedback mechanism. Testing - the volume of test cases, the coverage thresholds, and the reliability of test execution - proved to be the single most important investment in the entire journey. v2 extends the model from 5 to 6 levels, adding Level 6 (Fully Autonomous) with Hive as reference implementation and Beads for cross-agent memory continuity, plus throughput acceleration data showing 5x PR throughput and 37x issue throughput from Level 2 to Level 6.

## 내 메모


