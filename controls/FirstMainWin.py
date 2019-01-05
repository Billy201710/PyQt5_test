# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent = None):
        super(FirstMainWin,self).__init__(parent)
        self.resize(400,300)
        self.setWindowTitle('第一个主窗口程序')
        self.status = self.statusBar()
        self.status.showMessage('只显示5秒的消息',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstMainWin()
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main.show()
    sys.exit(app.exec_())

