# 일일 심층 연구 보고서

## 1. 범위와 방법

이번 실행은 2026-07-30 기준 최근 30일의 기술·커뮤니티 신호를 우선 탐색하고,
2024-2026의 배경 연구로 맥락을 보완했다. 구조화 수집기와 공식 RSS·릴리스,
arXiv 및 비-X SNS를 함께 조사했다. 중복은 canonical URL·DOI·arXiv ID를
우선 키로 제거했다.

핵심 결론은 서로 다른 도메인 두 곳 이상의 근거가 있는 주장만 사용했다.
SNS는 발견 경로와 관심 신호로만 두었고 성능 수치와 채택률은 별도 검증 없이는
결론으로 승격하지 않았다.

## 2. 자기진화형 하네스

하네스는 단순 프롬프트 껍데기가 아니라 모델의 실행 루프, 도구 호출, 컨텍스트,
지속 상태, 평가와 권한을 조정하는 런타임 계층으로 이동하고 있다
([src_001](https://lilianweng.github.io/posts/2026-07-04-harness/)).
최근 프리프린트들은 하네스 자체를 탐색·최적화 대상으로 만들지만
([src_003](https://arxiv.org/abs/2607.15524);
[src_004](https://arxiv.org/abs/2607.13683)), 동일 계산 예산에서 단순 재시도나
test-time scaling보다 항상 우월하다고 볼 수 없고 held-out 일반화도 제한될 수
있다 ([src_002](https://arxiv.org/abs/2607.12227)).

따라서 개인 자동화에서 먼저 구현할 것은 무제한 자기수정이 아니다. 실패 기록,
제한된 변경 제안, 독립 평가, 회귀 테스트, 승인·롤백 로그의 폐루프가 우선이다.
성능 향상 수치는 출발점이 아니라 검증 대상이다.

## 3. 에이전트 런타임과 Kubernetes

AI 작업은 CPU·GPU 적합성, VRAM 경합과 런타임 상태가 도구마다 달라 단순
GPU-first 정책으로 충분하지 않을 수 있다
([src_005](https://arxiv.org/abs/2607.22242)). Kubernetes v1.36의 DRA와
Workload·PodGroup 변화는 특수 장치 요청과 그룹 단위 배치를 기본 오케스트레이션
문제로 끌어올린다
([src_006](https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/);
[src_007](https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/)).

추론 계층에서는 llm-d가 라우팅, 캐시, 분리형 서빙과 Gateway API 연계를
Kubernetes 위에 묶고 있으며 릴리스가 계속 운영 기능을 확장한다
([src_008](https://github.com/llm-d/llm-d);
[src_009](https://github.com/llm-d/llm-d/releases)). NVIDIA Topograph는
토폴로지 라벨을 통해 네트워크 지역성과 가속기 배치를 스케줄러가 읽게 한다
([src_010](https://docs.nvidia.com/topograph/engines/kubernetes)).

장기 실행 에이전트 자체는 stateless 서비스와도 다르다. 하나의 에이전트를
하나의 Pod에 직접 대응시키면 대규모 상태·격리·idle 수명주기 관리가 비효율적일
수 있다
([src_011](https://www.cncf.io/blog/2026/07/14/is-a-pod-the-right-deployment-unit-for-an-ai-agent/)).
Kubernetes Agent Sandbox는 stable identity, 격리, suspend/resume, warm pool을
위한 별도 추상화를 제안한다
([src_012](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/)).

## 4. 클라우드·엣지

엣지-클라우드 연속체는 배치, 이동, 네트워크와 자원 제약을 함께 다루는
오케스트레이션 문제다
([src_013](https://doi.org/10.1109/JIOT.2026.3663918)). LLM 요청 라우팅
연구도 cloud-only 또는 edge-only의 이분법 대신 응답 품질, 지연, 비용을 함께
최적화한다 ([src_014](https://arxiv.org/abs/2507.15553)). 개인 연구 DB에서는
“엣지가 뜬다”보다 어떤 워크로드가 어떤 조건에서 이동하는지를 추적해야 한다.

## 5. 커뮤니티 신호

SNS에서는 하네스 성능을 matched-compute 기준으로 비교하자는 문제 제기
([src_015](https://www.tiktok.com/@rajistics/video/7664394161205923102)),
하네스·메모리·평가를 묶는 교육 콘텐츠
([src_016](https://www.linkedin.com/posts/shen-sean-chen_you-can-learn-ai-agent-harness-loop-engineering-activity-7478447459745210368-R6DR)),
DRA를 AI 플랫폼 자원 계층으로 보는 관심
([src_017](https://www.linkedin.com/posts/kubefm_kubernetes-currently-manages-cpu-memory-activity-7485056484427522049-lm1O)),
거버넌스를 둔 자기개선 메모리 프로젝트
([src_018](https://www.reddit.com/r/ContextEngineering/comments/1va8gr5/dejadb_governed_selfimproving_memory_for_ai_agents/))가 보였다.
이들은 다음 검색어를 정하는 데는 유용하지만 검증된 채택 추세는 아니다.

## 6. 다음 추적 항목

1. 하네스 논문이 동일 추론 예산, held-out split, 회귀 테스트와 독립 평가기를
   모두 제공하는지 확인한다.
2. Agent Sandbox, llm-d, Gateway API Inference Extension의 API 안정성과
   실제 릴리스 변화를 추적한다.
3. DRA·PodGroup·토폴로지 인지 스케줄링이 함께 사용된 공개 운영 사례를 찾는다.
4. cloud-edge 라우팅 연구에서 품질·지연·비용 외에 프라이버시와 에너지를 같은
   실험으로 측정한 재현 자료를 찾는다.

## 7. 한계

최근성 때문에 D등급 프리프린트 비중이 높고 SNS는 E등급이다. 이번 보고서는
기술 방향과 연구 질문을 정하는 용도이며, 개별 성능 수치나 시장 규모를
확정하는 자료가 아니다.
