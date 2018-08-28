import cv2,numpy as np
import matplotlib.pyplot as plt
import math

image = cv2.imread('./imgs/Lena.jpg',0).astype(np.float32) / 255

kernel =cv2.getGaborKernel((21,21),5,1,10,1,0,cv2.CV_32F)

kernel /= math.sqrt((kernel*kernel).sum())


filtered = cv2.filter2D(image,-1,kernel)


plt.figure(figsize=(8,3))

plt.subplot(131)

plt.axis('off')
plt.title("Image")
plt.imshow(image,cmap='gray')

plt.subplot(132)
plt.title("Kenel")
plt.imshow(kernel,cmap='gray')

plt.subplot(133)
plt.title("Filtered")
plt.imshow(filtered,cmap='gray')
plt.tight_layout()

plt.show()
'''
cv2.imshow('f',filtered)
cv2.waitKey()
cv2.destroyAllWindows()
'''


