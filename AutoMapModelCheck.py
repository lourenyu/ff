import time
from skimage.metrics import structural_similarity as ssim
import imutils
import cv2
# import argparse 解析器，后面用


# def timer(func):
# 	time_start = time.time()
# 	func()
# 	time_end = time.time()
# 	spent_time = time_end - time_start
# 	print("spent time:{}".format(spent_time))
#
#
# path_A = "Source_Pics/Test_Pics/shipyard1.png"
# path_B = "Source_Pics/Test_Pics/shipyard2.png"
#
# @timer
# def comapred_imgAB(path_A,path_B):
# 	imageA = cv2.imread("Source_Pics/Test_Pics/shipyard1.png")
# 	imageB = cv2.imread("Source_Pics/Test_Pics/shipyard2.png")
# 	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
# 	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
# 	(score, diff) = ssim(grayA, grayB, full=True)
# 	diff = (diff * 255).astype("uint8")
# 	thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# 	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 	cnts = imutils.grab_contours(cnts)
# 	for c in cnts:
# 		(x, y, w, h) = cv2.boundingRect(c)
# 		cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
# 		cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
# 	return imageA,imageB
#
# (imageA,imageB) = comapred_imgAB(path_A,path_B)



# 加载两个输入图像,注意要相同尺寸
imageA = cv2.imread("Source_Pics/Standard_pics/hanger.png")
imageB = cv2.imread("Source_Pics/Standard_pics/hanger1.png")
# LOD测试，（x,z,y ！= y）
imageA = cv2.imread("Source_Pics/Test_Pics/lodtest.png")
imageB = cv2.imread("Source_Pics/Test_Pics/lodtest1.png")
# 渲染，材质丢失测试
imageA = cv2.imread("Source_Pics/Test_Pics/shipyard1.png")
imageB = cv2.imread("Source_Pics/Test_Pics/shipyard2.png")
# 将图像转换为灰度
grayA = cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)
#计算两者之间的结构相似性指数 (SSIM)
#返回差异图像
(score,diff) = ssim(grayA,grayB,full = True)
diff = (diff *255).astype("uint8")
print("SSIM:{}".format(score))
#差异图像进行阈值处理，然后找到轮廓
#获取两个输入图像的不同区域
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# 遍历轮廓
for c in cnts:
	#计算轮廓的边界框，然后绘制
	#两个输入图像上的边界框来表示两个输入图像的位置
	#图像不同
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)


#输出结果
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
# cv2.imshow("Diff", diff)
# cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

#打印log

