import time
<<<<<<< HEAD
import pyautogui
import xlrd
import cv2
import pyperclip

# # while True:
# #     a = pyautogui.position()
# #     print(a)
# #     time.sleep(1)
#
# # b = pyautogui.size()
# # print(b)
#
# c = pyautogui.onScreen(4000,1000)
# print(c)
#
# # pyautogui.moveTo(1500,1000,duration=2)
# #
# # #相对于当前位置移动鼠标
# # pyautogui.moveRel(100,-100,duration=2)
#
# # pyautogui.click()#当前位置单击
# # pyautogui.click(x=714,y=454,clicks=1,interval=1,button='left')
# #interval 单击之间等待的秒数
# #doubleClick() 执行鼠标双击
# #right/left/middle/Click() 右击/左击/中间单击
#
# #左键拖动
# pyautogui.dragTo(x,y,button='left')
#
# pyautogui.mouseUp()
# pyautogui.mouseDown()
#
# #mouseDown()/mouseUp() 鼠标按下/释放，可进行鼠标拖动
#
#
# pyautogui.scroll(10) #向上滚动10格
# pyautogui.scroll(-10) #向下，，，
# pyautogui.scrolll(10,x=10,y=100) # 将鼠标移到x,y,在向上滚动10格
# # OS X和Linux平台上，可以通过和scroll()执行水平滚动

time.sleep(3)
pyautogui.write('hello world',interval=1) # 打印书hellow world 每个字符后延迟0.25秒
pyautogui.alert(text='hello',title='world',button='OK') # 显示一个带有文本和确定按钮的简单消息框，用户点击返回button的文本
pyautogui.confirm(text='',title='',buttons=['OK','Cancel']) #显示带有确定和取消按钮的消息框，可以自定义按钮的数量和文本，点击返回按钮的文本
=======

import pyautogui as pyg

def MousePosShow():
    """
    mouse_pos = 鼠标位置
    :return:
    """
    while True:
        mouse_pos = pyg.position()
        print(mouse_pos)
        time.sleep(0.5)

def main():
    try:
        MousePosShow()
        #目标模拟器尺寸(920,550),分辨率(1600*900)
        #启动游戏
        #登陆
        #点击匹配入口
        #点击UGC入口
          #关闭UGC introduction
          #提前买够房卡，确认角色等级在lv8以上
        #点击UGC自定义模板tab
        #点击模板



    except:
        pass
    finally:
        pass



if __name__ == '__main__':
    main()
>>>>>>> 5c9b77e08b4d359b51c3d5083b7caafaee16f029
