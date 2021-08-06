# 전처리 단계

1, 앵커가 말하는 부분(앵커 얼굴이 나오는 화면)만 분할

  1) 만약 영상 데이터의 길이가 2분을 초과한다면 video drop out -> File_selection.ipynb
     만약 시작부터 앵커 얼굴이 0명 또는 2명 이상이라면 video drop out -> File_selection.ipynb
  2) 만약 얼굴이 0명 또는 2명 이상이 되면 video cut (time stamp) -> video_face_one.py
  3) 앵커 목소리가 기자 목소리로 전환될 때 video cut (time stamp) -> Detect_Speaker_switching.ipynb -> 1-2가 거의 항상 더 빠른 timestamp를 내놓기 때문에 text_frame.py에서 제거

2, 영상에서 audio 파일 추출 - video_segment.py (초반 부분)

3, audio파일에서 silence 기준으로 단어 혹은 문장 범위 타임 스탬프 추출 - video_segment.py

4, 해당 타임 스탬프로 영상 분할 - video_segment.py

5, 분할한 영상의 얼굴 부분 crop한 영상 - face_crop_vid.py

6, crop한 영상과 맞는 오디오 합치기 - concat_vid_aud.py

7, 완전한 영상과 그에 맞는 text - 


# test_frame.py 주의사항
  1) 주피터 노트북에 Preprocessing에 있는 함수들을 먼저 실행하고 마지막에 돌릴 것
