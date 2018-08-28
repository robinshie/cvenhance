import cv2
import numpy as np
import matplotlib.pyplot as plt

c_image = np.zeros((500,500),np.uint8)
cv2.circle(c_image,(255,255),100,255,-1)

r_image = np.zeros((500,500),np.uint8)
cv2.rectangle(r_image,(100,100),(400,250),255,-1)

c_image_and_r_image = c_image & r_image

c_image_or_r_image = c_image | r_image

ax,((a1,a2),(a3,a4)) = plt.subplots(2,2)

a1.imshow(c_image)
a2.imshow(r_image)
a3.imshow(c_image_and_r_image)
a4.imshow(c_image_or_r_image)

plt.show()

