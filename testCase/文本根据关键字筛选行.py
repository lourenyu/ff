import sys
import os


listfile = []
with open(r"X:\Garena\ugc\log1\debugger-2022-06-13T11-42-14.txt", encoding='utf-8') as log_file:  # 从TXT文件中读出数据
    for line in log_file:
        listfile.append(line)  # 通过for循环一行一行加载

datalist =[]  # 定义一个数组
for item in list:  # 通过一个for循环将每一行按照空格分成不同的字符段
    l = item.split()  # 这句使用空格将item分割成字符段
    datalist.append(l)  # 将l放入数组
#
# for item in datalist:  # 通过一个for循环将某个字符段下含有某个字符串的行显示出来
#     if item[5] == 'error':
#         print(item)



