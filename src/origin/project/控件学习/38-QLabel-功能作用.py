from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # label = QLabel("社会我顺哥, 人狠话不多", self)
        # label = QLabel("账号(&s):", self)
        # label = QLabel("<a href='http://www.itlike.com'>撩课</a>", self)
        # label = QLabel("123 456 789 " * 6, self)
        label = QLabel("\n".join("123456789"), self)
        label.setStyleSheet("background-color: cyan;")
        label.move(50, 100)
        label.resize(400, 300)
        # label.adjustSize()

        # label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignRight)
        # label.setIndent(20)
        label.setMargin(20)

        # label.setTextFormat(Qt.PlainText)

        le1 = QLineEdit(self)
        le1.move(250, 250)

        le2 = QLineEdit(self)
        le2.move(250, 300)

        label.setBuddy(le1)

        # label.setPixmap(QPixmap("code.png"))
        # label.adjustSize()
        label.setScaledContents(True)

        # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)

        # label.setOpenExternalLinks(True)

        label.setWordWrap(True)

        label.setSelection(1, 2)

        # label.setText("<img src='code.png' width=60 height=60>")
        # label.setNum(888.88)

        # pic = QPicture()
        # painter = QPainter(pic)
        # painter.setBrush(QBrush(QColor(100, 200, 100)))
        # painter.drawEllipse(0, 0, 200, 200)
        #
        # label.setPicture(pic)

        # movie = QMovie("shulan.gif")
        # label.setMovie(movie)
        #
        # movie.start()
        # movie.setSpeed(1000)
        #
        # label.clear()

        label.setText("社会我顺哥<a href='http://www.itlike.com'>撩课</a>人狠话不多")

        # label.linkHovered.connect(lambda a: print(a))
        label.linkActivated.connect(lambda a: print(a))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())