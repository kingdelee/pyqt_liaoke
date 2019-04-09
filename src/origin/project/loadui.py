from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ui的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        from PyQt5.uic import loadUi
        loadUi("class_ts.ui", self)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    print(dir(window))
    def click():
        print("xxx")
        account = window.lineEdit.text()
        pwd = window.lineEdit_2.text()
        print(account, pwd)
    window.pushButton.clicked.connect(click)


    sys.exit(app.exec_())