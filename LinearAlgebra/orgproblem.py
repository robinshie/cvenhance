import numpy as np
import  cv2
pts = np.random.multivariate_normal([150,300],[[1024,512],[512,1024]],50)
rmat =cv2.getRotationMatrix2D((0,0),30,1)[:,:2]
repts = np.matmul(pts,rmat.transpose())
repts_noise = repts + np.random.multivariate_normal([0,0],[[200,0],[0,200]],len(pts))
M = np.matmul(pts.transpose(),repts_noise)

sigma,u,v_t=cv2.SVDecomp(M)
rmat_est =np.matmul(v_t,u).transpose()


res,rmat_inv = cv2.invert(rmat_est)
assert res != 0

pts_est = np.matmul(repts,rmat_inv.transpose())

rpts_err = cv2.norm(rpts,repts_noise,cv2.NORM_L2)

rmat_err = cv2.norm(rmat,rmat_est,cv2.NORM_L2)

def draw_pts(image,points,color,thickness=cv2.FILLED):
    for pt in points:
        cv2.circle(image,tuple([int(x) for x in pt]),10,color,thickness)
img = np.zeros([512,512,3])
draw_pts(img,pts,(0,255,0))
