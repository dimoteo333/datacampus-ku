# import libraries
import cv2
import face_recognition

# Get a reference to webcam 
video_capture = cv2.VideoCapture("video.mp4")

# Initialize variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        # crop the face
        cropped = frame[top - int((bottom-top)/4):top + (bottom-top) + int((bottom-top)/4), left - int((right-left)/4):left + (right-left) + int((right-left)/4)]

    # Display the resulting image
    cv2.imshow('Video', cropped)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()