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

import cv2 as cv
img1 = cv.imread(r"test_case.png")
img = img1[0:426,43:400]
img2 = cv.imread(r"test_case2.png")
img3 = img2[0:426,43:400]

# blend = cv.addWeighted(img,0.5,img3,0.9,0)  #两张图的大小和通道也应该相同

cv.imshow("blend",img)
cv.waitKey()
cv.destroyAllWindows()