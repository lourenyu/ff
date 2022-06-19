import os
import shutil


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
    :param filepath: 文件或者图片的路径
    :param filenames: 包含所有文件名的List
    :param str: 目标字符串名
    :param target_filename: 保存需要转存的文件名
    :return: None
    '''
    for i in range(len(filenames)):
        filename = filenames[i]
        # print(filename)
        if (filename.find(str, 0, len(filename)) != -1):  # 不等于-1表示在该文件名中找到了目标字符串
            # print("A4/" + filename)
            print(filepath + '/' + filename)
            shutil.copy(filepath + '/' + filename, target_filename)


if __name__ == '__main__':
    filepath = 'A4'  # 图片或文件所在的文件夹路径
    str = 'rgb.png'  # 该图片或者文件所包含的目标字符串
    target_filename = 'rgb_pic'  # 保存的目标文件夹
    filenames = listFiles(filepath)  # 获取该文件夹下的所有文件名，并保存为一个List返回
    moveFiles(filepath, filenames, str, target_filename)  # 移动