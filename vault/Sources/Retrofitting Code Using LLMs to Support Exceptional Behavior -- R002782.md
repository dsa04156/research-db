---
type: research-source
item_id: 2782
title: "Retrofitting Code Using LLMs to Support Exceptional Behavior"
source: "arxiv"
published: "2026-09-09T16:18:47Z"
first_seen: "2026-09-11"
review_status: "pending"
canonical_key: "arxiv:2609.10397"
url: "https://arxiv.org/abs/2609.10397v1"
generated_by: codex-research-db
aliases:
  - "Retrofitting Code Using LLMs to Support Exceptional Behavior"
topics:
  - "self-evolving-harness"
---

# Retrofitting Code Using LLMs to Support Exceptional Behavior

[원문 열기](https://arxiv.org/abs/2609.10397v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-11|2026-09-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-09T16:18:47Z
- 저자: Linghan Zhong, Jiyang Zhang, Jayanth Srinivasa, Junyi Jessy Li, Milos Gligoric
- 식별자: `arxiv:2609.10397`

## 요약·초록

Exception Related Code (ERC), which includes throw statements, conditions (if statements) that guard those throw statements, and try/catch blocks, is an essential component of software systems, allowing developers to detect and handle exceptional states that deviate from the expected program behavior. However, manually writing ERC across large codebases is tedious. We propose a novel task: retrofitting existing code with ERC. Namely, given code (without ERC) and Exceptional Behavior Tests (EBTs) (e.g., check if method throws InvalidArgumentException if null is given as the value to the argument) we aim to automatically generate missing ERC, such that the given tests pass. We design and implement Exception Coder (EXCODER) that performs context engineering to help Large Language Models (LLMs) tackle this task. EXCODER integrates static and dynamic program analysis with LLMs by providing the extracted contextual information to the LLMs. To evaluate EXCODER, we build a benchmark constructed from GitHub Java repositories, where we systematically remove ERC in 304 methods from 75 projects. Our results demonstrate that EXCODER provides an effective, though imperfect, solution to this problem in automated code generation, offering developers the first way to implement ERC following test-driven development. When combined with Qwen 2.5 Coder 32b, EXCODER achieves pass@1, 5, and 10 rates of 85.92% (12.56 percentage points over baseline), 86.18% (12.82 p.p. over baseline), and 86.51% (13.15 p.p. over baseline), respectively, on developer-written test suites. Our manual inspection of the generated code further reveals limitations of EXCODER, pointing to directions for future work.

## 내 메모


