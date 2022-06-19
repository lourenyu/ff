import os

def ugc_adb_pull_log(equis, file_aim, file_origin):
    '''
    手机ugc模板拉取到本地模板库
    :param equis: 设备编号
    :param file_origin: 本机模板路径
    :param file_aim: 手机模板路径
    :return:
    '''
    print('adb -s %s pull "%s" "%s"' % (equis, file_aim, file_origin))
    pullstr = 'adb -s %s pull "%s" "%s"' % (equis, file_aim, file_origin)
    os.system(pullstr)

def main():
    equis = input('#示例\nemulator-5554 & NXTDU16B05011269 & 192.168.3.142:5555\n请输入设备名称：')
    print('--------------------------------------------------------------------')
    file_aim = input('#示例\n文件夹：/sdcard/Android/data/com.dts.freefireth/files\n请输入设备路径:')
    print('----------------------------------------------------------------------------------')
    file_origin = input('#示例\nC:/Users/renyu.lou/Desktop/ugc/tamplets\n请输入本地路径:')
    print('---------------------------------------------------------')
    ugc_adb_pull_log(equis, file_aim, file_origin)
    pass

if __name__ == '__main__':
    main()