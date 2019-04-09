from PyQt5.Qt import *

class Btn(QPushButton):
    pass

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        box1 = QWidget(self)
        box2 = QWidget(self)
        box2.setObjectName("box2")

        box3 = QWidget(box2)
        box3.resize(150, 150)
        # box3.setStyleSheet("background-color: lightgray;")

        # box1.setStyleSheet("QPushButton {background-color: orange;}")
        # box2.setStyleSheet("background-color: cyan;")

        label1 = QLabel("标签1", box1)
        label1.resize(200, 60)
        label1.setObjectName("pink")
        label1.setProperty("notice_level", "warning")
        label1.move(50, 50)
        btn1 = Btn("按钮1", box1)
        btn1.move(150, 50)

        btn1.setObjectName("btn1")



        cb = QCheckBox("python", box1)
        cb.move(150, 100)
        cb.resize(100, 50)
        cb.setTristate(True)

        # btn1.setStyleSheet("background-color: orange;")

        label2 = QLabel("标签2", box3)
        label2.resize(100, 60)
        # label2.setProperty("notice_level", "error")

        label2.notice_level = "error"

        label2.move(50, 50)
        btn2 = QPushButton("按钮2", box2)
        btn2.move(150, 50)
        btn2.setObjectName("btn2")
        label3 = QLabel("标签3", box2)
        label3.move(200, 200)

        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        v_layout.addWidget(box1)
        v_layout.addWidget(box2)


        btn2.setEnabled(False)


        self.other_btn = QPushButton("按钮3")
        self.other_btn.show()

        # self.setStyleSheet("QPushButton {background-color: orange;}")


if __name__ == '__main__':
    import sys
    from Tool import QSSTool
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    QSSTool.setQssToObj("test.qss", app)


    sys.exit(app.exec_())