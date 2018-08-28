import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

image = cv2.imread('../imgs/BnW.png',0)

_,contours,hierarchy = cv2.findContours(image,cv2.RETR_CCOMP,
cv2.CHAIN_APPROX_SIMPLE)

image_external = np.zeros(image.shape,image.dtype)

for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(image_external,contours,i,255,-1)

image_internel = np.zeros(image.shape,image.dtype)

for i in range(len(contours)):
    if hierarchy[0][i][3] != -1:
        cv2.drawContours(image_internel,contours,i,255,-1)

ax,(a1,a2,a3) = plt.subplots(1,3)
a1.imshow(image,cmap='gray')
a2.imshow(image_external,cmap='gray')
a3.imshow(image_internel,cmap='gray')
plt.show()

'''
array([[[ 1, -1, -1, -1],
        [-1,  0,  2, -1],
        [ 3, -1, -1,  1],
        [ 4,  2, -1,  1],
        [-1,  3, -1,  1]]], dtype=int32)

hierarchy[0]
Out[5]: 
array([[ 1, -1, -1, -1],
       [-1,  0,  2, -1],
       [ 3, -1, -1,  1],
       [ 4,  2, -1,  1],
       [-1,  3, -1,  1]], dtype=int32)

hierarchy[0][0]
Out[6]: array([ 1, -1, -1, -1], dtype=int32)

hierarchy[0][0][3]
Out[7]: -1
'''