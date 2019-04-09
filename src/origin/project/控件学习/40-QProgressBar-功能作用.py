from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        pb.resize(400, 40)
        # print(pb.minimum())
        # print(pb.maximum())
        #
        # pb.setMinimum(50)

        pb.setRange(0, 80)

        pb.setValue(20)

        # pb.setFormat("当前人数{} / 总人数 %m".format(pb.value() - pb.minimum()))
        pb.setInvertedAppearance(True)
        # pb.setRange(0, 0)
        # pb.reset()
        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")
        def test():
            # pb.reset()
            # print(pb.minimum())
            # print(pb.maximum())
            # print(pb.value())
            # pb.resetFormat()
            # pb.setAlignment(Qt.AlignHCenter)
            # print(pb.text())
            pb.setOrientation(Qt.Vertical)
            pb.resize(40, 400)
            print(pb.isTextVisible())
            pb.setTextDirection(QProgressBar.TopToBottom)
            pb.setInvertedAppearance(True)

        btn.clicked.connect(test)

        timer = QTimer(pb)
        def change_progress():
            # print("xxx")
            if pb.value() == pb.maximum():
                timer.stop()
            pb.setValue(pb.value() + 1)
            pass
        timer.timeout.connect(change_progress)

        timer.start(1000)
        
        pb.valueChanged.connect(lambda val:print("当前的进度值为", val))

        # pb.setTextVisible(False)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())