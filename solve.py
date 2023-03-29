import cv2 as cv

# Hàm xét xem 2 pixel có khác nhau không
def not_equal(pixel1, pixel2):
    return pixel1[0] != pixel2[0] or pixel1[1] != pixel2[1] or pixel1[2] != pixel2[2]

# Tìm tâm của các vòng tròn đã vẽ, rồi khoanh lại
def find_differences(img, new_img):
    points = []
    for x in range(25, img.shape[0]-25):
        for y in range(25, img.shape[1]-25):
            if not_equal(img[x+25][y], new_img[x+25][y]) and not_equal(img[x][y+25], new_img[x][y+25]) and not_equal(img[x-25][y], new_img[x-25][y]) and not_equal(img[x][y-25], new_img[x][y-25]):
                points.append([x,y])
    for i in range(len(points)):
        print(points[i])
        cv.circle(new_img, (points[i][1],points[i][0]), 50, (0,0,255), 1)
    cv.imshow('Solved', new_img)

