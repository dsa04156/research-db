# Weekly AI Infrastructure Trends — 2026-08-18

## 조사 범위와 방법

2026-08-11부터 2026-08-18까지 self-evolving harness, AI agents, Kubernetes, cloud/distributed systems, edge AI를 조사했다. 공식 문서·공식 GitHub 릴리스·Kubernetes/CNCF 자료를 우선했고, Reddit·HN·YouTube·TikTok·LinkedIn·Threads는 후보 발굴과 반론 탐색에만 사용했다. X/Twitter는 제외했다. 핵심 결론은 서로 다른 도메인 두 곳 이상이 지지하고 검증 게이트를 통과한 주장만 사용했다. 시드 글은 하네스를 모델 주변의 개선 가능한 시스템으로 보는 분석 틀을 제공했다. [src_015] HN 글은 DeepSeek 공식 원문을 찾는 발견 경로로만 사용했다. [src_003]

## 1. Self-evolving harness

DeepSeek Harness는 모델 어댑터, 도구, 세션과 실행 루프를 교체 가능한 구성요소로 제공하는 공개 하네스를 내놓았다. 중요한 점은 “새 모델”이 아니라 모델을 둘러싼 실행 구조가 독립 제품·공개 소프트웨어 층으로 부상했다는 것이다. 같은 기간 OpenAI Agents SDK는 모델 호출 타임아웃, 실행 단위 샌드박스 작업 디렉터리, Docker 네트워크 차단, 정확한 승인 결정 반영을 추가했다. 서로 다른 구현이지만 공통 방향은 하네스를 설정 모음이 아니라 상태·권한·실패를 관리하는 런타임으로 취급하는 것이다. [src_001] [src_002] [src_004]

## 2. AI agents

에이전트 SDK의 변화는 기능 수보다 검증 가능성과 실패 경계에 집중된다. OpenAI Agents SDK v0.21.0은 공급자 호출 없이 수행하는 결정론적 테스트 도구, 상태 스냅샷 격리, MCP 수명주기 격리와 오류 민감정보 삭제를 포함했다. v0.21.1은 타임아웃, 네트워크 차단, 실행별 작업 공간, 사용량 집계와 승인 정확성을 보강했다. InfoQ의 agentic fitness functions 분석도 버전된 루브릭과 지속 평가 루프를 운영 구조로 제시한다. 이 흐름은 장기 실행 에이전트에서 “잘 답하는가”보다 “실패를 재현하고 제한하고 복구할 수 있는가”가 중요해졌음을 보여준다. [src_004] [src_005] [src_006]

Anthropic의 시스템 프롬프트 공개 문서는 투명성 논의를 키웠지만, 해당 프롬프트 변경은 Claude API에 그대로 적용되지 않는다고 명시한다. 따라서 공개 프롬프트를 API 에이전트의 실제 정책 전체로 간주해서는 안 된다. [src_013]

## 3. Kubernetes와 cloud-native AI

이번 주 직접적인 생태계 이정표는 Kubeflow의 CNCF 졸업이다. 이는 개별 기능의 성능 우위가 아니라 프로젝트 거버넌스, 유지관리, 채택과 수명주기가 성숙 단계에 들어섰다는 신호다. AI 파이프라인과 모델 운영을 Kubernetes 위에서 표준화하려는 흐름이 실험 도구 수준을 벗어나고 있다. [src_007] [src_008]

GPU 운영에서는 Dynamic Resource Allocation(DRA)이 핵심이다. Kubernetes v1.36 문서는 장치 분할, 우선순위 대체 자원, 장치 건강 상태, binding condition과 workload 단위 ResourceClaim을 확장한다. NVIDIA GPU DRA 드라이버는 GPU와 ComputeDomain을 관리하지만 일부 GPU 기능은 아직 공식 지원 전이거나 기본 비활성이다. 따라서 운영자는 기존 device plugin을 즉시 제거하기보다 DRA API, 드라이버 버전, feature gate, MIG·NVLink 요구사항을 함께 검증해야 한다. [src_009] [src_010]

## 4. Cloud·distributed systems

CNCF의 Kairos 사례는 Kubernetes 업그레이드를 선언적 상태와 건강 검사에 연결해 자동 복구하는 방향을 보여준다. Cloudflare workerd 릴리스는 GC strong-root 누수와 스트림 참조 수명 문제를 수정했다. OpenAI Agents SDK도 실패 후 provider 자원 정리와 스트림 종료를 강화했다. 서로 다른 계층에서 반복되는 공통점은 자동화 수준이 높아질수록 수명주기 누수와 실패 복구가 핵심 비용이 된다는 것이다. [src_011] [src_012] [src_004]

HAProxy 제어면에 LLM 정책을 적용한 preprint는 작은 모델의 실패, reasoning 비용 증가, 장애 격리 후 tail latency 상승을 보고한다. 흥미로운 초기 연구지만 단일 preprint이므로 핵심 결론에는 포함하지 않았다. [src_014]

## 5. Edge AI

이번 주 Edge AI에서 독립적으로 확인된 대형 제품 전환은 적었다. 대신 workerd 같은 엣지 런타임에서 메모리 수명과 스트림 안전성을 다듬는 변화가 이어졌다. SNS에서는 “저지연·개인정보·온디바이스” 메시지가 반복됐지만 구체적 성능·비용 비교가 부족해 lead-only로 남겼다. [src_012]

## 분야를 가로지르는 연결

다섯 분야의 공통 축은 **제어 가능한 실행**이다. 하네스는 플러그인과 상태 관리로, 에이전트 SDK는 테스트와 승인으로, Kubernetes는 DRA와 workload-aware scheduling으로, cloud/edge 런타임은 누수 제거와 복구로 같은 문제를 해결한다. 모델이 더 많은 행동을 맡을수록 권한 경계, 자원 수명, 비용 계측, 실패 재현이 인프라의 중심이 된다.

## 운영 권고

- 에이전트 릴리스 게이트에 결정론적 scripted model, timeout, max-turn, 네트워크 차단, 승인 회귀 테스트를 포함한다.
- Kubernetes GPU 도입은 DRA 기능 단계와 드라이버 기본값을 표로 관리하고 기존 device plugin과 병행 검증한다.
- 자동 복구 파이프라인은 성공 시간뿐 아니라 rollback, quorum, 리소스 누수와 tail latency를 함께 측정한다.
- SNS engagement는 후보 우선순위로만 사용하고 성능·비용 수치는 공식 원문 또는 재현 자료가 없으면 미확정으로 유지한다.
