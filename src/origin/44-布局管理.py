from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # 创建3个子控件
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        # 垂直排列, 子控件的宽度 = 父控件的宽度; 子控件的高度 = 父控件的高度 / 3
        # label_width = self.width()
        # label_height = self.height() / 3
        # label1.resize(label_width, label_height)
        # label2.resize(label_width, label_height)
        # label3.resize(label_width, label_height)
        #
        # label1.move(0, 0)
        # label2.move(0, label_height)
        # label3.move(0, label_height * 2)
        #
        # label2.hide()
        #
        # timer =QTimer(self)
        # timer.timeout.connect(lambda :label1.setText(label1.text() + "itlike\n"))
        # timer.start(1000)

        # 布局管理器实现方式
        layout = QHBoxLayout()

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())