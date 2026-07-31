---
type: research-source
item_id: 552
title: "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents"
source: "arxiv"
published: "2025-05-29T00:26:15Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.22954"
url: "https://arxiv.org/abs/2505.22954v3"
generated_by: codex-research-db
aliases:
  - "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents"
topics:
  - "self-evolving-harness"
---

# Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents

[원문 열기](https://arxiv.org/abs/2505.22954v3)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`AP53RCQP`)
- 발행일: 2025-05-29T00:26:15Z
- 저자: Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, Jeff Clune
- 식별자: `arxiv:2505.22954`

## 요약·초록

Today's AI systems have human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The advance of AI could itself be automated. If done safely, that would accelerate AI development and allow us to reap its benefits much sooner. Meta-learning can automate the discovery of novel algorithms, but is limited by first-order improvements and the human design of a suitable search space. The Gödel machine proposed a theoretical alternative: a self-improving AI that repeatedly modifies itself in a provably beneficial manner. Unfortunately, proving that most changes are net beneficial is impossible in practice. We introduce the Darwin Gödel Machine (DGM), a self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. Inspired by Darwinian evolution and open-endedness research, the DGM maintains an archive of generated coding agents. It grows the archive by sampling an agent from it and using a foundation model to create a new, interesting, version of the sampled agent. This open-ended exploration forms a growing tree of diverse, high-quality agents and allows the parallel exploration of many different paths through the search space. Empirically, the DGM automatically improves its coding capabilities (e.g., better code editing tools, long-context window management, peer-review mechanisms), increasing performance on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%. Furthermore, the DGM significantly outperforms baselines without self-improvement or open-ended exploration. All experiments were done with safety precautions (e.g., sandboxing, human oversight). The DGM is a significant step toward self-improving AI, capable of gathering its own stepping stones along paths that unfold into endless innovation.

## 내 메모


