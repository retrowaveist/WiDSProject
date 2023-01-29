import numpy as np
import cv2
from matplotlib import pyplot as plt
#affine transformation
'''img = cv2.imread("C:\\Users\mariy\Pictures\Screenshots\\yeetus.png")
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()'''
#perspective transformation
img = cv2.imread("C:\\Users\mariy\Pictures\Screenshots\\Timage.png")
rows,cols,ch = img.shape

pts1 = np.float32([[189,268],[296, 275],[186,365],[289,373]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()