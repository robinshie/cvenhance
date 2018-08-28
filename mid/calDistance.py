import cv2
import numpy as np
import matplotlib.pyplot as plt

image =np.full((480,640),255,np.uint8)
cv2.circle(image,(320,240),100,0)

distmap =cv2.distanceTransform(image,cv2.DIST_L2,cv2.DIST_MASK_PRECISE)

plt.figure()

plt.imshow(distmap,cmap='gray')

plt.show()