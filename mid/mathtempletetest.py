import cv2
import numpy as np

img = cv2.imread('./imgs/Lena.jpg',cv2.IMREAD_COLOR)

show_img = np.copy(img)

mouse_pressed = False

x = y =w =h = 0

def mouse_callBack(event,_x,_y,flags,param):
    global show_img,x,y,w,h,mouse_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        x,y =_x,_y
        show_img = np.copy(img)
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            show_img = np.copy(img)
            cv2.rectangle(show_img,(x,y),(_x,_y),(0,255,0),3)
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        w,h = _x - x,_y - y
cv2.namedWindow('image')
cv2.setMouseCallback('image',mouse_callBack)

while True:
    cv2.imshow('image',show_img)
    k=cv2.waitKey(1) & 0xFF
    if (k == ord('a') and not mouse_pressed):
        if(w*h)>0:
            break
cv2.destroyAllWindows()

templete = np.copy(img[y:y+h,x:x+w])

methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','TM_CCORR_NORMED'
,'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

show_img = np.copy(img)

while True:
    cv2.imshow('image',show_img)
    k = cv2.waitKey() & 0XFF
    print(k)
    if k == 27:
        break
    elif k > 0 and chr(k).isdigit():
        index = int(chr(k))
        if 0<=index<len(methods):
            method = methods[index]
            res = cv2.matchTemplate(img,templete,eval(method))
            res = cv2.normalize(res, None,0,1,cv2.NORM_MINMAX)
            if index >= methods.index('cv2.TM_SQDIFF'):
                loc  = np.where(res<0.01)
            else:
                loc = np.where(res>0.99)
            show_img = np.copy(img)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(show_img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)
                res = cv2.resize(res,show_img.shape[:2])*255
                res = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR).astype(np.uint8)
                print(method)
                cv2.putText(res,method,(0,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
                show_img = np.hstack((show_img,res))

cv2.destroyWindow()
