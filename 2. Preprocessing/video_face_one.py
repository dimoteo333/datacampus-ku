import cv2
import glob
import dlib
import numpy as np
import os
import imutils
from matplotlib import pyplot as plt
from imutils import face_utils

#전처리 1-2
#앵커 얼굴이 1명만 화면 상에 나타날때 까지의 영상을 자른다.

def one_anchor_only (MOV_Directory):
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    MOV_List = os.listdir(MOV_Directory)

    for MOV in MOV_List:
        MOV_name = MOV_Directory + '/' + MOV

        video =  cv2.VideoCapture(MOV_name)

        fps = video.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        size = (round(width), round(height))
        out = cv2.VideoWriter('./One_Anch/%s.mp4' %MOV, fourcc, fps, size)

        while(video.isOpened()):
        
            ret, frame = video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.25, 6)

            if len(faces) == 1:
                out.write(frame)
            else:
                break

        out.release()
    
    return './One_Anch' #자른 영상들이 있는 디렉토리 반환


#문제 1.
#소리가 함께 나오지 않음 -> 이건 전처리 1이 끝난 뒤, ffmpeg등을 사용해
#원본 video를 소리와 함께 잘라내는 방식을 사용하는 것이 좋을 것 같다.
