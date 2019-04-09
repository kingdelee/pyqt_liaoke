from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("案例的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        w = QPushButton("xx", self)
        w.setStyleSheet("""
            QPushButton:hover {
                background-color: red;
                min-width: 200px;
                min-height: 100px;
            }        
        """)



if __name__ == '__main__':
    import sys
    from Tool import QSSTool
    app = QApplication(sys.argv)

    # QSSTool.setQssToObj("demo.qss", app)

    window = Window()
    window.show()


    sys.exit(app.exec_())