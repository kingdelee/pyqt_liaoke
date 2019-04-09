from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("装饰器连接信号与槽的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.setObjectName("btn")
        btn.resize(200, 200)
        btn.move(100, 100)

        btn2 = QPushButton("测试按钮2", self)
        btn2.setObjectName("btn2")
        btn2.resize(200, 200)
        btn2.move(100, 300)

        QMetaObject.connectSlotsByName(self)
        # btn.clicked.connect(self.click)

    @pyqtSlot(bool)
    def on_btn_clicked(self, val):
        print("按钮被点击了", val)

    # self.btn.clicked[bool].connect(self.btn_clicked)
    # def btn_clicked(self):
    #     pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())