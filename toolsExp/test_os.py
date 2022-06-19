import os

#1 os.exists判断文件/文件夹是否存在
restult = os.path.exists("X:\Garena\pc\Free Fire_64_Data")
print(restult)

#2 os.access判断
# os.F_OK: 检查文件是否存在;
# os.R_OK: 检查文件是否可读;
# os.W_OK: 检查文件是否可以写入;
# os.X_OK: 检查文件是否可以执行;
if os.access("X:\Garena\pc\Free Fire_64_Data",os.F_OK):
    print("The filepath is exist")
else:
    print("do not exist")