import cv2
img = cv2.imread(r"./Source_Pics/Test_Pics/test_case.png")
cv2.imshow('orgin1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape) #读（高height，宽length，通道数）
print(img.size) #读取大小 height*length*通道数
print(img.dtype) #图片类型


