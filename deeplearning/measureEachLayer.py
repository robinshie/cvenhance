import cv2
import numpy as np

model = cv2.dnn.readNetFromCaffe("../data/bvlc_googlenet.prototxt",
'../data/bvlc_googlenet.caffemodel')

print('gflops:',model.getFLOPS((1,3,244,244))*1e-9)
w,b = model.getMemoryConsumption((1,3,224,224))

print('weights (mb):',w*1e-6,',blobs (mb)',b*1e-6)

blob = cv2.dnn.blobFromImage(np.zeros((224,224,3),np.uint8),1,(224,224))
model.setInput(blob)
model.forward()

total,timings =model.getPerfProfile()
tick2ms =1e3/cv2.getTickFrequency()
print('inference (ms):{:2f}'.format(total*tick2ms))

layer_names = model.getLayerNames()
print('{:<30}{}'.format('LAYER','TIME (ms)'))
for(i,t) in enumerate(timings):
    print('{:<30} {:.2f}'.format(layer_names[i],t[0]*tick2ms))