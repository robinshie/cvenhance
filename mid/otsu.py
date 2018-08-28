'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./imgs/Lena.jpg',0)

otsu_thr,otsu_mask = cv2.threshold(image,-1,1,cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(otsu_thr)

ax,(a1,a2) = plt.subplots(1,2)

a1.imshow(image,cmap='gray')
a2.imshow(otsu_mask,cmap='gray')
plt.show()
'''