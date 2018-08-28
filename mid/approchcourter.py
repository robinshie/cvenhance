import cv2,random
import numpy as np

img = cv2.imread('./imgs/bw.png',cv2.IMREAD_GRAYSCALE)

color = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

img2,contours,hierachy =cv2.findContours(img,cv2.RETR_TREE,
cv2.CHAIN_APPROX_SIMPLE)

'''
cv2.drawContours(color,contours,-1,(0,255,0),3)

print(contours[0])
contour = contours[0]

print('Area of contour is %.2f'%cv2.contourArea(contour))
print('Signed area of contour is %.2f'%cv2.contourArea(contour,True))
print('Signed area of contour is %.2f'%cv2.contourArea(contour[::-1],True))


print('Length of closed contour is %.2f'%cv2.arcLength(contour,True))
print('Length of open contour is %.2f'%cv2.arcLength(contour,False))

hull = cv2.convexHull(contour)
cv2.drawContours(color,[hull],-1,(0,0,255),3)

cv2.imshow('a',color)
cv2.waitKey()
cv2.destroyAllWindows()

print('Convex status of contour is %s'%cv2.isContourConvex(contour))
print('Convex status of hull is %s'%cv2.isContourConvex(hull))
'''

cv2.namedWindow('contours')

img = np.copy(color)

def trakbar_callback(value):
    global img
    epsilon = value * cv2.arcLength(contours[0],True)*0.1/255
    approx = cv2.approxPolyDP(contours[0],epsilon,True)
    img = np.copy(color)
    cv2.drawContours(img,[approx],-1,(255,0,255),3)
cv2.createTrackbar('Epsilon','contours',1,255,lambda v:trakbar_callback(v))
while True:
    cv2.imshow('contours',img)
    key = cv2.waitKey(3)
    if key == 27:
        break
cv2.destroyAllWindows()