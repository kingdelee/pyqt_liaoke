from PyQt5.Qt import *

class Label(QLabel):
    def sizeHint(self):
        return QSize(150, 60)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label1 = Label("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        # label1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # sp.setRetainSizeWhenHidden(True)
        label1.setSizePolicy(sp)

        dic = {"name": "sz", "age": "18"}
        dict

        # label1.setFixedSize(200, 200)
        # label2.setFixedSize(400, 100)
        # label1.hide()
        # label2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())