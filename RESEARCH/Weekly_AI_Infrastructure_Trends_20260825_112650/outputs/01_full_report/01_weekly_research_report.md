# Weekly AI Infrastructure Trends — 2026-08-25

## 검증된 변화

clm_001: 에이전트 하네스는 프롬프트와 도구를 묶는 얇은 루프에서 세션 상태, 승인, 격리, 복구 경계를 책임지는 독립 실행 계층으로 구체화되고 있다. Earendil의 개념 분해, Pi의 crash-safe 설계, TrueForge의 로컬·호스티드 배포가 서로 다른 형태로 같은 실행 계층을 가리킨다. [src_001] [src_002] [src_003]

clm_002: 하네스가 배포 시 실행 루프뿐 아니라 에이전트 강화학습의 환경 상호작용과 학습 데이터 경계까지 소유하는 방향이 실제 프레임워크로 나타났다. 다만 논문 성능 수치는 독립 재현 전이므로 채택 근거가 아니라 연구 방향 신호로만 본다. [src_004] [src_005]

clm_003: Kubernetes 기반 LLM 서빙에서는 일반적인 Pod·Service 상태만으로 부족하며 KV 캐시 위치, 대기열과 요청 우선순위를 읽는 추론 전용 라우팅 계층이 운영상 중요하다. llm-d의 endpoint picker와 독립 요청 경로 분석이 이를 교차 확인한다. [src_006] [src_007]

## 운영 판단

에이전트 런타임은 operation log, idempotent tool boundary, restart recovery, approval policy를 모델 호출과 분리해 설계할 가치가 있다. Kubernetes 추론에서는 GPU 사용률뿐 아니라 prefix-cache hit, queued tokens, prefill/decode 단계와 라우터 장애 시 fail-open/close 선택을 관측해야 한다.

## 조사 범위

검토된 추가 자료: [src_008] [src_009] [src_010]. 이들은 검증 상태가 부족하거나 반증되어 핵심 결론에서 제외했다. X/Twitter는 조사하지 않았다.
