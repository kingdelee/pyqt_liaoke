from PyQt5.Qt import *

class Btn(QPushButton):
    pass

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("级联和冲突的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn1 = Btn("b1", self)
        btn2 = QPushButton("b2", self)


        btn1.move(100, 100)
        btn2.move(200, 200)

        self.setStyleSheet("""
        
        Btn { color: orange; }
         
        QAbstractButton { color: gray; }
        
        QPushButton { color: red; } 
        
        
        
        
        
        
        
        """)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())