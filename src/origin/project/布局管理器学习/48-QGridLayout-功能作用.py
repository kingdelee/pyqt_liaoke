from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()

        self.setLayout(gl)

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color: cyan;")
        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color: yellow;")
        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color: red;")

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color: pink;")
        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color: blue;")
        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color: cyan;")
        #
        v_layout = QVBoxLayout()
        # v_layout.setDirection(QBoxLayout.RightToLeft)
        v_layout.addWidget(label5, 1)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)


        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 3, 3)

        gl.addLayout(v_layout, 4, 0, 1, 4)

        # print(gl.getItemPosition(2))
        # print(gl.itemAtPosition(1, 2).widget().text())

        # gl.setColumnMinimumWidth(0, 100)
        # gl.setRowMinimumHeight(0, 100)

        gl.setColumnStretch(0, 2)
        gl.setColumnStretch(1, 1)

        gl.setRowStretch(4, 1)

        # gl.setVerticalSpacing(60)
        # gl.setHorizontalSpacing(60)
        # gl.setSpacing(60)

        print(gl.spacing())
        print(gl.horizontalSpacing())
        print(gl.verticalSpacing())

        gl.setOriginCorner(Qt.BottomRightCorner)

        print(gl.rowCount())
        print(gl.columnCount())

        # print(gl.cellRect(0, 1))
        # print(gl.itemAtPosition(0, 1).widget().text())










if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    gl = window.layout()

    print(gl.cellRect(10, 11))


    sys.exit(app.exec_())