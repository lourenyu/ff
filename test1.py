import cv2
img = cv2.imread(r".\Source_Pics\Test_Pics\test_case.png",cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread(r".\Source_Pics\Test_Pics\test_case.png",cv2.IMREAD_COLOR)


print(img.shape)
print(img.size)
print(img.dtype)


