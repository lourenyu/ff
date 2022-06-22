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
        # MousePosShow()
        #目标模拟器尺寸(920,550),分辨率(1600*900)
        #启动游戏
        pyg.click(392,140,1,duration=0.5)
        time.sleep(25)
        #登陆
        pyg.click(455,472,1,duration=0.5)
        time.sleep(10)
        #关闭弹窗
        pyg.click(787, 116, 1, duration=0.5)
        time.sleep(3)
        pyg.click(895, 52, 1, duration=0.5)
        time.sleep(3)
        pyg.click(863, 131, 1, duration=0.5)
        time.sleep(3)
        #点击匹配入口
        pyg.click(817, 464, 1, duration=0.5)
        time.sleep(3)
        #点击UGC入口
        pyg.click(818, 503, 1, duration=0.5)
        time.sleep(3)
          #关闭UGC introduction
        pyg.click(792, 94, 1, duration=0.5)
        time.sleep(3)
          #提前买够房卡，确认角色等级在lv8以上
        #点击UGC自定义模板tab
        pyg.click(55, 503, 1, duration=0.5)
        time.sleep(10)
        #点击选中模板
        #确认

        #关闭FF进程
        pyg.click(428, 19, 1, duration=0.5)
        time.sleep(3)






    except:
        pass
    finally:
        pass

if __name__ == '__main__':
    main()