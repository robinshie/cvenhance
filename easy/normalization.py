import cv2,numpy as np

image = cv2.imread('./imgs/Lena.jpg',0).astype(np.float32) / 255

cv2.imshow('image',image)

image -= image.mean()

cv2.imshow('image',image)
image /= image.std()

cv2.imshow('image',image)

cv2.waitKey()
cv2.destroyAllWindows()