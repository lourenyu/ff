import cv2
img = cv2.imread(r".\Source_Pics\Test_Pics\test_case.png",cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread(r".\Source_Pics\Test_Pics\test_case.png",cv2.IMREAD_COLOR)


<<<<<<< HEAD:test_pyautogui.py
# img1 = cv2.imread('ceshi.jpg') #读取图像
# cv2.imshow('原始图像', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
=======
print(img.shape)
print(img.size)
print(img.dtype)


>>>>>>> 9bb3cc9ab37045bce5f5a7aed0b65eede7a64f58:test1.py
