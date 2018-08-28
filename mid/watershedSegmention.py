import cv2,random
import numpy as np
from random import randint

img = cv2.imread('./imgs/Lena.jpg')
show_img=np.copy(img)

seeds =np.full(img.shape[0:2],0,np.int32)
segmentation = np.full(img.shape,0,np.uint8)

n_seeds = 9

colors = []

for m in range(n_seeds):
    colors.append((255*m/n_seeds,randint(0,255)))
mouse_pressed = False
current_seed = 1
seeds_updated = False

def mouse_callback(event,x,y,flags,param):
    global mouse_pressed,seeds_updated

    