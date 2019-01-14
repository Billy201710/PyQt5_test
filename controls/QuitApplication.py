# -*- coding:utf8 -*-

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton,QMainWindow

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('点击关闭程序')

        # 创建按钮
        self.button1 = QPushButton('点击关闭程序')

        # 连接按钮和槽函数
        self.button1.clicked.connect(self.onClickButton)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        main = QWidget()
        main.setLayout(layout)

        self.setCentralWidget(main)

    def onClickButton(self):
        app = QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())