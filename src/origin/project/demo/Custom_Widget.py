from PyQt5.Qt import *
class Btn(QPushButton):
    title_clicked = pyqtSignal(str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setCheckable(True)
        self.setAutoExclusive(True)
        self.setProperty("type", "normal")

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        self.title_clicked.emit(self.text(), self.property("type"))

    def resizeEvent(self, evt):
        super().resizeEvent(evt)
        self.setStyleSheet("""
QPushButton[bg='gray'] {
    color: white;
    background-color: rgb(88, 88, 88);
}
QPushButton[bg='gray']:hover {
    background-color: rgb(150, 150, 150);
}
QPushButton[bg='orange'] {
    color: white;
    background-color: rgb(207, 138, 0);
}
QPushButton[bg='orange']:hover {
    background-color: rgb(238, 159, 0);
}
QPushButton[bg='orange']:checked {
    background-color: white;
    color: rgb(207, 138, 0);
}
QPushButton[bg='lightgray'] {
    color: black;
    background-color: rgb(200, 200, 200);
}
QPushButton[bg='lightgray']:hover {
    background-color: rgb(230, 230, 230);
}
        """ + """
        QPushButton[bg] {
                font-size: 28px;
                border-radius: %dpx;
                min-width: 50px;
                min-height: 50px;
        }
        """ % (min(self.height(), self.width()) * 0.5))


