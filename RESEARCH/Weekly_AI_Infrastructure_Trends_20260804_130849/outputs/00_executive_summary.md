# 2026-08-04 주간 AI 인프라 심층 조사

## 결론

1. <!-- clm_001 --> Self-evolving harness의 핵심은 더 긴 prompt가 아니라 실행 기록을 지속 상태로 만들고, 별도의 평가 gate가 다음 변경을 선택하게 하는 외부 개선 loop다. [src_001] [src_002] [src_003]
2. <!-- clm_003 --> Agent 검증 단위는 한 번의 정답률에서 장기 trajectory, tool·memory 상호작용, 시간 변화와 자원 예산으로 넓어지고 있다. [src_004] [src_005] [src_006]
3. <!-- clm_004 --> Agent serving은 token 처리량만 보면 부족하다. Stateful sandbox의 idle-burst 패턴, 복구 비용과 격리 경계를 함께 관찰해야 한다. [src_005] [src_010] [src_011]
4. <!-- clm_005 --> Kubernetes GPU 공유는 정수형 GPU 요청에서 device claim·topology·hardware partition·tenant isolation을 묶는 방향으로 이동한다. [src_007] [src_009]
5. <!-- clm_006 --> 이번 주 cloud-native AI 변화의 공통점은 만능 agent abstraction이 아니라 networking, resource claims, sandbox, SDK 같은 강제 가능한 control-plane primitive의 강화다. [src_007] [src_008] [src_012]
6. <!-- clm_007 --> Edge AI는 cloud 제거가 아니라 workload placement 문제다. Device 제약과 latency·privacy·connectivity를 기준으로 local inference와 cloud orchestration을 나눠야 한다. [src_013] [src_014] [src_015]

## Confidence

- 전체 결론: Medium-High
- 공식 Kubernetes·Red Hat·NVIDIA 운영 변화: High
- Self-evolving harness 구조적 방향: Medium
- 논문 성능 수치와 넓은 production 도입: 검증 보류

## Refuted

- Edge-only 서사는 공식 학습 구현과 산업 분석의 hybrid placement 전제와 맞지 않는다.

## Unresolved

- Living-Harness와 AIDE²의 성능 수치는 독립 재현 전까지 일반화하지 않는다.
- Agent Sandbox 및 DRA/MIG의 장기 대규모 도입 수준은 아직 확인하지 못했다.
- 공개 커뮤니티 게시물은 관심 신호일 뿐 production 보급 증거가 아니다. [src_016] [src_017] [src_018]
