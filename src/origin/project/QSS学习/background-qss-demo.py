from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("案例的学习")
        self.resize(800, 800)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QPushButton {
                background-image: url(../source/puke.png);
                border: 20px double red;
                background-origin: content;
                background-clip: padding;
            }
        """)
        h_layout = QHBoxLayout(self)
        for i in range(0, 13):

            btn = QPushButton(self)
            btn.setFixedSize(90, 106)
            btn.setStyleSheet("""
            QPushButton {
                padding-left: -%dpx;
                padding-top: -%dpx;
            }
            
            """%(i * 49, 0))
            h_layout.addWidget(btn)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())