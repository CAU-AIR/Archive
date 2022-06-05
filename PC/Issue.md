### 1. Avalanche 툴은 아직 호환성에 매우 민감 (OS, python version, pytorch version, cuda version ...)
  --> 현재 셋팅: window10, python 3.8.13, pytorch 1.11.0, cuda 11.3

### 2. Avalanche의 최신 버전과 Doc내용 불일치
  --> e.g. 두개 이상의 strategies 결합하여 사용하는 기능을 지원하는 avalanche.training.strategies 제거됨
  
### 3. 몇가지 호환되지 않는 dataset-strategy 조합이 있음
  --> e.g. video datasets - ICaRL ... (데이터 전처리 코딩 요구)
  
### 4. Jetson Nano 환경(python 3.6.9)에서 실험 셋팅시 많은 시간 소모가 예상됨
  --> 파이썬 버전이 낮아지면서 필요한 코드부분만 가져와서 셋팅해야 함
  --> 많은 상속과 외부 라이브러리들 사용 (python 3.6.9에서 지원안되는 외부 라이브러리의 경우 새로 구현 요구)
