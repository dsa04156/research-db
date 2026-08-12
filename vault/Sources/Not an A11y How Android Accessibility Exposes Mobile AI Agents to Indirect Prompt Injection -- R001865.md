---
type: research-source
item_id: 1865
title: "Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection"
source: "arxiv"
published: "2026-08-09T22:13:55Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.08939"
url: "https://arxiv.org/abs/2608.08939v1"
generated_by: codex-research-db
aliases:
  - "Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection"
topics:
  - "ai-agents"
---

# Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection

[원문 열기](https://arxiv.org/abs/2608.08939v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6SG58VTW`)
- 발행일: 2026-08-09T22:13:55Z
- 저자: Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea, Kaushal Punjabi, Stjepan Picek
- 식별자: `arxiv:2608.08939`

## 요약·초록

The rise of autonomous AI agents represents a major paradigm shift in how users interact with mobile devices. Frameworks such as MobileRun and Mobile-Use can autonomously navigate Android applications and execute complex multi-step tasks. To interpret user interfaces, these frameworks rely primarily on Android accessibility (A11y) trees and secondarily on visual screenshots. In this paper, we demonstrate that this architectural dependence on unsanitized accessibility metadata, together with visual input, introduces a systemic vulnerability to indirect prompt injection. We show that adversarial prompts can cause autonomous agents to abandon their original objectives, violate context boundaries, and perform unauthorized device actions. Our empirical evaluation demonstrates goal hijacking, context drift, and unauthorized actions across visually hidden and fully exposed attack scenarios. In aggregate, MobileRun reaches an attack success rate of 0.822 with Gemma4:31B, while Mobile-Use with Qwen3.6:35B reduces this to 0.150 but does not eliminate context drift or unauthorized actions. These findings reveal that current mobile agent frameworks fail to enforce semantic context boundaries, treating passive environmental text as trusted instructions. Finally, we present a taxonomy of these attacks and discuss the need for zero-trust input validation, dedicated security agents, and strict context isolation within mobile agent architectures.

## 내 메모


