from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("样式表的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        label= QLabel("xxx")
        layout.addWidget(label)

        btn = QPushButton("xx2")
        layout.addWidget(btn)

        cb = QComboBox()
        cb.addItems(["1", "2", "3"])
        layout.addWidget(cb)


        sb = QSpinBox()
        layout.addWidget(sb)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    import qdarkgraystyle

    style_sheet = qdarkgraystyle.load_stylesheet_pyqt5()
    print(style_sheet)
    app.setStyleSheet(style_sheet)


    sys.exit(app.exec_())