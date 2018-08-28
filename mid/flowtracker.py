import cv2
import numpy as np

cap = cv2.VideoCapture('./imgs/highway.mp4')

_,frame = cap.read()

#bbox = (287, 23, 86, 320)
bbox = cv2.selectROI(frame,False)

cv2.destroyAllWindows()

#tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
#tracker_type = tracker_types[0]
#tracker = cv2.Tracker_create(tracker_type)
tracker = cv2.TrackerMedianFlow_create()
status_tracker = tracker.init(frame,bbox)
fps = 0
while True:
    status_cap,frame = cap.read()
    if not status_cap:
        break
    if status_tracker:
        timer = cv2.getTickCount()
        status_tracker,bbox = tracker.update(frame)
        if status_tracker:
            x,y,w,h = [int(i) for i in bbox]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),15)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
            cv2.putText(frame,"FPS : %.0f" % fps,(0,80),cv2.FONT_HERSHEY_SIMPLEX,3.5,(0,0,0),8)
        else:
            cv2.putText(frame,"FPS : %.0f" % fps,(0,80),cv2.FONT_HERSHEY_SIMPLEX,3.5,(0,0,255),8)
        cv2.imshow('MedianFlow tracker',frame)
        k = cv2.waitKey(1) & 0XFF
        if k==27:
            break
cv2.destroyAllWindows()   