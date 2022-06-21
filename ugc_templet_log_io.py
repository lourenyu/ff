import os
import shutil
import sys


def listFiles(filepath):
    '''
    获取该文件夹下的所有文件名，并保存为一个List返回
    :param filepath: 文件路径
    :return: 包含了文件名的List
    '''
    # file = open(filepath)
    # for root, dirs, files in os.walk(file)
    filenames = []
    for pic_name in os.listdir(filepath):
        filenames.append(pic_name)
    return filenames

def moveFiles(filepath, filenames, str, target_filename):
    '''
    移动文件或者图片
    :param filepath: 文件路径
    :param filenames: 包含所有文件名的List
    :param str: 目标字符串名
    :param target_filename: 保存需要转存的文件名
    :return: None
    '''
    for i in range(len(filenames)):
        filename = filenames[i]
        # print(filename)
        if filename.find(str, 0, len(filename)) != -1:  # 不等于-1表示在该文件名中找到了目标字符串
            print(filepath + '/' + filename)
            shutil.copy(filepath + '/' + filename, target_filename)

def main():
    # 读取远程文件不稳定，先将远程文件拉到本地
    # os.system(r'adb -s emulator-5554 pull "/sdcard/Android/data/com.dts.freefireth/files" "X:\Garena\ugc"')
    filepath = r"X:\Garena\ugc\files"  # 文件所在的文件夹路径
    str = 'debugger'  # 该文件所包含的目标字符串
    target_filename = r'X:\Garena\ugc\log1'  # 保存的目标文件夹
    filenames = listFiles(filepath)  # 获取该文件夹下的所有文件名，并保存为一个List返回
    print("List内容:",filenames)
    print("文件列表长度：",len(filenames))
    print("--------------------------")
    moveFiles(filepath, filenames, str, target_filename)  # 移动

if __name__ == '__main__':
    main()
