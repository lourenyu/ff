import os
import sys

def adb_command(command):
    """
    adb指令封装
    :param command: 具体命令
    :return: 完整的adb命令
    """
    return os.popen('adb ' + command).read()

def adb_test():
    '''
    测试设备联通性
    :return: 
    '''
    print(adb_command('devices'))

#ugc文件本地上传手机客端
def ugc_adb_pushmap(equis, file_origin, file_aim):
    '''
    本地ugc模板上传到手机
    :param equis: 设备编号
    :param file_origin: 本机模板路径
    :param file_aim: 手机路径
    :return:
    '''
    print('adb -s %s push "%s" "%s"' % (equis, file_origin, file_aim))
    pushstr = ('adb -s %s push "%s" "%s"' % (equis, file_origin, file_aim))
    os.system(pushstr)

#ugc文件下载本地
def ugc_adb_pullmap(equis, file_aim, file_origin):
    '''
    手机ugc模板拉取到本地模板库
    :param equis: 设备编号
    :param file_origin: 本机模板路径
    :param file_aim: 手机模板路径
    :return:
    '''
    pullstr = ('adb -s %s pull "%s" "%s"' % (equis, file_aim, file_origin))
    print(pullstr)
    os.system(pullstr)

    #文件*
    #adb push "X:\Garena\ugc\tamplets\test.txt" "/sdcard/"
    #adb pull /sdcard/test.txt X:\Garena\ugc\tamplets
    #文件夹*
    # adb push "X:\Garena\ugc\tamplets\test" "/sdcard/"
    # adb pull “/sdcard/test” “X:\Garena\ugc\tamplets”

def main():
    try:
        os.system("adb root")
        adb_test()
        #持续获取设备列表
        # while True:
        #     print("adb测试联通性")
        #     # #有设备则length必定>4
        #     if len(adb_test()) >4:
        #         break
        equis = input('#示例\nemulator-5554 & NXTDU16B05011269 & 192.168.3.142:5555\n请输入设备名称：')
        if len(equis) < 13:
            sys.exit()
        print('--------------------------------------------------------------------')
        key1 = input("上传文件打1，导出文件打2\n")
        if key1 == '1':#upload
            file_origin = input('#示例\nC:/Users/renyu.lou/Desktop/ugc/tamplets/Workshop/account id\n请输入本地路径:')
            print('---------------------------------------------------------')
            file_aim = input('#示例\n文件夹：/sdcard/Android/data/com.dts.freefireth/files/Workshop/account id\n请输入设备路径:')
            print('----------------------------------------------------------------------------------')
            ugc_adb_pushmap(equis, file_origin, file_aim)

        elif key1 == '2':#download
            file_aim = input('#示例\n文件夹：/sdcard/Android/data/com.dts.freefireth/files/Workshop/\n请输入设备路径:')
            print('----------------------------------------------------------------------------------')
            file_origin = input('#示例\nC:/Users/renyu.lou/Desktop/ugc/tamplets/\n请输入本地路径:')
            print('---------------------------------------------------------')
            ugc_adb_pullmap(equis, file_aim, file_origin)
        else:
            sys.exit()

    except:
        print('error')
    finally:
        # print('Done')
        pass

if __name__ == '__main__':
    main()

