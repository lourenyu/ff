import os ,datetime

class check_status():
    base_dir = r"\\10.21.100.89\Project Snake\Versions\DTS\PC\RCT_MAX"
    list = os.listdir(base_dir)
    num_files = len(list)
    print("当前文件总数量是 {}".format(num_files))

    filelist = []
    for i in range(0, len(list)):
        path = os.path.join(base_dir, list[i])
        if os.path.isfile(path):
            filelist.append(list[i])

    for i in range(0, len(filelist)):
        path = os.path.join(base_dir, filelist[i])
        if os.path.isdir(path):
            continue
        timestamp = os.path.getmtime(path)
        ts1 = os.stat(path).st_mtime

        date = datetime.datetime.fromtimestamp(timestamp)
        print(list[i], ' Time: ', date.strftime('%Y-%m-%d %H:%M:%S'))




