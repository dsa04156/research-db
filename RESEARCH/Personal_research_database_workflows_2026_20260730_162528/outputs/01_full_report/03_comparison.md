# 3. 현재 로컬 DB와 공개 사례 비교

| 계층 | 현재 로컬 구현 | 공개 사례 | 판단 |
|---|---|---|---|
| 수집 | arXiv, Crossref, OpenAlex, RSS, GitHub | arXiv, Semantic Scholar, Zotero | 현재 구현이 더 넓음 |
| 중복 | DOI, arXiv ID, URL, 제목·연도 | DOI, arXiv ID, 제목·저자·연도, 콘텐츠 해시 | 거의 동일 |
| 상태 DB | SQLite `items`, `topics`, `sightings`, `runs` | SQLite 처리 상태와 실행 로그 | 동일한 방향 |
| 자료별 한국어 요약 | 아직 없음 | 자료별 구조화 노트·JSON | 추가 필요 |
| 사람 노트 | 일일 종합만 존재 | 한 자료당 한 소스 노트 | 추가 필요 |
| PDF 전문 검색 | 없음 | PaperQA2/Qdrant 계층 | 필요해질 때만 추가 |
| 인간 검토 | `pending` 상태만 존재 | relevant/not relevant, done/error, human oracle | 상태 확장 필요 |

Obsidian의 Properties는 작은 원자적 메타데이터를 YAML frontmatter로 다룰 수 있지만 중첩 데이터와 대량 상태 변경에는 제한이 있다. 따라서 복잡한 처리 상태와 AI 출력 버전은 SQLite에, 사람이 볼 핵심 필드만 Markdown frontmatter에 복제하는 편이 적합하다. (src_003; [Obsidian Properties](https://obsidian.md/help/properties))

검증된 결론은 **원문 메타데이터, AI가 만든 자료별 요약, 여러 자료를 묶은 종합 보고서는 서로 다른 저장 계층으로 분리해야 추적성과 재처리가 쉬워진다**는 것이다. (clm_004; src_003, src_007, src_008)
