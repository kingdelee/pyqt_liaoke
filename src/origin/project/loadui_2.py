from PyQt5.Qt import *
from class_ts import Ui_Form
class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("加载ui的学习")
        self.resize(500, 500)
        self.setupUi(self)

    def setup_ui(self):
        pass

    def btn_click(self):
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()




    sys.exit(app.exec_())