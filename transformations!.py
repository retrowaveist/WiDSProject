import cv2
from PIL import Image


res = Image.open(r"C:\Users\mariy\Pictures\Screenshots\yeetus.png")



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
