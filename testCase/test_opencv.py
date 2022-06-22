import time

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