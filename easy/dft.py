import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('./imgs/Lena.jpg',0).astype(np.float32) / 255

fft = cv2.dft(image,flags=cv2.DFT_COMPLEX_OUTPUT)
fft = fft-np.mean(fft)
#VISUALIZE IMAGE

shifted = np.fft.fftshift(fft,axes=[0,1])

magnitude = cv2.magnitude(shifted[:,:,0],shifted[:,:,1])
restored = cv2.idft(fft,flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
plt.axis('off')
plt.imshow(restored,cmap='gray')
plt.tight_layout()
plt.show()



print(magnitude)