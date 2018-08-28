import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((480,640),np.uint8)

cv2.ellipse(image,(320,240),(200,100),0,0,360,255,-1)

m = cv2.moments(image)

for name,val in m.items():
    print(name,'\t',val)

print('center x estimated',m['m10']/ m['m00'])
print('center y estimated',m['m01']/m[ 'm00'])
#cv2.imshow(image)
#cv2.waitKey()
#cv2.destroyAllWindows() 

