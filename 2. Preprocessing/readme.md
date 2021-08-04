#전처리 단계

1, 앵커가 말하는 부분(앵커 얼굴이 나오는 화면)만 분할 - Video_of_one_Anchor.ipynb

  1) 만약 시작부터 앵커 얼굴이 0명 또는 2명 이상이라면 video drop out -> One_anchor_starts_MOV.ipynb
  2) 만약 얼굴이 0명 또는 2명 이상이 되면 video cut (time stamp) -> video_face_one.py
  3) 앵커 목소리가 기자 목소리로 전환될 때 video cut (time stamp) -> 

2, 영상에서 audio 파일 추출 - video_segment.py (초반 부분)

3, audio파일에서 silence 기준으로 단어 혹은 문장 범위 타임 스탬프 추출 - video_segment.py

4, 해당 타임 스탬프로 영상 분할 - video_segment.py

5, 분할한 영상을 프레임으로 나눈 뒤, face detection하고 이미지 저장 - video_frame_face.py

6, 얼굴에서 하관 부분만 분리 - video_frame_face.py


#Video_frame_face 문제점

1, frame이 숫자 순서대로가 아니라, 1, 100, 101,,,, 순으로 진행됨 -> sorted로 해결 가능, 전처리 1 해결 후 생각해볼 것.

2, lipjpeg-turbo 사용

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=lucidmaj7&logNo=220769743363
설치해야 하는 것들이 많음...

3, test_frame.py 주의사항
  1) 주피터 노트북에 Preprocessing에 있는 함수들을 먼저 실행하고 마지막에 돌릴 것
  2) Switching_moment()에서 timestamp 가져오는 작업이 아직 끝나지 않았음
