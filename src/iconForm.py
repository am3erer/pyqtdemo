import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,\
    QDesktopWidget,QPushButton,QWidget,QHBoxLayout
from PyQt5.QtGui import QIcon

class iconForm(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle('设置窗口图标')
        self.setWindowIcon(QIcon('../images/龙.png')) #不推荐
        self.resize(400,300)    #设置工作区的尺寸
        self.button1 = QPushButton('退出应用程序')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('../images/龙.png'))   @推荐使用这个设置窗口图标
    main = iconForm()
    main.show()
    sys.exit(app.exec_())
