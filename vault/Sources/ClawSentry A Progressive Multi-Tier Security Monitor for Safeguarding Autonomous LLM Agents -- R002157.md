---
type: research-source
item_id: 2157
title: "ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents"
source: "arxiv"
published: "2026-08-21T13:47:51Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.21101"
url: "https://arxiv.org/abs/2608.21101v1"
generated_by: codex-research-db
aliases:
  - "ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents"
topics:
  - "self-evolving-harness"
---

# ClawSentry: A Progressive Multi-Tier Security Monitor for Safeguarding Autonomous LLM Agents

[원문 열기](https://arxiv.org/abs/2608.21101v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3X6NWIXF`)
- 발행일: 2026-08-21T13:47:51Z
- 저자: Kai Wang, Zeming Wei, BiaoJie Zeng, Chang Jin, An Wang, Xiaokun Luan, Zhixiao Lin, Jingjing Qu, Xia Hu, Xingcheng Xu
- 식별자: `arxiv:2608.21101`

## 요약·초록

As large language model (LLM) agents move from conversation to executing code, reading local files, and orchestrating external tools, a single agent hijacked by a malicious third-party skill can cause data exfiltration, privilege escalation, or cascading compromise. We argue that agentic risk is progressive: it can enter at four loci of the agent control loop--skill admission, invocation-time intent, execution-time effect, and post-action consequence--while a denied dangerous objective can reappear across surface forms, tools, or turns; existing safeguards are typically local to one lifecycle boundary or one call. Guided by this threat model, we present ClawSentry, an open-source, framework-agnostic security supervision gateway for agent runtimes. Before a skill package is ever executed, First-use Skill Package Review (FSPR) audits it under a deterministic evidence floor, escalating unresolved cases to bounded read-only agentic review (locus A). At runtime, a three-tier progressive decision engine--a deterministic L1 layer, a rule-anchored L2 semantic reviewer, and a read-only L3 evidence-seeking agent--spends contextual review only on the residual ambiguity, while a session-level anti-bypass mechanism recognizes tool-switching and rephrased retries (loci B--C); a post-action path feeds high-severity evidence non-retroactively into later review (locus D). An Agent Harness Protocol (AHP) abstraction applies one policy across Codex, Claude Code, Kimi CLI, and Gemini CLI without modifying agent internals. On SkillInject with Codex/GPT-5.4, contextual ASR falls from 39.55% to 2.61% while contextual TSR moves only from 83.78% to 83.05%. Across five Work Agents on the full SkillsSafety benchmark, ClawSentry confines ASR to 9.09--15.03% from 33.5--49.7% unprotected, and aggregate TSR on clean skills remains 98.7%.

## 내 메모


