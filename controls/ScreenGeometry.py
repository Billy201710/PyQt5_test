# -*- coding:utf8 -*-

import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication,QWidget,QPushButton,QMainWindow

def onClickButton():
    print('1')
    print('widge.x() = %d' % widge.x())  # 250 （窗口横坐标）
    print('widge.y() = %d' % widge.y())  # 200  (窗口纵坐标)
    print('widge.width() = %d' % widge.width())  # 300 (工作区宽度)
    print('widge.height() = %d' % widge.height())  # 240 (工作区高度)
    print('2')
    print('widge.geometry().x() = %d' % widge.geometry().x())  # 258 （工作区横坐标）
    print('widge.geometry().y() = %d' % widge.geometry().y())  # 231  (工作区纵坐标)
    print('widge.geometry().width() = %d' % widge.geometry().width())  # 300 (工作区宽度)
    print('widge.geometry().height() = %d' % widge.geometry().height())  # 240 (工作区高度)
    print('3')
    print('widge.frameGeometry().x() = %d' % widge.frameGeometry().x())  # 250 （窗口横坐标）
    print('widge.frameGeometry().y() = %d' % widge.frameGeometry().y())  # 200  (窗口纵坐标)
    print('widge.frameGeometry().width() = %d' % widge.frameGeometry().width())  # 316 (窗口宽度)
    print('widge.frameGeometry().height() = %d' % widge.frameGeometry().height())  # 279 (窗口高度)

app = QApplication(sys.argv)
widge = QWidget()
btn = QPushButton(widge)
btn.setText('按钮')

btn.clicked.connect(onClickButton)

widge.setWindowTitle('屏幕坐标系')

btn.move(24,52)

widge.move(250,200)

widge.resize(300,240)  # 设置工作区尺寸

widge.show()

sys.exit(app.exec_())