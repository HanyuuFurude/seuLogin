import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hanyuu\'s seu login windows [dev]'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.count = 0
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar()
        self.statusBar().showMessage('HanyuuDesu')
        self.btnLogin = QPushButton('登录', self)
        self.btnLogin.setToolTip('登录按钮')
        self.btnLogin.clicked.connect(self.on_click)
        # self.button.move(100, 100)
        self.show()

    # @pyqtSlot()
    def on_click(self):
        self.statusBar().showMessage('点按了'+(str)(self.count)+' 次')
        self.count+=1
        print('Hanyuu click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
