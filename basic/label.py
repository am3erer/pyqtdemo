'''
QLablel控件
常用的信号
1.当鼠标滑过QLabel控件时触发 linkHovered
2.当鼠标单击QLabel控件时触发 linkActivated
'''

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.resize(400,500)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签。</font>")
        label1.setAutoFillBackground(True)
        palette =QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序。</a>")
        label2.setAlignment(Qt.AlignCenter)

        label3.setPixmap(QPixmap("../images/龙.png"))
        label3.setAlignment(Qt.AlignCenter)

        label4.setText("<a href='https://www.bilibili.com/video/BV154411n79k?p=29'>我看到视频链接")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是个链接")
        label4.setOpenExternalLinks(True)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)


    def linkHovered(self):
        QMessageBox.about(self,'提示','当鼠标滑过')

    def linkClicked(self):
        QMessageBox.about(self,'提示','当鼠标单击')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
