# -*- coding:utf8 -*-

# 显示控件提示消息

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QToolTip,QPushButton,QHBoxLayout
from PyQt5.QtGui import QFont

class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm,self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,240,500,380)
        self.setWindowTitle('设置控件提示消息')
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('<b>今天是星期二<b>')

        # 创建按钮
        self.button1 = QPushButton('悬停显示提示信息')
        self.button1.setToolTip('How are you?')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main = QWidget()
        main.setLayout(layout)

        self.setCentralWidget(main)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())