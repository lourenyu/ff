import pyautogui as pg
import uiautomator2 as u2

screenWidth, screenHeight = pg.size() #获取当前屏幕分辨率
print(screenWidth, screenHeight)
# pg.moveTo(screenWidth / 2, screenHeight / 2,3) #移动鼠标到屏幕中间

pg.FAILSAFE = False #鼠标位置边界警告=关闭
currentMouseX, currentMouseY = pg.position() #获取当前鼠标位置
print(currentMouseX,currentMouseY)
# pg.moveTo(currentMouseX,currentMouseY,0) #移动鼠标到指定位置
# pg.PAUSE = 0.5 #全局pg函数延迟
pg.click(x=currentMouseX, y=currentMouseY, clicks=2, interval=0.0, button= "left", duration=0.0, tween=pg.linear)
im2 = pg.screenshot(r'.\Source_Pics\Result_Pics\首次截屏.png')