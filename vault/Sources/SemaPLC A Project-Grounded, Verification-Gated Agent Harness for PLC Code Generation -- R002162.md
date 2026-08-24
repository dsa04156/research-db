---
type: research-source
item_id: 2162
title: "SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation"
source: "arxiv"
published: "2026-08-19T05:44:29Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.18565"
url: "https://arxiv.org/abs/2608.18565v1"
generated_by: codex-research-db
aliases:
  - "SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation"
topics:
  - "self-evolving-harness"
---

# SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Generation

[원문 열기](https://arxiv.org/abs/2608.18565v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-19T05:44:29Z
- 저자: Yanlun Tu, Huacan Wang, Ziyue Zhou, Jie Zhou, Ningyan Zhu, Ge Chen, Wangyi Chen, Tengfei Zhou, Yifan Zhou, Dasheng Yang, Xiaofeng Mou, Hui Zhang, Yi Xu
- 식별자: `arxiv:2608.18565`

## 요약·초록

Programmable logic controllers (PLCs) run industrial plants, and large language models can already generate independent program organization units (POUs) for them. Whether such logic integrates into an existing PLC project and then runs correctly has been checked only in limited tests. We present \textsc{SemaPLC}, a project-grounded and verification-gated agent harness assembled from conventional tools but governed by a strict completion rule. Rather than stopping when the model judges its own output adequate, \textsc{SemaPLC} declares a task complete only when logged external checks confirm it. Those checks cover the specification, the compilation, and the behavior on a live runtime. On 117 independent-POU tasks matching existing benchmarks, it attains the highest strict verified pass rate on all seven models (72.6\% mean). On a project-context track of 65 tasks whose generated logic must compile and run inside a real project, it attains the highest mean on integrated compilation, static behavior, and dynamic behavior. Of the three layers, dynamic behavior is the most revealing. We measure it by deploying the generated and the reference logic to a live PLC runtime and comparing their executed traces. All methods fall within 10 static points of one another, whereas dynamic scores separate them sharply, from 22.4 to 31.4 for the baselines against 52.2 for \textsc{SemaPLC}. Overall, our verification-gated harness raises the mean at every layer and most sharply at runtime. Execution, not static scoring, is the faithful test of whether generated control logic actually works. \textsc{SemaPLC} is open-sourced at https://github.com/midea-ai/SemaPLC.

## 내 메모


