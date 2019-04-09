from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErrorMessage的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # em = QErrorMessage(self)
        # em.setWindowTitle("错误提示")
        #
        # em.showMessage("社会我顺哥, 人狠话不多")
        # em.showMessage("社会我顺哥, 人狠话不多")
        # em.showMessage("社会我顺哥, 人狠话不多")
        # em.showMessage("社会我顺哥, 人狠话不多4")

        # em.open()
        # em.exec()
        pass



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    QErrorMessage.qtHandler()
    # qDebug("xxxx")
    qWarning("123456")

    sys.exit(app.exec_())