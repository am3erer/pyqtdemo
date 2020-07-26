import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,\
    QDesktopWidget,QPushButton,QWidget,QHBoxLayout,QToolTip
from PyQt5.QtGui import QIcon,QFont

class iconForm(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天是星期天')
        self.setWindowTitle('设置控件提示消息')
        self.setWindowIcon(QIcon('../images/龙.png')) #不推荐
        self.resize(400,300)    #设置工作区的尺寸


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('../images/龙.png'))   @推荐使用这个设置窗口图标
    main = iconForm()
    main.show()
    sys.exit(app.exec_())
