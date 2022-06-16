import os

#adb命令
def adb_command(command):
    return os.popen('adb ' + command).read()

#adb测试联通性
def adb_test():
    print(adb_command('devices'))


#ugc文件本地上传手机客端
def ugc_adb_pushmap(equi,file1_orign, file2_aim):
    os.system('adb -s %s pull "%s" %s' % (equi, file1_orign, file2_aim))


#ugc文件下载本地
def ugc_adb_pushmap(equi,file1_orign, file2_aim):
    os.system('adb -s %s push "%s" %s' % (equi, file1_orign, file2_aim))
    #adb -s emulator-5558 pull "/sdcard/Android/data/com.dts.freefireth/files/Workshop" C:/Users/renyu.lou/Desktop/ugc/tamplets


def main():

    try:
        while True:
            adb_test()
            print("1.adb测试联通性")
        equi = input('#示例\nemulator-5558 & NXTDU16B05011269 & 192.168.3.142:5555\n请输入设备名称：')
        file1_orign = input('请输入本地路径:\n#示例\n文件夹："/sdcard/Android/data/com.dts.freefireth/files/Workshop"\n文件：/sdcard/Android/data/com.dts.freefireth/files/Workshopxxxx\n')
        file2_aim = input('请输入目标路径:\n#示例\nC:/Users/renyu.lou/Desktop/ugc/tamplets\n')
        ugc_adb_pushmap(equi, file1_orign, file2_aim)
    except:
        print('error')
    finally:
        print('Done')
        pass


if __name__ == '__main__':
    main()

