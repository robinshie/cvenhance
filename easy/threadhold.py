import cv2,numpy as np
import matplotlib.pyplot as plt
import math

image = cv2.imread('./imgs/Lena.jpg',0)

thr,mask = cv2.threshold(image,200,1,cv2.THRESH_BINARY)

print('Threshold used',thr)

adapt_mask = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY_INV,11,10
)

ax,((p1,p2,p3))  = plt.subplots(1,3)
p1.imshow(image,cmap='gray')
p2.imshow(mask,cmap='gray')
p3.imshow(adapt_mask,cmap='gray')
plt.show()