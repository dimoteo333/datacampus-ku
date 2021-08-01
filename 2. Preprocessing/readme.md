#전처리 단계

1, 앵커가 말하는 부분(앵커 얼굴이 나오는 화면)만 분할 - Video_of_one_Anchor.ipynb

  1) 인물 배경 있는 영상 제거 -> 인물 배경 있는 영상(주로 정치 분야)은 STT로 전처리하는 방식 고려
  2) 인물 배경 없는 영상 리스트 만들기
  3) face detection이 2명 이상 되었을 때 -> drop out
  4) 긴 침묵 (video_segment)을 기준으로 crop -> 3번 보완 방식으로 진행할 예정

2, 영상에서 audio 파일 추출 - video_frame_face.py (초반 부분)

3, audio파일에서 silence 기준으로 단어 혹은 문장 범위 타임 스탬프 추출 - video_segment.py

4, 해당 타임 스탬프로 영상 분할 - video_segment.py

5, 분할한 영상을 프레임으로 나눈 뒤, face detection하고 이미지 저장 - video_frame_face.py

6, 얼굴에서 하관 부분만 분리 - video_frame_face.py


#Video_frame_face 문제점

1, 저화질일 때 하관 부분(특히 턱부분)을 잘 crop하지 못함 -> 코드 수정(확인 요청)

2, frame이 숫자 순서대로가 아니라, 1, 100, 101,,,, 순으로 진행됨 -> sorted로 해결 가능, 전처리 1 해결 후 생각해볼 것.

