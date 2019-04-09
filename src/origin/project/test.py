from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("下拉复选框的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # cb = QComboBox(self)
        # lv = QListView()
        # cb.setView()
        # self.update()
        print(QDate.fromString("2019-01-09", "yyyy-MM-dd"))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    # with open("./xxx.txt", "w", encoding="utf-8") as f:
    #     f.write("Python-GUI-编程")

    sys.exit(app.exec_())