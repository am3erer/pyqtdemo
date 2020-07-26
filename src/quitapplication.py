import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,\
    QDesktopWidget,QPushButton,QWidget,QHBoxLayout
from PyQt5.QtGui import QIcon

class quitapplication(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle('退出应用程序')
        self.resize(400,300)
        self.button1 = QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClickButton)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


    def onClickButton(self):
        sender = self.sender()
        print(sender.text + ' 按钮被按下')
        app = QApplication.instance()

        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/龙.png'))
    main = quitapplication()
    main.show()
    sys.exit(app.exec_())
