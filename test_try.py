#coding:utf-8
# import cv2 as cv
# import matplotlib.pyplot as plt
#
# img2 = cv.imread(r"test_case.png")
# img = cv.cvtColor(img2,cv.COLOR_BGR2RGB)  #matplotlib的图像为RGB格式
# constant = cv.copyMakeBorder(img,20,20,20,20,cv.BORDER_CONSTANT,value=[0,255,0]) #绿色
# reflect = cv.copyMakeBorder(img,20,20,20,20,cv.BORDER_REFLECT)
# reflect01 = cv.copyMakeBorder(img,20,20,20,20,cv.BORDER_REFLECT_101)
# replicate = cv.copyMakeBorder(img,20,20,20,20,cv.BORDER_REPLICATE)
# wrap = cv.copyMakeBorder(img,20,20,20,20,cv.BORDER_WRAP)
# titles = ["constant","reflect","reflect01","replicate","wrap"]
# images = [constant,reflect,reflect01,replicate,wrap]
#
# for i in range(5):
#     plt.subplot(2,3,i+1),plt.imshow(images[i]),plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()


# import cv2 as cv
# import numpy as np
# img1 = cv.imread("test_case.png",2)
# roi_img  = np.zeros(img1.shape[0:2],dtype=np.uint8)
# print(img1.shape[0:2])
# cv.imshow("roi_img0",roi_img)
# roi_img[100:280,400:550]=255
# img_add = cv.add(img1,img1)
# img_add_mask = cv.add(img1,img1,mask=roi_img)
# cv.imshow("img1",img1)
# cv.imshow("roi_img",roi_img)
# cv.imshow("img_add",img_add)
# cv.imshow("img_add_mask",img_add_mask)
# cv.waitKey(0)
# cv.destroyAllWindows()

# import cv2 as cv
# img1 = cv.imread(r"test_case.png")
# img = img1[0:426,43:400]
# img2 = cv.imread(r"test_case2.png")
# img3 = img2[0:426,43:400]
# blend = cv.addWeighted(img,0.5,img3,0.5,0)  #两张图的大小和通道也应该相同
# cv.imshow("blend",blend)
# cv.waitKey()
# cv.destroyAllWindows()


import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread(r"test_case.png")
# img = img1[0:426,43:400]
rows,cols = img1.shape[0:2]
img2 = cv.imread(r"test_case2.png")
# img = img1[0:426,43:400]
roi = img2[0:rows,0:cols]
img1_gray = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)

ret,img1_thres = cv.threshold(img1_gray,200,255,cv.THRESH_BINARY_INV)
img1_fg =cv.add(img1,img1,mask=img1_thres)    #拿到logo图案的前景

img1_thres_inv = cv.bitwise_not(img1_thres)
roi_bg = cv.add(roi,roi,mask=img1_thres_inv)  #拿到roi图案的背景

img_add = cv.add(img1_fg,roi_bg)     #背景和前景相加
img2[0:rows,0:cols] = img_add

cv.imshow("gray",img1_gray)
cv.imshow("thres",img1_thres)
cv.imshow("fg",img1_fg)
cv.imshow("tinv",img1_thres_inv)
cv.imshow("roi_bg",roi_bg)
cv.imshow("img_add",img_add)
cv.imshow("img2",img2)
cv.waitKey(0)
cv.destroyAllWindows()