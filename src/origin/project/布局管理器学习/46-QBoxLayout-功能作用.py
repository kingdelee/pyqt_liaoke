from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QBoxLayout的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel("标签1")

        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color: orange;")

        # 1. 创建布局管理器对象
        # layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout = QHBoxLayout()

        # 2. 把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)


        # 3. 添加需要布局的子控件到布局管理器当中
        layout.addWidget(label1)
        # layout.addSpacing(100)
        layout.addStretch()
        layout.addWidget(label2)
        layout.addStretch()
        layout.addWidget(label3)
        # layout.addWidget(label4)

        # layout.setStretchFactor(label2, 1)

        # layout.insertSpacing(3, 60)

        # layout.insertWidget(1, label4)

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")
        #
        h_layout = QVBoxLayout()
        h_layout.setDirection(QBoxLayout.RightToLeft)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6, 1)
        h_layout.addWidget(label7)

        layout.addLayout(h_layout, 1)

        # layout.insertLayout(2, h_layout)

        label1.hide()
        label1.show()

        # layout.removeWidget(label1)
        # label1.setParent(None)


        # timer = QTimer(self)
        # def test():
        #     # QBoxLayout.LeftToRight
        #     layout.setDirection((layout.direction() + 1) % 4)
        #     pass
        # timer.timeout.connect(test)
        # timer.start(1000)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())