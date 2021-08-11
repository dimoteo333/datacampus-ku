def face_crop_vid (Clean_File_name):
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    File_name = './CUT_VID/' + Clean_File_name + '.mp4'
    video =  cv2.VideoCapture(File_name)

    fps = video.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (round(width), round(height))
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    
    cnt = 0
    
    
    out = cv2.VideoWriter('./FINAL_VID/%s.mp4' %Clean_File_name, fourcc, fps, size)

    while(video.isOpened()):
    
        ret, frame = video.read()
        
        cnt += 1
        
        if frame is None:
            break


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 
                                              scaleFactor=1.2, 
                                              minNeighbors=5, 
                                              minSize=(20,20))
        if ret == True:
            
            for (x, y, w, h) in faces:
                track_window = (x, y, w, h)
            
                x, y, w, h = track_window
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0, 0), 2)
                dst = np.zeros_like(frame)
                dst[y:y+h,x:x+w] = frame[y:y+h,x:x+w]
                
            xx = cnt * 100/frames


        out.write(dst)

    video.release()
    out.release()
    cv2.destroyAllWindows()
