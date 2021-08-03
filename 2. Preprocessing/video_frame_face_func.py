import cv2
import glob
import dlib
import numpy as np
import os
import imutils
from matplotlib import pyplot as plt
from imutils import face_utils


def video_frame_face(MOV_Directory):
    
    MOV_List = os.listdir(MOV_Directory)

    for MOV in MOV_List:
        MOV_name = MOV_Directory + '/' + MOV

        video =  cv2.VideoCapture(MOV_name)

        i = 0

        a = str(MOV)

        while(video.isOpened()):
            ret, frame = video.read()
            if ret == False:
                break
            cv2.imwrite("./Frame/%s_frame_%d.jpg" %a %i, frame) #이름 변경, 저장할 공간 생각
            i+=1
        
        
        images = glob.glob('./Frame/%s_frame_*.jpg' %a) #디렉토리


        face_detecor = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

        count = 0
        for i in images:
            print(i)
            img = cv2.imread(i)
            img = cv2.resize(img, (600,600))
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            faces = face_detecor(gray, 1)

            for face in faces:
                landmarks = predictor(gray, face)
                shape = face_utils.shape_to_np(landmarks)

                (x, y, w, h) = face_utils.rect_to_bb(face)
                crop_img = img[shape[1][1]:y+h+int(h/4)*2, shape[1][0]:shape[15][0]]
                crop_img = cv2.resize(crop_img, (600,600))

            cv2.imwrite("./Cutted_F/%s_frame_%d.jpg" %a %count, crop_img)
            count += 1

    return './Cutted_F' #잘린 이미지 디렉토리