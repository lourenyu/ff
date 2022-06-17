import os

def ugc_adb_pullmap(equi,file2_aim, file1_orign):
    os.system('adb -s %s push "%s" %s' % (equi, file2_aim, file1_orign))


def ugc_pull_log():
    try:
        #判断是否存在log
        if True:
            os.system("adb pull log文件夹路径 本机路径")
            
        else:
            pass



    except:
        print('error')
    finally:
        pass




def main():
    pass

if __name__ == '__main__':
    main()
