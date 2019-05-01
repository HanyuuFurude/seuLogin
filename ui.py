import sys
# from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import (QMainWindow,QPushButton,QStatusBar,QApplication,QMessageBox,QLineEdit,QHBoxLayout,QGroupBox,QVBoxLayout,QWidget,QGridLayout,QLabel)
import connect

# 主UI类
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Hanyuu\'s seu login windows [dev]'
        # self.left = 100
        # self.top = 100
        # self.width = 200
        # self.height = 200
        self.wgtCanvas = QWidget()
        self.setCentralWidget(self.wgtCanvas)
        self.count = 0
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar()
        self.statusBar().showMessage('HanyuuDesu')
        self.btnAccount = QPushButton("修改登录信息", self)
        self.btnAccount.clicked.connect(self.login)
        self.btnLog = QPushButton('查看日志',self)
        self.btnLogin = QPushButton('登录', self)
        self.btnSetting = QPushButton('设置', self)
        self.btnLogin.setToolTip('登录按钮')
        self.btnLogin.clicked.connect(self.on_click)
        self.btnLogin.clicked.connect(connect.login)
        self.windowLayout = QVBoxLayout()
        self.windowLayout.addWidget(self.btnAccount)
        self.windowLayout.addWidget(self.btnLog)
        self.windowLayout.addWidget(self.btnLogin)
        self.windowLayout.addWidget(self.btnSetting)
        self.wgtCanvas.setLayout(self.windowLayout)
        self.initUI()

    def initUI(self):
        self.show()
    def login(self):
        Login()

    # @pyqtSlot()
    def on_click(self):
        self.statusBar().showMessage('点按了'+(str)(self.count)+' 次')
        self.count += 1
        buttonReply = QMessageBox.information(self, "seuLogin", "return information", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            print("yes")
        else:
            print("no")
        print('Hanyuu click')

# 登录UI
class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.windowLayout = QGridLayout()
        self.lblUsername = QLabel("用户名")
        self.letUsername = QLineEdit("")
        self.lblPassword = QLabel("密码")
        self.letPassword = QLineEdit("")
        self.btnModify = QPushButton("修改")
        self.btnCancel = QPushButton("取消")
        self.windowLayout.addWidget(self.lblUsername,0,0)
        self.windowLayout.addWidget(self.letUsername,0,1)
        self.windowLayout.addWidget(self.lblPassword,1,0)
        self.windowLayout.addWidget(self.letPassword,1,1)
        self.windowLayout.addWidget(self.btnModify,2,0)
        self.windowLayout.addWidget(self.btnCancel,2,1)
        self.setLayout(self.windowLayout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
