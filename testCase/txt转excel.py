import os
import xlwt


class TxtToExcel(object):
    def __init__(self, file_path):
        """
        初始化excel
        :param file_path:文件存放目录路径
        """
        self.file_path = file_path
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.worksheet = self.workbook.add_sheet('My Worksheet', cell_overwrite_ok=True)
        self.style = xlwt.XFStyle()  # 初始化样式
        self.font = xlwt.Font()  # 为样式创建字体
        self.font.name = 'Times New Roman'
        self.font.bold = True  # 黑体
        self.font.underline = True  # 下划线
        # self.font.italic = True  # 斜体字
        self.style.font = self.font  # 设定样式
        self.header = [u'1', u'2', u'3', u'4']

    def file_list(self, file):
        """
        获取目录下的所有文件
        :return:
        """
        return os.listdir(file)

    def get_file_path(self):
        """
        获取文件路径
        :return:
        """
        file_list = self.file_list(self.file_path)
        file_path_list = []
        for file in file_list:
            path = os.path.join(self.file_path, file)
            if os.path.isdir(path):
                file_path_list.extend([os.path.join(path, f) for f in self.file_list(path)])
            else:
                file_path_list.append(path)
        return file_path_list

    def read_file_content(self, file):
        """
        读取文件内容
        :return:
        """
        with open(file, 'r', encoding='utf-8') as f:
            content = f.readlines()
        return content
        # return list(lines for lines in open(file, 'r', encoding='utf-8'))

    def writ_to_excel(self, row, content, file_name):
        """
        写入excel文件
        :return:
        """
        content_list = content.split(" ")
        while '' in content_list:
            content_list.remove('')
        i = 0
        for each_header in self.header:
            self.worksheet.write(0, i, each_header, self.style)
            i += 1
        content_list[0] = file_name

        if len(content_list) <= 3:
            return False
        print(content_list)
        for con in content_list[:3]:
            index = content_list.index(con)
            self.worksheet.write(row, index, con)
        self.worksheet.write(row, 3, '关闭')
        return True

    def get_file_content(self):
        """
        获取txt文件内容并写入excel
        :return:
        """
        files = self.get_file_path()
        files.remove(os.path.join(self.file_path, '转excel小工具.exe'))
        # 生成器方式获取文件内容
        generator_ex = (self.read_file_content(file) for file in files)
        index = 0
        for content in generator_ex:
            file_name = content.pop(0)
            for con in content:
                res = self.writ_to_excel(index+1, con, file_name)
                if res:
                    index += 1
                else:
                    index = index
        self.workbook.save(r'C:\Users\renyu.lou\Desktop\pc\RCT3\matchresult/log.xls')


if __name__ == '__main__':
    path = r"C:\Users\renyu.lou\Desktop\pc\RCT3\matchresult"
    path = os.getcwd()
    import threading
    try:
        TxtToExcel(path).get_file_content()
        # 多线程
        t1 = threading.Thread(target=TxtToExcel(path).get_file_content, args=())
        t1.start()
    except Exception as e:
        print(e)
