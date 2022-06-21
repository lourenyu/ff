import shutil
import sys
import os
import time

def CheckDuplicateName(newpath,myfile):
    """
    :param newpath:
    :param myfile:
    :return:
    """
    check_existence = os.path.join(newpath, os.path.basename(myfile))
    if os.path.exists(check_existence):
        os.remove(check_existence)

def main():
    """
    i:计数器
    filenames：log分页名称
    fs_list：log分页列表
    :return:
    """
    i = 0
    filenames = ('error.log',)
    fs_list = []
    try:
        #装弹
        for filename in filenames:
            fs_list.append(open(filename, 'w',encoding='utf-8'))
        # 从TXT文件中读出数据
        with open("C:/Users/renyu.lou/Desktop/ugc/log1/debugger-2022-06-16T12-11-37.log", mode='r', encoding='utf-8') as log_file:
            for line in log_file:
                if line.find("error") != -1: #根据指定字符串查当前行
                    fs_list[0].write(line)
                    print(line, end='')
                    time.sleep(0.1)
                    i += 1
            print("\n捕获了error %d行,日志分析完成" % i)
    except:
        pass
    finally:
        for fs in fs_list:
            fs.close()
        log_file.close()
        for filename in filenames:
            shutil.move(filename, "C:/Users/renyu.lou/Desktop/ugc/log2")



if __name__ == '__main__':
    main()
