import cv2
import glob

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

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count = 0
for i in images:
    print(i)
    img = cv2.imread(i)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3,5)
    for (x,y,w,h) in faces:
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
        cropped = img[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    cv2.imwrite("changed_frame%d.jpg" %count, cropped) #얼굴만 잘린 사진들
    count += 1






