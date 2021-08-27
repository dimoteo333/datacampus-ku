# 데이터청년캠퍼스 고려대학교 5조

## 프로젝트 소개
- 팀원 : 이우준, 안혜준, 이태희, 임준혁, 송문영
- 프로젝트 명 : Lip2Text
- 프로젝트 설명 : 독화술을 제공해 자막 형태로 제공
- 연구분야 : Computer Vision, Natural Language Processing
- 개발기간 : 2021-06-28 ~

## 사용 예정 데이터
- 데이터 수집 기간 (전처리 기간 포함)
  - 2021.07.22 ~ 2021.08.26
- 네이버 뉴스 영상<br><br>
  <img src="https://user-images.githubusercontent.com/78715821/126625141-3a16ac16-0316-4945-8b21-be35e578936e.png" width="75%" height="75%">

  > http://news.naver.com/main/read.naver?mode=LSD&mid=sec&sid1=001&oid=052&aid=0001617819
  - 2014년부터 제공되고 있는 신문사들의 뉴스 데이터를 크롤링
  - 한명의 앵커가 얘기하고 있는 영상/음성/텍스트 이용
  - 동영상의 음성을 활용해 텍스트와 영상의 입모양을 매칭시킴
  - __1년에 대략 5만 2천개, 총 30만개 이상의 데이터를 확보 가능__
<br><br>
- 단어 단위 입모양 데이터<br><br>
  <img src="https://user-images.githubusercontent.com/78715821/126626307-96c608a6-15f6-48f9-859c-4b4febc65f8a.jpg" width="75%" height="75%">
 
  > https://aihub.or.kr/aidata/33813
  - 자주 사용하는 한글 1000개의 단어 발화 영상
  - 200명의 배우들이 다양한 성별과 나이로 구성되어 모델의 유연성 확보 가능

## 사용 예정 데이터의 한계
- 네이버 뉴스 영상

  - 영상과 대본의 싱크를 맞추는 문제점
  - 실제 alignment를 단어 단위로 처리할 시 너무 많은 시간이 걸릴 것
- AIHub의 베타 버전
 
  - 데이터의 부족 : 1000개의 어휘 중 양이 적은 감탄사, 관형사 등만 공개됨
  - 데이터가 아직 처리 중이며 공개 일정이 미정

- 사용 예정 데이터의 한계 극복 방안

  - 메인 모델의 학습 및 예측을 단어가 아닌 문장 단위로 진행하고자 함
  - 문장 단위 데이터
      - 유튜브에서 생성되는 자동 자막을 이용해 문장 단위로 alignment

## 사용 데이터
<img src="https://user-images.githubusercontent.com/87217639/131153084-630fd3d7-f0ff-4530-8470-dfcb55932cc0.jpg"  width="700" height="370">

> https://www.youtube.com/user/pitchforktv
- 유튜브 영상
  - Pitchfork의 over / under 인터뷰 영상을 크롤링
  - 한 명이 발화하고 있는 영상/음성/텍스트 이용
  - 유튜브 자동 자막을 사용해 영상을 문장 단위로 크롭
  - 영상의 텍스트와 영상의 입모양을 매치시킴


## 데이터 전처리
![image](https://user-images.githubusercontent.com/78715821/126666663-eff812ca-d669-47a0-befa-f6df8787fc49.png)
- 뉴스 영상의 경우, 음성과 텍스트의 싱크를 맞추기 위해 forced alignment를 이용한다.
  > https://web.sas.upenn.edu/phonetics-lab/facilities/ <br>
  > https://www.speechsciences.or.kr/board/view?b_name=bo_reference&bo_id=17&per_page=15
- 그 후 동영상을 한 단어의 발음 시간과 맞게 1~2초 내외로 잘라 모델 학습에 이용한다

## 데이터 Features
![output_15_0](https://user-images.githubusercontent.com/87217639/131155569-889d2559-fc76-4204-a760-364010a2a4cf.png)

- 단어 단위가 아닌, 문장 단위의 영상/텍스트 데이터
- 얼굴 이외의 부분은 영상 데이터에서 필요하지 않다고 판단
- 발화 중 얼굴 ROI만을 크롭해 영상 데이터들을 모두 같은 크기로 저장

### 사용한 모델
- 문장 단위로 Lip reading 학습을 진행한 모델
  <img src="https://user-images.githubusercontent.com/87217639/131153040-f5491e6e-2cb1-4ede-8d9a-75844d00f1c1.jpg"  width="600" height="300">

  - STCNN + Transformer (+ Language Model)
  - 인코더는 MV-LRS로 단어 단위 분류를 진행하도록 학습
  - 디코더는 문장으로 이루어진 LRS 데이터셋으로 학습된 Transformer 모델

- 데이터 학습
  - 부족한 시간 및 데이터로 인해, 영어로 학습되어 있는 기존의 모델에 유튜브 영상을 학습
  - 영어 화자 유튜브 영상을 Lip reading 모델에 적용

- 학습 결과
  - WER(에러 수치) 98%
    - 논문과의 차이점 : 사람 이름, 제품명 등의 고유 명사에 대한 학습이 진행되어 있지 않음

### 한계점 및 활용 방안
- 추후 AIHub의 한글 단어 데이터가 공개될 시 한국어 독순술 모델 제작 가능
- 입력과 출력, 그리고 사용하는 모델에 따라 실시간 독순술 처리 모델 제작 가능

