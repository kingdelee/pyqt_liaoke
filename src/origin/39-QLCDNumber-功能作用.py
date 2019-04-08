from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLCDNumber的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # lcd = QLCDNumber(self)
        lcd = QLCDNumber(self)
        lcd.move(0, 0)
        lcd.resize(300, 100)

        lcd.setDigitCount(2)

    #     0 / O, 1, 2, 3, 4, 5 / S, 6, 7, 8, 9 / g
    #
    # A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y
    # : ' 空格
    #     lcd.display(": '")
    #     lcd.display(12)

        # lcd.setMode(QLCDNumber.Hex)

        print(lcd.checkOverflow(99))
        print(lcd.checkOverflow(100))
        lcd.overflow.connect(lambda :print("数值溢出"))


        lcd.display(99)

        lcd2 = QLCDNumber(self)
        lcd2.move(0, 100)
        lcd2.resize(300, 100)

        lcd3 = QLCDNumber(self)
        lcd3.move(0, 200)
        lcd3.resize(300, 100)

        lcd2.display(99)
        lcd3.display(99)

        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)

        # btn = QPushButton(self)
        # btn.setText("测试按钮")
        # btn.move(50, 50)
        # btn.clicked.connect(lambda :print(lcd.value()))
        # btn.clicked.connect(lambda :print(lcd.intValue()))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())