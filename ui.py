import sys
# from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QStatusBar, QApplication, QMessageBox, QTextBrowser,
                             QLineEdit, QHBoxLayout, QGroupBox, QVBoxLayout, QWidget, QGridLayout, QLabel)
from PyQt5.QtCore import Qt
import sys
import threading
import time
import datetime
import connect


# 主UI类


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        #  窗体本体绘制
        self.title = 'Hanyuu\'s seu login windows [dev]'
        # self.left = 100
        # self.top = 100
        # self.windowWidth = 200
        # self.windowHeight = 200
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.wgtCanvas = QWidget()
        self.setCentralWidget(self.wgtCanvas)
        # self.setWindowFlags(PyQt5.QtCore.Qt.WindowMinimizeButtonHint)
        # self.setFixedWidth(self.PdmWidth(),self.PdmHeight())

        # 定义控件，绑定事件
        self.btnAccount = QPushButton("修改登录信息", self)
        self.btnAccount.clicked.connect(self.on_click_account)

        self.btnLog = QPushButton('查看日志', self)
        self.btnLog.clicked.connect(self.on_click_log)

        self.btnLogin = QPushButton('登录', self)
        self.btnLogin.clicked.connect(self.on_click_login)
        self.btnLogin.setToolTip('登录按钮')

        self.btnLogout = QPushButton('登出', self)
        self.btnLogout.clicked.connect(self.on_click_logout)

        self.btnSetting = QPushButton('设置', self)
        self.btnSetting.clicked.connect(self.on_click_setting)

        self.statusBar().showMessage('欢迎')

        # 控件布局
        self.windowLayout = QVBoxLayout()
        self.windowLayout.addWidget(self.btnAccount)
        self.windowLayout.addWidget(self.btnLog)
        self.windowLayout.addWidget(self.btnLogin)
        self.windowLayout.addWidget(self.btnLogout)
        self.windowLayout.addWidget(self.btnSetting)
        self.wgtCanvas.setLayout(self.windowLayout)
        self.setWindowTitle(self.title)
        self.updater = None
        self.show()

    # 修改账户
    def on_click_account(self):
        self.loginWindow = Account()

    #  登录
    def on_click_login(self):
        try:
            res = connect.login()
        except Exception as e:
            QMessageBox.critical(self, 'seuLogin', '错误：\n' +
                                 str(e), QMessageBox.Ok, QMessageBox.Ok)
            return
        QMessageBox.information(self, 'seuLogin', res,
                                QMessageBox.Ok, QMessageBox.Ok)

    #  登出
    def on_click_logout(self):
        try:
            res = connect.logout()
        except Exception as e:
            QMessageBox.critical(self, 'seuLogin', '错误：\n' +
                                 str(e), QMessageBox.Ok, QMessageBox.OK)
        QMessageBox.information(self, 'seuLogin', res,
                                QMessageBox.Ok, QMessageBox.Ok)

    # 查看日志
    def on_click_log(self):
        self.log = Log()
    # 设置

    def on_click_setting(self):
        QMessageBox.information(
            self, 'seuLogin', '当前无可用设置', QMessageBox.Ok, QMessageBox.Ok)

    def closeEvent(self, event):
        choose = QMessageBox.question(
            self, 'seuLogin', '真的要退出嘛？', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if choose == QMessageBox.Yes:
            self.updater.stop()
            return super().closeEvent(event)
        else:
            return event.ignore()

    # 修改状态栏信息
    def modifyStatusBar(self, info: str)->None:
        self.statusBar().showMessage(info)

# 修改账户模块


class Account(QWidget):

    def __init__(self):
        # 窗体绘制，控件绘制和事件绑定
        super().__init__()
        self.windowLayout = QGridLayout()
        self.lblUsername = QLabel("用户名")
        self.letUsername = QLineEdit("")
        self.lblPassword = QLabel("密码")
        self.letPassword = QLineEdit("")
        self.btnModify = QPushButton("修改")
        self.btnModify.clicked.connect(self.on_click_modify)
        self.btnCancel = QPushButton("取消")
        self.btnCancel.clicked.connect(self.on_click_cancel)
        self.windowLayout.addWidget(self.lblUsername, 0, 0)
        self.windowLayout.addWidget(self.letUsername, 0, 1)
        self.windowLayout.addWidget(self.lblPassword, 1, 0)
        self.windowLayout.addWidget(self.letPassword, 1, 1)
        self.windowLayout.addWidget(self.btnModify, 2, 0)
        self.windowLayout.addWidget(self.btnCancel, 2, 1)
        self.setLayout(self.windowLayout)
        self.show()

    # 修改事件
    def on_click_modify(self):
        try:
            # 写入数据
            connect.writeAccount(self.letUsername.text())
            connect.writePassword(self.letPassword.text())
            QMessageBox.information(
                self, 'seuLogin', '保存成功', QMessageBox.Ok, QMessageBox.Ok)
            self.close()
        except Exception as e:
            # 数据写入出现异常，反馈错误
            QMessageBox.critical(
                self, 'seuLogin', '出现错误:\n' + str(e), QMessageBox.Ok, QMessageBox.Ok)
            self.close()
    # 取消事件

    def on_click_cancel(self):
        self.close()
# 日志模块


class Log(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('seuLogin日志查看器')
        self.layout = QHBoxLayout()
        self.txtBroser = QTextBrowser()
        self.layout.addWidget(self.txtBroser)
        self.setLayout(self.layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        try:
            self.txtBroser.setPlainText(connect.logFile())
        except Exception as e:
            QMessageBox.critical(self, 'seuLogin', '错误：\n' +
                                 str(e), QMessageBox.Ok, QMessageBox.Ok)
        self.show()

# 联网状态巡检器


class StatusUpdater(threading.Thread):
    def __init__(self, handler: App):
        threading.Thread.__init__(self, name='updater')
        self.handler = handler
        self.autoQuery = True
        self.updateInterval = 600
        self.updateIntervalWhenFailed = 60

    def run(self):
        while self.autoQuery:
            print('running')
            try:
                res = connect.getStatus()
            except Exception as e:
                self.handler.modifyStatusBar(
                    datetime.datetime.now().strftime('%H:%M:%S')+'登录信息更新失败')
                time.sleep(self.updateIntervalWhenFailed)
                continue
            self.handler.modifyStatusBar(
                info=(datetime.datetime.now().strftime('%H:%M:%S')+res))
            if res == '用户未登录':
                try:
                    connect.login()
                except Exception:
                    time.sleep(self.updateIntervalWhenFailed)
                    continue
            time.sleep(self.updateInterval)

    def stop(self):
        self.autoQuery = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #开启高分辨率适配
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    ex = App()
    # 设置联网巡检器
    updater = StatusUpdater(ex)
    updater.start()
    # 将巡检器传递给主线程以便主线程退出时结束巡检器线程
    ex.updater = updater
    sys.exit(app.exec_())
