from source.caculator_ui import Ui_Form
from Caculator_Tool import Caculator
from PyQt5.Qt import *

class CaculatorPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.caculator = Caculator()
        self.caculator.show_data.connect(self.lineEdit.setText)

    def btn_clicked(self, content, type):
        print(content, type)
        self.caculator.parse({"type": type, "data": content})