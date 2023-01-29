import cv2
from PIL import Image
'''import numpy as np

import torch
import matplotlib.pyplot as plt


img= cv2.imread('C:\\Users\mariy\Pictures\Screenshots\\yeetus.png')'''
res = Image.open(r"C:\Users\mariy\Pictures\Screenshots\yeetus.png")
'''res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('ogimg', res)

y=60
x=42
h=900
w=510
crop_image = res[x:w, y:h]'''


right = 100
left = 100
top = 100
bottom = 100

width, height = res.size

new_width = width + right + left
new_height = height + top + bottom

result = Image.new(res.mode, (new_width, new_height), (50, 0, 100))

result.paste(res, (left, top))

result.save('output.png')
result.show()
res.close()
'''
cv2.imshow("Cropped", crop_image)
cv2.waitKey(0)

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()'''