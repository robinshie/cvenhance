import cv2,random

image = cv2.imread('./imgs/Lena.jpg')

w,h = image.shape[1],image.shape[0]

def rand_pt(mult =1.):
    return (random.randrange(int(w*mult)),
    random.randrange(int(h*mult))
    )
cv2.circle(image,rand_pt(),40,[255,0,0])
cv2.circle(image,rand_pt(),5,[255,0,0])
cv2.circle(image,rand_pt(),5,[255,46,233])
cv2.circle(image,rand_pt(),5,[255,0,0],2,cv2.LINE_AA)

cv2.line(image,rand_pt(),rand_pt(),[233,3,3],3,cv2.LINE_AA)

cv2.arrowedLine(image,(0,0),(100,100),[233,3,3],3,cv2.LINE_AA)

cv2.ellipse(image,rand_pt(),rand_pt(0.3),random.randrange(360),0,360,(255,255,255),2)

cv2.putText(image,'Robin',rand_pt(),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(22,155,22),3)
cv2.rectangle(image,rand_pt(),rand_pt(),[255,46,233])
cv2.imshow('circle',image)
cv2.waitKey()
