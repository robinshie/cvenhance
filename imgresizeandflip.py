import cv2 
import matplotlib.pyplot as plt
import os,sys
img = cv2.imread('./imgs/Lena.jpg')

print("Oraginal image shape: ",img.shape)

width,height = 128,255

resize_img = cv2.resize(img,(width,height))

print("resized image result is:",resize_img.shape)

w_mult,h_mult =0.25,0.5
resize_img = cv2.resize(img,(0,0),resize_img,w_mult,h_mult)

print("imge shape:",resize_img.shape)

img_flip_along_x= cv2.flip(img,0)
img_flip_along_y= cv2.flip(img,1)
img_flip_along_xy = cv2.flip(img,-1)
cv2.imshow("f",img_flip_along_xy)
cv2.waitKey()