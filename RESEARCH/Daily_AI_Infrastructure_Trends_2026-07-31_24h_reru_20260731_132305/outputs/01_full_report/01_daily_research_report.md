# Daily AI Infrastructure Trends - 2026-07-31 rerun

## 범위와 방법

실행 시점 최근 24시간 자료를 우선하고 최근 7일을 누락 복구 창으로 사용했다. X/Twitter는 제외했다. SNS engagement는 우선순위 신호로만 사용했고 핵심 결론은 독립 도메인 둘 이상으로 확인된 주장만 사용했다.

## Verified findings

1. **Harness의 단위가 넓어졌다.** 최근 연구와 구현은 harness를 context·skills·evaluation·verification·memory·security·infrastructure optimization을 함께 조절하는 운영 계층으로 다룬다. [src_001] [src_003] [src_013]
2. **자기개선 대상이 협업 구조로 이동한다.** SKIMIX의 skill mixture, MANTA의 topology update, AgentRadio의 실행 중 비동기 정보교환, Asari의 serving configuration loop는 서로 다른 계층을 개선 대상으로 둔다. [src_002] [src_004] [src_005] [src_013]
3. **Production readiness는 외부 집행 계층을 요구한다.** 권한·sandbox·provenance·memory recovery와 audit는 model의 자기판단에 맡기기보다 강제 가능한 경계로 분리해야 한다. [src_001] [src_007] [src_008] [src_020] [src_021]
4. **Kubernetes 공급망 검증은 runtime 경로까지 내려가야 한다.** admission webhook만으로는 static pod와 direct kubelet 경로가 남을 수 있으며 NRI plugin이 runtime 보완 방식을 구현한다. [src_009] [src_010]
5. **Inference 성능은 full-stack control-plane 문제다.** Triton Control과 Modelplane은 model lifecycle과 fleet operations를 통합하려 하고, Asari·NVIDIA·OpenAI 자료는 topology·runtime·scheduler·routing·correctness를 함께 검증해야 함을 보여준다. [src_011] [src_012] [src_013] [src_014] [src_015]
6. **Edge는 hybrid placement 문제다.** 공개 model, 산업 연구와 foundation orchestration 자료는 workload별 latency·bandwidth·privacy·connectivity 제약에 따라 cloud와 edge 역할을 나눈다. [src_016] [src_017] [src_018]

## 운영 영향

- Harness evaluation에는 최종 점수 외에 topology 변경, message flow, tool call, policy decision과 recovery event를 trace로 남겨야 한다.
- Kubernetes 운영자는 admission policy와 runtime NRI policy의 coverage 차이를 테스트해야 한다.
- GPU inference platform은 model server 설치보다 placement, routing, performance test, credentials, artifact provenance와 lifecycle을 하나의 운영 표면으로 만드는 일이 중요하다.
- Edge 배치는 단말 성능만 보지 말고 연결 단절, data gravity, privacy, cloud fallback과 fleet update 경로를 함께 설계해야 한다.

## Unresolved

- MANTA·AgentRadio·SKIMIX의 성능 개선 폭은 독립 재현과 비용 정규화 전까지 구조적 가능성으로만 본다. [src_002] [src_004] [src_005]
- PAIChecker의 SWE-bench 계열 정합성 문제는 중요하지만 보고 비율을 전체 benchmark 생태계에 그대로 일반화하지 않는다. [src_006]
- Triton Control과 Modelplane은 실제 구현이지만 광범위한 production 채택을 입증하지 않는다. [src_011] [src_012]
- Agent Harness Distillation의 추출·방어 결과는 저자 외 검증이 필요하다. [src_019]
- MemTxn·ChronoMem의 production 비용과 장기 복구 효과는 아직 독립 운영 자료가 없다. [src_020] [src_021]
- Instagram·LinkedIn 신호는 조사 질문을 만드는 데만 사용한다. [src_022] [src_023]

## Refuted

이번 실행에서 확정적으로 반박된 핵심 주장은 없다.

## Confidence

구조적 결론은 Medium-High, 신규 preprint의 정량 성능과 초기 프로젝트 채택 신호는 Low-Medium이다.

## Source registry coverage

보고서는 등록된 모든 근거를 인용했다: [src_001] [src_002] [src_003] [src_004] [src_005] [src_006] [src_007] [src_008] [src_009] [src_010] [src_011] [src_012] [src_013] [src_014] [src_015] [src_016] [src_017] [src_018] [src_019] [src_020] [src_021] [src_022] [src_023]
