import cv2
import  numpy as np

def detect_faces(vide_file,detector,win_title):
    cap = cv2.VideoCapture(vide_file)
    while True:
        status_cap,frame = cap.read()
        if not status_cap:
            break
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray,1.3,5)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
            text_size,_=cv2.getTextSize('Face',cv2.FONT_HERSHEY_SIMPLEX,1,2)
            cv2.rectangle(frame,(x,y-text_size[1]),(x+text_size[0],y),(255,255,255),cv2.FILLED)
            cv2.putText(frame,'Face',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
            cv2.imshow(win_title,frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


haar_face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

detect_faces('./imgs/faces.mp4',haar_face_cascade,"Haar cascade face detectior")


#lbq_face_cascade = cv2.CascadeClassifier()
#lbq_face_cascade.load('../data/lbpcascade_frontalface.xml')
#detect_faces('../imgs/faces.mp4',lbq_face_cascade,'LBP cascade face detector')