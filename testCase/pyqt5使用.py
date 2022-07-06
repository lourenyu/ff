from PySide2.QtWidgets import QApplication,QMainWindow, QPushButton, QPlainTextEdit,QMessageBox

class Stats():
    def __init__(self):
        # 主窗口
        self.window = QMainWindow()
        self.window.resize(540,960)
        self.window.move(300,310)
        self.window.setWindowTitle('ugc模板管理工具')

        # 模板信息显示
        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText('请选择模板进行操作')
        self.textEdit.move(10,25)
        self.textEdit.resize(300,350)

        #操作按钮
        self.buttonImport = QPushButton('批量导入', self.window)#批量导入
        self.buttonImport.move(350, 25)
        self.buttonImport.clicked.connect(self.handleCalc)

        self.buttonOutput = QPushButton('批量导出', self.window)#批量导出
        self.buttonOutput.move(350, 55)
        self.buttonOutput.clicked.connect(self.handleCalc)

        self.buttonSearch = QPushButton('查询', self.window)#查询
        self.buttonSearch.move(350, 85)
        self.buttonSearch.clicked.connect(self.handleCalc)

        self.buttonAdd = QPushButton('添加', self.window)#添加
        self.buttonAdd.move(350, 115)
        self.buttonAdd.clicked.connect(self.handleCalc)

        self.buttonDel = QPushButton('删除', self.window)#删除
        self.buttonDel.move(350, 145)
        self.buttonDel.clicked.connect(self.handleCalc)

    def handleCalc(self):
            info = self.textEdit.toPlainText()
            salary_above_20k = ''
            salary_below_20k = ''
            for line in info.splitlines():
                if not line.strip():
                    continue
                parts = line.split(' ')
                # 去掉列表中的空字符串内容
                parts = [p for p in parts if p]
                name, salary, age = parts
                print(type(parts))
                print(salary_above_20k)
                if int(salary) >= 20000:
                    salary_above_20k += name + '\n'
                else:
                    salary_below_20k += name + '\n'
            QMessageBox.about(self.window, '统计结果',
                              f''' 以上的有：\n{salary_above_20k}\n 以下的有：\n{salary_below_20k}''')

def main():
    app = QApplication([])
    stats = Stats()
    stats.window.show()
    app.exec_()

if __name__ == '__main__':
    main()


