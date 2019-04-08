from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        # result = QInputDialog.getInt(self, "xxx1", "xxx2", 888, step=8)
        # result = QInputDialog.getDouble(self, "xxx1", "xxx2", 888.88, decimals = 2)
        # result = QInputDialog.getText(self, "xx1", "xx2", echo=QLineEdit.Password)
        # result = QInputDialog.getMultiLineText(self, "xx1", "xx2", "default")
        # result = QInputDialog.getItem(self, "xx1", "xx2", ["1", "2", "3"], 2, True)
        # print(result)
        input_d = QInputDialog(self, Qt.FramelessWindowHint)
        # input_d.setOption(QInputDialog.UseListViewForComboBoxItems)

        # input_d.setLabelText("请输入你的姓名")
        # input_d.setOkButtonText("好的")
        # input_d.setCancelButtonText("我想取消")
        #
        input_d.setInputMode(QInputDialog.TextInput)
        # input_d.setDoubleRange(9.9, 19.9)
        # input_d.setDoubleStep(2)
        # input_d.setDoubleDecimals(3)
        #
        input_d.setComboBoxItems(["abc", "def", "ccc"])
        # input_d.setComboBoxEditable(True)

        # input_d.intValueChanged.connect(lambda val:print("整型数据发生改变", val))
        # input_d.intValueSelected.connect(lambda val:print("整型数据最终被选中", val))

        # input_d.doubleValueChanged.connect(lambda val:print("浮点型数据发生改变", val))
        # input_d.doubleValueSelected.connect(lambda val:print("浮点型数据最终被选中", val))

        input_d.textValueChanged.connect(lambda val:print("字符串型数据发生改变", val))
        input_d.textValueSelected.connect(lambda val:print("字符串型数据最终被选中", val))

        input_d.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())