import numpy
import cv2
# print("-------------python")

#使用矩阵
img_1=numpy.ndarray(shape=(500,500,3),dtype=numpy.uint8)
img_py=[[[255,255,0]for y in range(250)]for x in range(500)] #BGR？RGB
img_2=numpy.array(img_py)
img_1[0,0,0]=0
img_1[0,0,1]=255
img_1[0,0,2]=0
# print("--------------")
# print(img_2[0,0])
# print("--------------")
# cv2.imwrite("1.png",img_1)
# cv2.imwrite("2.png",img_2)
cv2.imwrite("1.png",img_1)
cv2.imwrite("2.png",img_1)
# 加载图像
img_3=cv2.imread("0002.png")
# img_3[:,:,1]=0
# img_3[:,:,1]=0
img_3[img_3[:,:,0]>100]=0 
img_3=cv2.imwrite("3.png",img_3)