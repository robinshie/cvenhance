import cv2,numpy as np

image = cv2.imread('./imgs/Lena.jpg',0).astype(np.float32) / 255

gamma = 0.5
corrected_image = np.power(image,gamma)

cv2.imshow("image",image)
cv2.imshow("gamma image",corrected_image)

cv2.waitKey()
cv2.destroyAllWindows()