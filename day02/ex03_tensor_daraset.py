import numpy
import cv2

import torchvision
import torch

# 1.加载数据集，导出图像
t2=torchvision.transforms.ToTensor()
t3=torchvision.transforms.Normalize((0.0,0.0,0.0),(1.0,1.0,1.0))
t1=torchvision.transforms.Compose([t2,t3])
mnist_train=torchvision.datasets.MNIST(root="./data",train=True,transform=t1,download=True)
mnist_valid=torchvision.datasets.MNIST(root="./data",train=False,transform=t1,download=True)
# 2.加载图像为张量，做卷积运算，结果再保存为图片

