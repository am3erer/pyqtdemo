import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon

class centerForm(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setWindowTitle('让窗口居中')
        self.resize(400,300)
        self.center()

    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft),int(newTop))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../images/龙.png'))
    main = centerForm()
    main.show()
    sys.exit(app.exec_())
