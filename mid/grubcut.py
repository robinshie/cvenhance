import cv2
import numpy as np

img = cv2.imread('./imgs/Lena.jpg',cv2.IMREAD_COLOR)

show_img = np.copy(img)

mose_pressed = False

y=x=w=h=0
'''
def mose_callBack(event,_x,_y,flags,param):
    global show_img,x,y,w,h,mose_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        mose_pressed = True
        x,y =_x,_y
        show_img = np.copy(img)
    elif event == cv2.EVENT_MOUSEMOVE:
        if mose_pressed:
            show_img = np.copy(img)
            cv2.rectangle(show_img,(x,y),(_x,_y),(0,255,0),3)
    elif event == cv2.EVENT_LBUTTONUP:
        mose_pressed = False
        w,h = _x - x,_y - y

cv2.namedWindow('image')

cv2.setMouseCallback('image',mose_callBack)

while True:
    cv2.imshow('image',show_img)
    if (cv2.waitKey(1) & 0xFF == ord('a') and not mose_pressed):
        if w*h > 0:
            break
cv2.destroyAllWindows()

labels = np.zeros(img.shape[:2],np.uint8)
labels,bgdModel,fgModel = cv2.grabCut(img,labels,(x,y,w,h),
None,None,5,cv2.GC_INIT_WITH_RECT)
show_img = np.copy(img)

show_img[(labels == cv2.GC_PR_BGD) | (labels == cv2.GC_BGD)] //= 3

cv2.imshow('image',show_img)
cv2.waitKey()
cv2.destroyAllWindows()
'''
label = cv2.GC_BGD
lbl_clrs = {cv2.GC_BGD:(0,0,0),cv2.GC_FGD:(255,255,255)}
def mouse_callBack(event,x,y,flags,param):
    global mose_pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        mose_pressed = True
        cv2.circle(labels,(x,y),5,label,cv2.FILLED)
        cv2.circle(show_img,(x,y),5,lbl_clrs[label],cv2.FILLED)
    elif event == cv2.EVENT_MOUSEMOVE:
        if mose_pressed:
            cv2.circle(labels,(x,y),5,label,cv2.FILLED)
            cv2.circle(show_img,(x,y),5,lbl_clrs[label],cv2.FILLED)
    elif event == cv2.EVENT_LBUTTONUP:
        mose_pressed = False

cv2.namedWindow('image')

cv2.setMouseCallback('image',mouse_callBack)
bgdModel,fgModel = None,None
labels = np.zeros(img.shape[:2],np.uint8)
while True:
    cv2.imshow('image',show_img)
    k = cv2.waitKey(1) & 0xFF 
    if (k == ord('a') and not mose_pressed):
            break
    elif k == ord('1'):
        label = cv2.GC_FGD - label

cv2.destroyAllWindows()
labels,bgdModel,fgModel = cv2.grabCut(img,labels,None,bgdModel,fgModel,5,cv2.GC_INIT_WITH_MASK)
show_img = np.copy(img)

show_img[(labels == cv2.GC_PR_BGD) | (labels == cv2.GC_BGD)] //= 3

cv2.imshow('image',show_img)
cv2.waitKey()
cv2.destroyAllWindows()