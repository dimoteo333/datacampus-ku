import cv2
import glob
import dlib
import numpy as np
import os
import imutils
from matplotlib import pyplot as plt
from imutils import face_utils

#video -> image frame
#open video

video = cv2.VideoCapture("video.mp4") #video name change

i = 0

while(video.isOpened()):
    ret, frame = video.read()
    if ret == False:
        break
    cv2.imwrite("frame%d.jpg" %i, frame) #이름 변경, 저장할 공간 생각
    i+=1

#video.release() #비디오 끄는 것
#cv2.destroyAllWindows()

#비디오 프레임들 불러오기
images = glob.glob('*.jpg') #디렉토리

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_detecor = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

count = 0
for i in images:
    print(i)
    img = cv2.imread(i)
    img = cv2.resize(img, (600,600))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #faces = face_cascade.detectMultiScale(gray, 1.25, 6)
    faces = face_detecor(gray, 1)


    #for (x,y,w,h) in faces:
        #cropped = img[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]




    for face in faces:
        landmarks = predictor(gray, face)
        shape = face_utils.shape_to_np(landmarks)

        (x, y, w, h) = face_utils.rect_to_bb(face)
        crop_img = img[shape[1][1]:y+h+int(h/4)*2, shape[1][0]:shape[15][0]]
        #하관 crop이 잘 안되면 [8]을 [7]로 변경해보기
        crop_img = cv2.resize(crop_img, (600,600))

    cv2.imwrite("changed_frame %d.jpg" %count, crop_img)
    count += 1






