import os
import uiautomator2 as u2
import time

from ff_install_apk import *

#主流程运行计时
t1 = time.time()
print("计算过程")

# order = u2.connect('RFCNA0FJPXY') #链接手机&模拟器
#安装包
# order(text="Free Fire").click() #打开应用Free Fire
# order(text="Free Fire MAX").click() #打开应用Free Fire MAX
# order.click(0.685, 0.651)#判断--权限说明
# order.click(0.488, 0.671)#判断--照片访问d.click(0.488, 0.671)
#garena logo
#loding
#登陆页面
# order.click(0.445, 0.889) #游客登陆
# order.click(0.497, 0.848) #TAP TO BEGIN
#弹窗-WHATS NEW
#弹窗-活动-回归老兵
#弹窗-活动-日常任务
#弹窗-活动-充值LEVEL UP PASS
#order.click(0.871, 0.198) #BOOYAH DAY

# @loop_start
#流程

#主流程运行计时结束
t2 = time.time()
print(t2 - t1)