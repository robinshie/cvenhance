import cv2
import numpy as np

image = cv2.imread('./data/Lena.png',cv2.IMREAD_COLOR)
tensor = cv2.dnn.blobFromImages([image,image],10.0,(224,224),
(104,117.123),False,True,)

net = cv2.dnn.readNetFromCaffe("./data/bvlc_googlenet.prototxt",
'./data/bvlc_googlenet.caffemodel')

net.setInput(tensor)
prob = net.forward()
print(prob)
net.setInput(tensor,'data')
prob = net.forward('prob')

print(prob)