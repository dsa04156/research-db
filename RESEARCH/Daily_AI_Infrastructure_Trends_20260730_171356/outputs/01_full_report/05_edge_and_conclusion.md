# 5. 엣지 AI와 연구 우선순위

## 검증된 핵심 주장

**clm_005 — 엣지 AI의 최근 연구·산업 논의는 클라우드의 전면 대체보다
워크로드별 하이브리드 배치, 이기종 장치 재현성, 자원 할당의 자기보정을
강조한다.**

ARM 엣지 장치 연구는 이기종 microkernel에서도 재현 가능한 추론 결과를 만들기
위한 정밀도·양자화 선택을 다룬다
([src_012](https://arxiv.org/abs/2607.23227)). 다른 프리프린트는
ground truth가 고정되지 않은 엣지 자원 예측에서 drift를 줄이기 위한
self-calibration을 제안한다
([src_013](https://arxiv.org/abs/2607.22400)). 업계 기고는 지연·민감
데이터·반복 비용이 중요한 작업은 로컬이나 엣지에 두되, 탄력성과 프런티어
모델 접근이 중요한 작업은 클라우드에 남기는 하이브리드 배치를 주장한다
([src_014](https://www.techradar.com/pro/the-case-for-moving-creative-production-ai-to-the-edge)).

## 개인 연구 DB에 바로 반영할 설계

1. **자료 수집과 Zotero를 분리한다.** SQLite는 모든 발견·중복·실패 이력을
   보존하고 Zotero는 읽을 가치가 있는 항목의 인박스로 사용한다.
2. **하네스 변경을 연구 객체로 만든다.** 변경 전후 버전, evaluator, 승인 결과,
   실패 궤적을 한 레코드로 연결한다.
3. **논문과 블로그를 같은 DB에 넣되 품질 등급은 분리한다.** 프리프린트와
   벤더 블로그의 수치를 확정 사실로 승격하지 않는다.
4. **Kubernetes 기능의 성숙도를 별도 필드로 둔다.** Sandbox와 production
   기능이 일일 브리핑에서 섞이지 않게 한다.
5. **엣지 배치 판단에 workload profile을 저장한다.** latency, privacy,
   accelerator, energy, connectivity, reproducibility를 공통 비교축으로 둔다.

## 결론

이번 주 자료의 공통점은 자기진화를 “자유로운 자기수정”으로 보지 않는다는
것이다. 개선 대상은 하네스 상태와 절차로 좁히고, 외부 검증과 rollback을
두며, 실행 궤적과 메모리를 관찰하고, 인프라 계층에서는 자원을 단계별로
배치한다. 개인 연구 시스템도 같은 원칙을 따르면 된다. **광범위하게
수집하되, 승인과 단정은 좁고 검증 가능하게 유지한다.**

## Confidence

방향성은 독립 도메인 교차검증을 통과했다. 개별 성능 수치는 대부분 최신
프리프린트에 있으므로 실험 재현 전까지 참고 지표로만 사용한다.

## Refuted

없음.

## Unresolved

없음. 다만 자동 하네스 진화의 보편적 우월성과 Sandbox·alpha 기능의
production readiness는 이 리포트가 주장하지 않는다.
