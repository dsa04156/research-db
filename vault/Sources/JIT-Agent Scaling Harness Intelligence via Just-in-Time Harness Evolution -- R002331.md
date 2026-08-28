---
type: research-source
item_id: 2331
title: "JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution"
source: "arxiv"
published: "2026-08-26T10:05:33Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25593"
url: "https://arxiv.org/abs/2608.25593v1"
generated_by: codex-research-db
aliases:
  - "JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution"
topics:
  - "self-evolving-harness"
---

# JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution

[원문 열기](https://arxiv.org/abs/2608.25593v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KTQMF2IV`)
- 발행일: 2026-08-26T10:05:33Z
- 저자: Guibin Zhang, Leo Lu, Fangzhou Xie, Kang Zhu, Junhao Wang, Zhifei Xie, Zhaochen Yu, Zihang Liu, Zhongxiang Sun, Qiankun Li, Yue Liao, Heng Chang, Xiaobin Hu, Qibing Ren, Wangchunshu Zhou, Shuicheng Yan
- 식별자: `arxiv:2608.25593`

## 요약·초록

Agent capability is not determined by the model alone. The agent harness, encompassing memory management, planning strategy, action protocol, and tool/skill orchestration, can dominate the contribution of the underlying foundation model. Yet harness design remains manual, task-specific, and fundamentally unscalable. We present JIT-Agent, a harness intelligence model trained to synthesize task-adaptive agent harnesses on the fly for arbitrary off-the-shelf agentic LLMs. We formalize the agent harness as a composable, machine-generatable artifact governed by a fixed four-module protocol, and train JIT-Agent to customize harnesses for a given task at hand, repair harnesses for stable and reliable execution, and self-evolve by distilling performance signals from an expanding archive of prior harness configurations. Equipped with JIT-Agent as a harness helper, DeepSeek-V4-Flash surpasses GPT-5.6 on DeepSearchQA (+9.1) and OdysseyBench (+4.3), while the already strong GLM-5.2 gains up to +20.2 points. Across controlled evaluations, JIT-Agent-generated harnesses are performance-competitive with mature agent runtimes such as OpenCode and Claude Code and consistently improve multi-scale model families of DeepSeek V4, Mimo-V2.5, and Qwen3.6. To our knowledge, JIT-Agent is the first model purpose-built for just-in-time harness generation, establishing harness intelligence as a trainable, transferable, and compounding dimension of agent capability orthogonal to model scaling.

## 내 메모


