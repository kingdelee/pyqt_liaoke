from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("样式声明的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label = QCheckBox("复选框", self)
        # layout = QVBoxLayout(self)
        # layout.addWidget(label)

        label.resize(300, 300)
        label.move(0, 0)

        self.qss边框(label)

    def qss边框(self, label):
        label.setStyleSheet("""
        QCheckBox {
            color: gray;    
            border: 10px double rgb(76, 76, 76);
            padding: 5px;
        }
 
        QCheckBox::indicator {
            subcontrol-origin: border;
            subcontrol-position: left center;
            background: white;
            border: 2px solid gray;
        }
 
        QCheckBox::indicator:checked {
            background: rgb(76, 76, 76);
        }
        
        """)

        return None
        label.setStyleSheet("""
        QSpinBox {
            font-size: 26px;
            color: orange;
            border: 10px double red;
            border-radius: 10px;
            background-color: lightgray;
        
        }
        QSpinBox::up-button, QSpinBox::down-button {
            width: 50px;
            height: 50px;
        }
        QSpinBox::up-button {
            subcontrol-origin: padding;
            subcontrol-position:left center;
            image: url(../source/up.png)
        }
        QSpinBox::up-button:hover {
            bottom: 10px;
        }
        
        QSpinBox::down-button:hover {
            
            top: 100px;
        }
        QSpinBox::down-button {
            subcontrol-origin: padding;
            subcontrol-position:right center;
            image: url(../source/down.png)
        }
        
        
        """)

        return None
        # label.setStyleSheet("""
        # QLabel {
        #     background-color: red;
        #     font-family: 隶书;
        #     font-size: 30px;
        #     font-style: italic;
        #     font-weight: 900;
        #     color: orange;
        #
        #     width: 400px;
        #     height: 400px;
        #
        # }
        #
        # """)

        # label.setStyleSheet("""
        #     QTextEdit {
        #         background-color: rgb(100, 200, 100);
        #         background-image: url(../source/desktop.png);
        #         background-repeat: no-repeat;
        #         background-position: left top;
        #         background-origin: border;
        #         background-clip: content;
        #         background-attachment: fixed;
        #
        #         color: red;
        #         border:20px double red;
        #         padding: 20px;
        #         margin: 20px;
        #
        #
        #
        #     }
        #
        # """)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())