import os #系统文件处理包
import uiautomator2 as u2 #android控制包
import pyautogui as pg
#FFtest SDK


location=pg.locateOnScreen(image=r'C:\Users\renyu.lou\Desktop\py\ff\TAP TO BEGIN.png') #判定目标截图在系统上的位置
print(location)#输出坐标

def loop_start(func):
    def dectory():
        func()
    return dectory()
        
#拉取log
class FFMandroidSmoke:
    
    # 结果统计
    def __init__(self):
        #异常处理统计
        self.pass_count = 0  # FreeFireMAXandroidSmoke+= 1
        self.failed_count = 0  # FreeFireMAXandroidSmoke+= 1

    # 登陆
    @loop_start
    def check_login(self):
        print("登陆成功")
        # 点击
        # 截图

    # 登出
    def check_logout(self):
        # 点击
        # 截图
        pass

    # 登陆动画
    def check_login_animation(self):
        # 点击
        # 截图
        pass

    # 大厅背景
    def check_lobby_background(self):
        # 点击
        # 截图
        pass

    # 签到
    def check_signin(self):
        # 点击
        # 截图
        pass

    # 小迅雷
    def check_ui_Thunder(self):
        # 点击
        # 截图
        pass

    # 充值
    def check_ui_Recharge(self):
        # 点击
        #截图
        #点击&切换tab
        pass

    # 幸运抽奖
    def check_ui_LuckyRoyal(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 角色系统
    def check_ui_character(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 仓库
    def check_ui_valut(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 宠物系统
    def check_ui_pet(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 藏品
    def check_ui_collection(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 武器库
    def check_ui_armory(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # season pass 季票
    def check_ui_ep(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 聊天
    def check_ui_chat(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # FF手册
    def check_ui_journal(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 排行榜
    def check_ui_leaderboard(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 好友
    def check_ui_friends(self):

        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 活动
    def check_ui_activity(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 每日/每周任务
    def check_ui_dailywork(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 公会
    def check_ui_guild(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 组队邀请
    def check_ui_team_invitation(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 排位赛
    def check_ui_rank(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 战备
    def check_ui_loadout(self):
        pass

    # 老兵回归
    def check_ui_veterans_return(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 电池
    def check_ui_battery(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    # 模式选择
    def check_ui_mode_selection(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

    #大厅武器展示
    def check_ui_weapon_display(self):
        # 点击
        # 截图
        # 点击&切换tab
        pass

