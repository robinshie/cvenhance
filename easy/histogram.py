import cv2,numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./imgs/Lena.jpg',0)

cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()

image_eq = cv2.equalizeHist(image)
hist,bins = np.histogram(image_eq,256,[0,255])
plt.fill(hist)
plt.xlabel('pixel value')

plt.show()