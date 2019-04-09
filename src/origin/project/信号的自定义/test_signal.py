from PyQt5.Qt import *

class Btn(QPushButton):
    rightClicked = pyqtSignal([str], [int, str])

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)

        if evt.button() == Qt.RightButton:
            print("应该发射右击信号")
            self.rightClicked[str].emit(self.text())
            self.rightClicked[int, str].emit(888, "itlike")



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = Btn("xx", self)
        # btn.clicked.connect(lambda :print("按钮被点击了"))
        btn.rightClicked[int, str].connect(lambda content, c2:print("按钮右键被点击了", content, c2))
        btn.pressed.connect(lambda :print("按钮被按下"))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())