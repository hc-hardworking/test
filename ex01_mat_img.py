import numpy
import cv2
# 使用矩阵来创建图像
#构造器方式
img_1 = numpy.ndarray(shape=(500, 500, 3), dtype=numpy.uint8)
# 构造python数据列表，BGR
img_py = [[[255, 255, 20] for y in range(250)] for x in range(500)]    
# 工厂方式
img_2 = numpy.array(img_py)

# print(img_2[slice(0, 2, 1), 0, 1 ], img_2[0][0])
# print(img_2[0:2:1, 0, 1 ], img_2[0][0])
# print(img_1) 

img_1[0, 0, 0] = 255
img_1[0, 0, 1] = 255
img_1[0, 0, 2] = 255

cv2.imwrite("ex01_result01.png", img_1)
cv2.imwrite("ex01_result02.png", img_2)
# 加载图像

img_3 = cv2.imread("import01.jpg")

# img_3[:, :, 2] = 0
# img_3[:, :, 1] = 0

img_3[ img_3[:,:, 2] > 150] = 0

cv2.imwrite("ex01_result03.png", img_3)