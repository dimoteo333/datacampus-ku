import cv2
import glob
import dlib
import numpy as np
import os
import imutils
from matplotlib import pyplot as plt
from imutils import face_utils


def face_crop_vid (MOV_Directory):
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    MOV_List = glob.glob(MOV_Directory + '*.mp4')
    MOV_List = os.listdir(MOV_List)

    for MOV in MOV_List:
        MOV_name = MOV_Directory + '/' + MOV

        video =  cv2.VideoCapture(MOV_name)

        fps = video.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        size = (round(width), round(height))
        out = cv2.VideoWriter('./FINAL_VID/%s.mp4' %MOV, fourcc, fps, size)

        while(video.isOpened()):
        
            ret, frame = video.read()
            
            if frame is None:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.25, 6)

            for (x, y, w, h) in faces:
                cropped = frame[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]


            out.write(cropped)

        out.release()
    
    return './FINAL_VID'