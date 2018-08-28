import cv2
import numpy as np

A = np.random.randn(10,10)
w,u,v_t = cv2.SVDecomp(A)
Rank = 5
w[Rank:,0] = 0
B = u @ np.diag(w[:,0]) @ v_t


print('Rnak before:',np.linalg.matrix_rank(A))
print('Rank after:',np.linalg.matrix_rank(B))
print('Norm before',cv2.norm(A))
print('Norm after',cv2.norm(B))