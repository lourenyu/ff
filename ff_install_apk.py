#1
import os

#安装gp_obb
class AdbInstallGpApk():
    os.system("adb devices")  # 查验连接状态
    print("Parpare to install\n")
    print("------Installing------")
    os.system(r"adb -s emulator-5554 install -r C:\Users\renyu.lou\Desktop\signed_shell_FF_RCT_1.7.3574_114720_1366069_unity20180411_gp-release.apk")  # -r强制覆盖安装本地-s特定安装包
    print("Install Over")



#安装spilt_obb，内部嵌有obb和json的拉取方法
class AdbInstallSpiltApk():
    os.system("adb devices")  # 查验连接状态
    os.system("adb -s 设备编号 install  -r apk路径")  # -r强制覆盖安装本地-s特定安装包

    def adb_push_obb(self):
        obb_path = os.path.exists("ff_obb路径")  # 判断ff_obb是否存在
        if obb_path == True:
            os.system("adb shell rm ff_obb路径")
            os.system("adb push ff_obb路径 目标路径")  # 添加obb
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
class AdbPullDebuggerlog():
    os.system("adb devices")  # 查验连接状态
    debuggerlog_path = os.path.exists("debuggerlog路径")  # 判断ff_json是否存在
    if debuggerlog_path == True:
        os.system("adb pull log文件夹路径 目标路径")  # 存在则拉取
        print("已拉取至{}".format(debuggerlog_path))  # 找到提示
    else:
        os.system("未找到log")  # 未找到提示

#拉取json
class AdbPullJson():
    os.system("adb devices")  # 查验连接状态
    json_path = os.path.exists("json路径")  # 判断ff_json是否存在
    if json_path == True:
        os.system("adb pull json路径 目标路径")  # 存在则拉取
        print("已拉取至{}".format(json_path))  # 找到提示
    else:
        os.system("未找到json")  # 未找到提示



