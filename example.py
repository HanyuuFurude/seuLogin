from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("请选择文件/文件夹")
        self.resize(700, 500)

        self.initUI()
        self.show()

    def initUI(self):
        Layout = QGridLayout(self)
        #定义全局布局，注意参数self
        g = QGridLayout()
        v = QVBoxLayout()
        h = QHBoxLayout()
        # 定义其他两种种布局
        label1 = QLabel("快速访问")
        label2 = QLabel("桌面")
        label3 = QLabel("库")
        label4 = QLabel("我的电脑")
        label7 = QLabel("文件名(N):")
        label6 = QLabel("文件类型(T):")
        label5 = QLabel("网络")
        btn1 = QPushButton("选择")
        btn1.resize(100, 10)
        btn2 = QPushButton("取消")
        combo1 = QComboBox()
        combo2 = QComboBox()
        combo2.addItem("所有文件(*.*)")
        #定义各种控件

        splitter = QSplitter()
        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        tree = QTreeView(splitter)
        tree.setModel(model)
        #tree.setRootIndex(model.index(QDir.currentPath()))

        v.addWidget(label1)
        v.addWidget(label2)
        v.addWidget(label3)
        v.addWidget(label4)
        v.addWidget(label5)
        g.addWidget(label7, 0, 0)
        g.addWidget(label6, 1, 0)
        g.addWidget(combo1, 0, 1)
        g.addWidget(combo2, 1, 1)
        g.addWidget(btn1, 0, 2)
        g.addWidget(btn2, 1, 2)
        h.addWidget(tree)
        #把控件加入布局
        Layout.addLayout(v, 0, 0)
        Layout.addLayout(h, 0, 1)
        Layout.addLayout(g, 1, 1,)
        #把布局加入总的布局方式


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
