# -*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QDesktopWidget,QMainWindow
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent = None):
        super(FirstMainWin,self).__init__(parent)
        self.setWindowTitle('第一个主窗口程序')
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('只显示5秒的消息',5000)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = FirstMainWin()
    main.show()
    main.center()
    sys.exit(app.exec_())