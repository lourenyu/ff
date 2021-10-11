import pyautogui as pg

location=pg.locateOnScreen(image=r'C:\Users\renyu.lou\Desktop\py\ff\TAP TO BEGIN.png') #判定目标截图在系统上的位置
print(location)#输出坐标

def loop_start_roomlobby(func):
    def dectory():
        func()
    return dectory()


class FFM_android_smoke_roomlobby:
    # 结果统计
    def __init__(self):
        # 异常处理统计
        self.pass_count = 0  # FreeFireMAXandroidSmoke+= 1
        self.failed_count = 0  # FreeFireMAXandroidSmoke+= 1