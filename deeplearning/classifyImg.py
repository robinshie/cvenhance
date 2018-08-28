import cv2
import numpy as np

def classify(video_src,net ,in_layer,out_layer,meanval,category_names,swapchannels=False):
    cap = cv2.VideoCapture(video_src)
    t = 0
    while True:
        status_cap,frame = cap.read()
        if not status_cap:
            break
        if isinstance(meanval,np.ndarray):
            tensor = cv2.dnn.blobFromImage(frame,1.0,(224,224),1.0,False)

            tensor -= meanval
        else:
            tensor = cv2.dnn.blobFromImage(frame,1.0,(224,224),meanval,swapchannels)
            net.setInput(tensor,in_layer)
            prob = net.forward(out_layer)
            prob = prob.flatten()
            r=1
            for i in np.argsort(prob)[-5:]:
                txt = '"%s";probability: %.2f'%(category_names[i],prob[i])
                cv2.putText(frame,txt,(0,frame.shape[0]-r*40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                r += 1
                cv2.imshow('classifiction',frame)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()

with open('../data/synset_words.txt') as f:
    class_names = [' '.join(l.split(' ')[1:]).rstrip() for l in f.readlines()]
        

googlenet_caffe = cv2.dnn.readNetFromCaffe("../data/bvlc_googlenet.prototxt",
'../data/bvlc_googlenet.caffemodel')
classify('../data/traffic.mp4',googlenet_caffe,"data",'prob',(104,117,123),class_names)