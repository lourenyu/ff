#coding:utf-8

# cv2.imread()
# imread(img_path,flag) 读取图片，返回图片对象
#     img_path: 图片的路径，即使路径错误也不会报错，但打印返回的图片对象为None
#     flag：cv2.IMREAD_COLOR，读取彩色图片，图片透明性会被忽略，为默认参数，也可以传入1
#           cv2.IMREAD_GRAYSCALE,按灰度模式读取图像，也可以传入0
#           cv2.IMREAD_UNCHANGED,读取图像，包括其alpha通道，也可以传入-1

# cv2.imshow()
# imshow(window_name,img)：显示图片，窗口自适应图片大小
#     window_name: 指定窗口的名字
#     img：显示的图片对象
#     可以指定多个窗口名称，显示多个图片

# waitKey(millseconds)  键盘绑定事件，阻塞监听键盘按键，返回一个数字（不同按键对应的数字不同）
#     millseconds: 传入时间毫秒数，在该时间内等待键盘事件；传入0时，会一直等待键盘事件

# destroyAllWindows(window_name)
#     window_name: 需要关闭的窗口名字，不传入时关闭所有窗口

# cv2.imwrite()
# imwrite(img_path_name,img)
#     img_path_name:保存的文件名
#     img：文件对象



import cv2
img = cv2.imread(r"../Source_Pics/Test_Pics/LOG_IN_BG.png")  #读取图片
print(img.shape) #打印height,length，通道数
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #rgb转码bgr
ret,img_threshold = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)  #图像二值化（0~255）
cv2.imshow("img",img) #输出图片img，命名img
cv2.imshow("thre",img_threshold) #输出图片img_threshold，命名thre
key = cv2.waitKey(0) #图片停留时间，1=1ms，0=forever
if key==27: #按esc键时，关闭所有窗口
    print(key)
    cv2.destroyAllWindows()
cv2.imwrite(r"..\Source_Pics\Test_Pics\1.png",img_threshold) #保存图片img_threshold到此路径

