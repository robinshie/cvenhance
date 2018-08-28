import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img = np.full((512,512,3),255,np.uint8)

axes = (int(256*random.uniform(0,1)),int(356*random.uniform(0,1)))

angle = int(180*random.uniform(0,1))

center = (256,256)

pts = cv2.ellipse2Poly(center,axes,angle,0,360,1)

pts += np.random.uniform(-10,10,pts.shape).astype(np.int32)


cv2.ellipse(img,center,axes,angle,0,360,(0,255,0),3)
'''
for pt in pts:
    cv2.circle(img,center,int(pt[0]),int(pt[1]),3)
'''
ellipse = cv2.fitEllipse(pts)
cv2.ellipse(img,ellipse,(0,0,0),3)

img = np.full((512,512,3),255,np.uint8)

pts = np.arange(512).reshape(-1,1)
pts = np.hstack((pts,pts))
pts += np.random.uniform(-10,10,pts.shape).astype(np.int32)
cv2.line(img,(0,0),(512,512),(0,255,0),3)

for pt in pts:
    cv2.circle(img,(int(pt[0]),int(pt[1])),3,(0,255,255))


vx,vy,x,y = cv2.fitLine(pts,cv2.DIST_L2,0,0.01,0.01)

yo = int(y- x*vy/vx)
y1 = int((512-x)*vy/vx +y)

cv2.line(img,(0,yo),(512,y1),(0,0,0),3)

cv2.imshow('Fit line',img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('Fit line',img)
cv2.waitKey()
cv2.destroyAllWindows()