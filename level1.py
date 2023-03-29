import cv2 as cv
import random
from solve import *

# Level 1: Vẽ từ 5~10 hình tròn với các màu ngẫu nhiên lên ảnh ở các vị trí ngẫu nhiên

img = cv.imread('Photos/park.jpg')
height, width = img.shape[:2]
new_img = img.copy()

# Vẽ từ 5~10 hình tròn
for x in range(random.randint(5,10)):
    w = random.randint(25, width - 25)
    h = random.randint(25, height - 25)
    b, g, r = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    cv.circle(new_img, (w,h), 25, (b, g, r), -1)

# Show 2 ảnh trước và sau khi vẽ thêm hình tròn
cv.imshow('Img', img)
cv.imshow('New Img',new_img)

# Hàm giải import từ file solve.py
find_differences(img, new_img)

cv.waitKey(0)