---
type: research-source
item_id: 983
title: "Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents"
source: "arxiv"
published: "2026-07-16T15:47:19Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.15143"
url: "https://arxiv.org/abs/2607.15143v1"
generated_by: codex-research-db
aliases:
  - "Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents"
topics:
  - "self-evolving-harness"
---

# Setup Complete, Now You Are Compromised: Weaponizing Setup Instructions Against AI Coding Agents

[원문 열기](https://arxiv.org/abs/2607.15143v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IUAE9IBX`)
- 발행일: 2026-07-16T15:47:19Z
- 저자: Aadesh Bagmar, Pushkar Saraf
- 식별자: `arxiv:2607.15143`

## 요약·초록

AI coding agents set up projects by reading documentation and installing the dependencies it lists, without verifying their names, sources, or known vulnerabilities. By editing only a README, requirements file, or Makefile, an attacker can redirect the agent to an untrusted registry, a known-vulnerable version, or a wrong-but-plausible name: documentation becomes a vector for code execution. We present the first systematic evaluation of package-install-time supply-chain attacks delivered through ordinary project-setup documentation across production coding-agent harnesses, probing frontier models on twelve scenarios in five attack classes, grounded in documented incidents. The same model catches an attack through one harness and installs it through another: install-time security rests on the harness-model combination, not the model alone. Agents catch blatant typosquats reliably, but plausible separator-confusion names (azurecore for azure-core) slip through, and how often depends on the harness-model pairing. Source-based attacks like registry redirection are missed almost everywhere. The source blind spot recurs on npm and Cargo, where nearly every model installs the untrusted dependency; name detection carries over less consistently across ecosystems. Security-oriented prompts recover part of the gap but only for the dimension they name; a deterministic pre-install check that verifies names, sources, and versions before any code runs closes most of it.

## 내 메모


