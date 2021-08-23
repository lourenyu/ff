import cv2

# img = cv2.imread("test1.jpg")  #导入图片
# cv2.namedWindow("Image")  #命名容器
# cv2.imshow("Image",img)
# cv2.waitKey(0)   #刷新时间
# cv2.destroyAllWindows()  #close

img = cv2.imread(r"test_case.png")

# #获取和设置
# pixel = img[100,100]  #[57 63 68],获取(100,100)处的像素值
# print(pixel)
# img[100,100]=[57,63,99] #设置像素值
# print(pixel)
# b = img[100,100,0]    #57, 获取(100,100)处，blue通道像素值
# print(b)
# g = img[100,100,1]    #63
# print(g)
# r = img[100,100,2]      #68
# print(r)
# r = img[100,100,2]=99    #设置red通道值
# print(r)
# #获取和设置
# piexl = img.item(100,100,2)
# img.itemset((100,100,2),99)
# print(pixel)
# print(img)
roi = img[100:300,200:400]
roi1 = roi[:,:,-2]
cv2.imshow("1",roi1)

cv2.waitKey()
cv2.destroyAllWindows()

