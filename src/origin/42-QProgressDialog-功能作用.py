from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pd = QProgressDialog(self)
        # pd = QProgressDialog("xx1", "xx2", 1, 1000, self)
        pd.setWindowTitle("xx3")
        pd.setLabelText("下载进度")
        pd.setCancelButtonText("取消下载")

        pd.setRange(0, 100)
        pd.setValue(95)
        print(pd.minimum())
        print(pd.maximum())
        # pd.setAutoClose(False)
        # pd.setAutoReset(False)
        # pd.open(lambda :print("对话框被取消"))
        pd.show()
        # pd.setMinimumDuration(0)
        # for i in range(1, 101):
        #     # import time
        #     # time.sleep(1)
        #     pd.setValue(i)
        timer = QTimer(pd)
        def test():
            # if pd.value() + 1 >= pd.maximum() or pd.wasCanceled():
            if pd.value() + 1 >= pd.maximum():
                timer.stop()
                print(pd.autoClose())
            pd.setValue(pd.value() + 1)

            if pd.value() == 98:
                pd.cancel()

        timer.timeout.connect(test)
        timer.start(1000)


        pd.canceled.connect(timer.stop)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())