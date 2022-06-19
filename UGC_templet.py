import os

#adb命令
def adb_command(command):
    """
    adb指令封装
    :param command: 具体命令
    :return: 完整的adb命令
    """
    return os.popen('adb ' + command).read()

#adb测试联通性
def adb_test():
    print(adb_command('devices'))

#ugc文件本地上传手机客端
def ugc_adb_pushmap(equi,file1_orign, file2_aim):
    '''
    本地ugc模板上传到手机
    :param equi: 设备编号
    :param file1_orign: 本机模板路径
    :param file2_aim: 手机路径
    :return:
    '''
    os.system('adb -s %s pull "%s" %s' % (equi, file1_orign, file2_aim))

#ugc文件下载本地
def ugc_adb_pullmap(equi,file1_orign, file2_aim):
    '''
    手机ugc模板拉取到本地模板库
    :param equi: 设备编号
    :param file1_orign: 本机模板路径
    :param file2_aim: 手机模板路径
    :return:
    '''
    os.system('adb -s %s push "%s" %s' % (equi, file1_orign, file2_aim))
    #adb -s emulator-5558 pull "/sdcard/Android/data/com.dts.freefireth/files/Workshop" C:/Users/renyu.lou/Desktop/ugc/tamplets


def main():
    try:
        #持续获取设备列表
        while True:
            adb_test()
            print("adb测试联通性")
            #有设备则length必定>4
            if len(adb_test()) >4:
                break
        equip = input('#示例\nemulator-5558 & NXTDU16B05011269 & 192.168.3.142:5555\n请输入设备名称：')
        print('--------------------------------------------------------------------')
        file1_orign = input('#示例\n文件夹："/sdcard/Android/data/com.dts.freefireth/files/Workshop"\n文件：/sdcard/Android/data/com.dts.freefireth/files/Workshopxxxx\n请输入本地路径:')
        print('----------------------------------------------------------------------------------')
        file2_aim = input('#示例\nC:/Users/renyu.lou/Desktop/ugc/tamplets\n请输入目标路径:')
        print('---------------------------------------------------------')
        ugc_adb_pushmap(equip, file1_orign, file2_aim)

    except:
        print('error')
    finally:
        # print('Done')
        pass


if __name__ == '__main__':
    main()

