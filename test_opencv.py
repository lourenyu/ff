import cv2

img = cv2.imread("test1.jpg")  #导入图片
cv2.namedWindow("Image")  #命名容器
cv2.imshow("Image",img)
cv2.waitKey(0)   #刷新率
cv2.destroyAllWindows()  #close