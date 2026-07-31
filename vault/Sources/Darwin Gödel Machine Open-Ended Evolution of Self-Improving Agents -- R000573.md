---
type: research-source
item_id: 573
title: "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
source: "openalex"
published: "2025-07-20"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.70777/si.v2i3.15063"
url: "https://doi.org/10.70777/si.v2i3.15063"
generated_by: codex-research-db
aliases:
  - "Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents"
topics:
  - "self-evolving-harness"
---

# Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents

[원문 열기](https://doi.org/10.70777/si.v2i3.15063)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`ZGZ5ZFX7`)
- 발행일: 2025-07-20
- 저자: Jenny Zhang, Shengran Hu, Cong Lu, R. D. Lange, Jeff Clune
- 식별자: `doi:10.70777/si.v2i3.15063`

## 요약·초록

Most of today’s AI systems are constrained by human-designed, fixed architectures and cannot autonomously and continuously improve themselves. The scientific method, on the other hand, provides a cumulative and open-ended system, where each innovation builds upon previous artifacts, enabling future discoveries. There is growing hope that the current manual process of advancing AI could itself be automated. If done safely, such automation would accelerate AI development and allow us to reap its benefits much sooner. This prospect raises the question of how AI systems can endlessly improve themselves while getting better at solving relevant problems. Previous approaches, such as meta-learning, provide a toolset for automating the discovery of novel algorithms but are limited by the human design of a suitable search space and first-order improvements. The Godel machine [116], on the other hand, introduced a theoretical approach to a self-improving AI, capable of modifying itself in a provably beneficial manner. Unfortunately, this original formulation is in practice impossible to create due to the inability to prove the impact of most self-modifications. To address this limitation, we propose the Darwin Godel Machine (DGM), a novel self-improving system that iteratively modifies its own code (thereby also improving its ability to modify its own codebase) and empirically validates each change using coding benchmarks. In this paper, the DGM aims to optimize the design of coding agents, powered by frozen foundation models, which enable the ability to read, write, and execute code via tool use. Inspired by biological evolution and open-endedness research, the DGM maintains an archive of generated coding agents. It then samples from this archive and tries to create a new, interesting, improved version of the sampled agent. This open-ended exploration forms a growing tree of diverse, high-quality agents and allows the parallel exploration of many different paths through the search space. Empirically, the DGM automatically improves its coding capabilities (e.g., better code editing tools, long-context window management, peer-review mechanisms), producing performance increases on SWE-bench from 20.0% to 50.0%, and on Polyglot from 14.2% to 30.7%. Furthermore, the DGM significantly outperforms baselines without self-improvement or open-ended exploration. All experiments were done with safety precautions (e.g., sandboxing, human oversight). Overall, the DGM represents a significant step toward self-improving AI, capable of gathering its own stepping stones along a path that unfolds into endless innovation. All code is open-sourced at https://github.com/jennyzzt/dgm.

## 내 메모


