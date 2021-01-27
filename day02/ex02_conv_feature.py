import numpy as np
import cv2

in_img=cv2.imread("0002.png")

#sobel一阶导数运算（任意阶导数）
# out_img=cv2.Sobel(in_img,-1,1,1,ksize=3,scale=1.0,delta=128,)

#laplace二阶导数运算
# out_img=cv2.Laplacian(in_img,-1,ksize=3,delta=0.0)

#高斯模糊运算
out_img=cv2.GaussianBlur(in_img,ksize=(11,11),sigmaX= 20)


#卷积运算 
# kernel=np.array([
#     [1,0,-1],
#     [1,0,-1],
#     [1,0,-1],
# ])
# out_img=cv2.filter2D(in_img,-1,kernel,delta=0.0)
cv2.imwrite("gauss.png",out_img)