1, 앵커가 말하는 부분(앵커 얼굴이 나오는 화면)만 분할 - X

2, 영상에서 audio 파일 추출 - O

3, audio파일에서 silence 기준으로 단어 혹은 문장 범위 타임 스탬프 추출 - video_segment.py

4, 해당 타임 스탬프로 영상 분할 - video_segment.py

5, 분할한 영상에서 face detection - video_face.py

6, 얼굴에서 하관 부분만 분리 - X
