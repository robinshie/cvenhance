import cv2, numpy as np

image = np.full((480,540,3),255,np.int8)

cv2.imshow('white',image)

cv2.waitKey()
cv2.destroyAllWindows()

image = np.full((480,540,3),(0,0,255),np.uint8)

cv2.imshow('red',image)
cv2.waitKey()
cv2.destroyAllWindows()

image.fill(0)
cv2.imshow('black',image)
cv2.waitKey()
cv2.destroyAllWindows()

image[240,160] = image[240,320]=image[240,480] = (255,255,255)

cv2.imshow('black with white pixels',image)
cv2.waitKey()
cv2.destroyAllWindows()


image[:,:,0] = 255
cv2.imshow('blue with white pixels',image)
cv2.waitKey()
cv2.destroyAllWindows()


image[:,340,:] = 255
cv2.imshow('blue with white lines',image)
cv2.waitKey()
cv2.destroyAllWindows()

image[100:600,100:200,2] = 255
cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()
