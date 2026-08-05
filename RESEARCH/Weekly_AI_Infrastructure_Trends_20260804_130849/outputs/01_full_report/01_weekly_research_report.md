# Weekly AI Infrastructure Research Report — 2026-W32

기간: 2026-07-29 ~ 2026-08-04  
범위: self-evolving harness, AI agents, Kubernetes/cloud-native AI infrastructure, cloud/distributed serving, edge AI  
제외: X/Twitter

## 한눈에 보는 변화

이번 주의 중심은 “agent를 더 영리하게 만드는 prompt”보다 “agent가 바꿀 수 있는 범위와 바꾼 결과를 검증하는 운영 계층”으로 옮겨갔다. 연구 쪽에서는 지속 상태와 evaluator-gated update가, 인프라 쪽에서는 resource claim, sandbox, 표준 networking이 같은 방향을 가리킨다.

## Self-evolving harness

<!-- clm_001 --> **검증된 결론:** self-evolving harness의 실질적 개선은 완료 trajectory를 지속 상태로 바꾸고 held-out 평가나 고정 예산 gate로 변경을 선별하는 외부 loop에서 나온다. Living-Harness는 interaction 결과를 episodic memory와 state graph의 procedural repair로 바꾸고, AIDE²는 outer loop가 inner agent 코드를 수정한 뒤 private score와 fixed budget으로 선별한다. Lilian Weng의 시드 글도 context·memory·evaluation·execution control을 model 밖의 harness 문제로 묶는다. [src_001] [src_002] [src_003]

**운영 해석:** 자동 개선 권한과 production 반영 권한을 분리하고, candidate harness는 held-out test와 rollback 가능한 version으로만 승격해야 한다.

## AI agent 평가

<!-- clm_003 --> **검증된 결론:** agent 시스템 검증은 단일 출력 정확도보다 trajectory, 시간에 따른 상태 변화, tool·memory 상호작용, 자원 사용을 함께 보는 lifecycle 평가로 이동해야 한다. 257개 문헌을 검토한 survey는 temporal validity와 runtime evidence가 상대적으로 약하다고 정리하고, Aries와 AgentSLABench는 system telemetry와 resource budget을 평가 표면으로 끌어온다. [src_001] [src_004] [src_005] [src_006]

**실무 체크:** pass/fail만 저장하지 말고 step별 tool call, memory write, retry, latency, sandbox 상태, cost와 정책 위반을 하나의 trace ID로 묶어야 한다.

## Cloud agent serving과 sandbox

<!-- clm_004 --> **검증된 결론:** agent serving infrastructure는 token throughput만이 아니라 sandbox의 burst-idle 패턴, state 복구 비용, 격리와 attack surface를 별도 운영 지표와 control boundary로 다뤄야 한다. Aries는 비추론 병목과 snapshot 복구 비용을 지적하고, Kubernetes Agent Sandbox는 stateful singleton workload를 격리하는 공식 구현 경로를 제공한다. [src_005] [src_006] [src_010] [src_011]

**실무 체크:** model server autoscaling과 sandbox autoscaling을 같은 지표로 묶지 않는다. Sandbox에는 idle suspension, state restore time, filesystem/network 권한, egress policy와 kill boundary를 별도 SLO로 둔다.

## Kubernetes·GPU·networking

<!-- clm_005 --> **검증된 결론:** Kubernetes GPU multitenancy의 현재 실무 패턴은 scheduler가 device topology와 claim을 보게 하고 hardware partition과 tenant boundary를 함께 적용하는 방향이다. Red Hat은 DRA와 MIG로 한 H100에 격리된 두 inference service를 구성했고, NVIDIA는 공유 GPU 위 tenant별 cluster 격리를 설명한다. 이는 재현 가능한 reference architecture의 증거이며, 모든 환경의 비용 절감 폭을 보장하는 결과는 아니다. [src_007] [src_009]

<!-- clm_006 --> **검증된 결론:** 지난 7일의 cloud-native AI 운영 변화는 새로운 단일 AI abstraction보다 표준 networking, resource claims, sandbox, 통합 SDK 같은 외부 control-plane primitive를 강화하는 흐름으로 모인다. Gateway API v1.6은 TCPRoute·UDPRoute를 Standard v1으로 승격하고 experimental API를 별도 그룹으로 분리했다. Kubeflow SDK는 통합 인터페이스의 사용 확대를 알렸다. Agent workload도 결국 network, device, sandbox, pipeline 경계마다 명시적 정책이 필요하다. [src_005] [src_007] [src_008] [src_009] [src_010] [src_011] [src_012]

**실무 체크:** GPU Operator만 설치했다고 multitenancy가 완성되는 것은 아니다. DRA driver와 ResourceClaim, MIG profile, Gateway conformance, tenant namespace·network policy를 함께 검증한다.

## Edge AI

<!-- clm_007 --> **검증된 결론:** edge AI는 cloud를 없애는 구조가 아니라 latency, privacy, connectivity, device capacity에 맞춰 inference와 orchestration을 나누는 workload-placement 문제다. Microsoft의 학습 저장소는 hardware-aware optimization과 local agent 기능을 함께 다루고, GSMA 분석은 연결성과 비용 조건에 따른 선택을 강조한다. Workerd 릴리스는 edge runtime이 지속적으로 갱신되는 software surface임을 보여준다. [src_013] [src_014] [src_015]

**이번 주 판단:** 최근 7일 안에 이 원칙을 뒤집을 만큼 검증된 edge architecture 변화는 없었다.

## SNS·약한 신호

Instagram에서는 Microsoft edge 학습 저장소가, TikTok에서는 소형 device detection과 cloud messaging 데모가, LinkedIn에서는 embedded 프로젝트에 coding agent를 붙이는 논의가 포착됐다. 모두 발견 경로로만 썼으며 보급 규모나 성능 근거로 사용하지 않았다. [src_016] [src_017] [src_018]

## 반증·한계

- Living-Harness와 AIDE²의 benchmark 수치는 저자 보고다. 독립 재현과 동일 비용 조건 검증이 없다.
- Weco는 개선된 outer-loop 효율이 통계적으로 유의하지 않다고 명시했고, 진화한 code의 복잡성과 유지보수 어려움도 밝혔다.
- DRA/MIG와 Agent Sandbox는 공식 구현·가이드는 확인됐지만 독립 조직의 장기 장애율, 운영비, 대규모 tenancy 수치는 부족하다.
- Edge-only 주장은 반증됐다. 근거는 local과 cloud의 역할 분리를 전제로 한다.

## 다음 7일 자동 조사 질문

1. Living-Harness 또는 AIDE² 결과를 독립 팀이 같은 비용 gate로 재현했는가?
2. Agent Sandbox가 release 이후 공개 production incident나 latency·restore SLO를 보고했는가?
3. DRA partitionable devices가 OpenShift 외 upstream Kubernetes 운영 사례로 확장됐는가?
4. Gateway API v1.6의 XBackend와 egress 논의가 agent outbound policy로 구체화됐는가?
5. Edge agent 사례가 교육용 데모를 넘어 fleet update·rollback·observability 자료를 공개했는가?

## Confidence

- Harness 개선 구조: Medium
- Agent lifecycle 평가 방향: Medium-High
- Kubernetes networking·DRA 운영 변화: High
- Cloud agent-serving 세부 수치: Medium
- Edge-cloud placement 원칙: Medium-High

## Refuted

- Edge-only 배치 서사는 반증 검색을 통과하지 못했다.

## Unresolved

- 최신 preprint와 vendor 연구의 성능 크기 및 production 일반화
- DRA/MIG·Agent Sandbox의 폭넓은 production 정착
- SNS에서 보이는 학습·데모 관심이 실제 도입으로 이어지는지
