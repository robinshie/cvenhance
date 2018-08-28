'''
import cv2

import sys

 

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if __name__ == '__main__' :

 

    # Set up tracker.

    # Instead of MIL, you can also use

 

    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']

    tracker_type = tracker_types[4]

 

    if int(minor_ver) < 3:

        tracker = cv2.Tracker_create(tracker_type)

    else:

        if tracker_type == 'BOOSTING':

            tracker = cv2.TrackerBoosting_create()

        if tracker_type == 'MIL':

            tracker = cv2.TrackerMIL_create()

        if tracker_type == 'KCF':

            tracker = cv2.TrackerKCF_create()

        if tracker_type == 'TLD':

            tracker = cv2.TrackerTLD_create()

        if tracker_type == 'MEDIANFLOW':

            tracker = cv2.TrackerMedianFlow_create()

        if tracker_type == 'GOTURN':

            tracker = cv2.TrackerGOTURN_create()

 

    # Read video

    video = cv2.VideoCapture('./imgs/highway.mp4')
    if not video.isOpened():

        print ("Could not open video")

        sys.exit()

 

    # Read first frame.

    ok, frame = video.read()

    if not ok:

        print ('Cannot read video file')

        sys.exit()

    

    # Define an initial bounding box

    bbox = (287, 23, 86, 320)

 

    # Uncomment the line below to select a different bounding box

    bbox = cv2.selectROI(frame, False)

 

    # Initialize tracker with first frame and bounding box

    ok = tracker.init(frame, bbox)

 

    while True:

        # Read a new frame

        ok, frame = video.read()

        if not ok:

            break

        

        # Start timer

        timer = cv2.getTickCount()

 

        # Update tracker

        ok, bbox = tracker.update(frame)

 

        # Calculate Frames per second (FPS)

        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

 

        # Draw bounding box

        if ok:

            # Tracking success

            p1 = (int(bbox[0]), int(bbox[1]))

            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

        else :

            # Tracking failure

            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

 

        # Display tracker type on frame

        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)

    

        # Display FPS on frame

        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)

 

        # Display result

        cv2.imshow("Tracking", frame)

 

        # Exit if ESC pressed

        k = cv2.waitKey(1) & 0xff

        if k == 27 : break

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


haar_face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')

#detect_faces('../imgs/faces.mp4',haar_face_cascade,"Haar cascade face detectior")


lbq_face_cascade = cv2.CascadeClassifier()
lbq_face_cascade.load('../data/lbpcascade_frontalface.xml')
detect_faces('../imgs/faces.mp4',lbq_face_cascade,'LBP cascade face detector')
'''

import cv2
import  time


#cap = cv2.VideoCapture(0)
#time.sleep(2)
haar_face_cascade = cv2.CascadeClassifier('../data/haarcascade_frontalface_default.xml')
img =cv2.imread('../imgs/people.jpg')
faces = haar_face_cascade.detectMultiScale(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
cv2.imshow("p", img)

'''
while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_face_cascade.detectMultiScale(gray, 1.3, 5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.imshow("p",frame)

    k = cv2.waitKey(1)

    if k == 27:
        break
cap.release()
'''
cv2.waitKey()
cv2.destroyAllWindows()
