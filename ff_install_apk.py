#1
import os

#安装gp_obb
class AdbInstallGpApk(object):
    def __init__(self):
        os.system("adb devices")  # 查验连接状态
        print("Parpare to install......\n")
        phone_id = input("请输入手机序列号：\n")
        gp_apk_file = input("请输入gp.apk绝对路径：\n")
        print("------Installing------")
        os.system("adb -s {} install -r {}".format(phone_id,gp_apk_file))  # -r强制覆盖安装本地-s特定安装包
        print("APK Install Over")

#安装spilt_obb，内部嵌有obb和json的拉取方法
class AdbInstallSpiltApk(object):
    def __init__(self):
        os.system("adb devices")  # 查验连接状态
        phone_id = input("请输入手机序列号：\n")
        Spilt_apk_file = input("请输入spilt.apk绝对路径\n")
        print("------Installing------")
        os.system("adb -s {} install  -r {}".format(phone_id,Spilt_apk_file))  # -r强制覆盖安装本地-s特定安装包
        print("APK Install Over")


    def adb_push_obb(self):
        obb_path = os.path.exists("com.dts.freefireth")  # 判断ff_obb是否存在
        if obb_path == True:
            os.system("adb shell rm com.dts.freefireth")
            ff_spilt_obb = input("请输入需要移动的obb绝对路径：\n")
            os.system("adb push {} 目标路径".format(ff_spilt_obb))  # 添加obb
        else:
            os.system("adb push ff_obb路径 目标路径")  # 添加obb

    def adb_push_json(self):
        json_path = os.path.exists("ff_json路径")  # 判断ff_json是否存在
        if json_path == True:
            os.system("adb shell rm ff_json路径")
            os.system("adb push ff_json路径 目标路径")  # 添加json
        else:
            os.system("adb push ff_json路径 目标路径")  # 添加json

#拉取log
class AdbPullDebuggerlog(object):
    def __init__(self):
        os.system("adb devices")  # 查验连接状态
        debuggerlog_path = os.path.exists("debuggerlog路径")  # 判断ff_json是否存在
        if debuggerlog_path == True:
            os.system("adb pull log文件夹路径 目标路径")  # 存在则拉取
            print("已拉取至{}".format(debuggerlog_path))  # 找到提示
        else:
            os.system("未找到log")  # 未找到提示

#拉取json
class AdbPullJson(object):
    def __init__(self):
        os.system("adb devices")  # 查验连接状态
        json_path = os.path.exists("json路径")  # 判断ff_json是否存在
        if json_path == True:
            os.system("adb pull json路径 目标路径")  # 存在则拉取
            print("已拉取至{}".format(json_path))  # 找到提示
        else:
            os.system("未找到json")  # 未找到提示

