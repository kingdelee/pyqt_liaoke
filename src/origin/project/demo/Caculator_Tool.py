
from PyQt5.Qt import *

class Caculator(QObject):

    show_data = pyqtSignal(str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.datas = [] # 存放所有数据
        self.result = 0

    def parse(self, dic={"type": "", "data": ""}):

        if dic["data"] == "AC":
            self.clear()
            return None

        # 判断数据是否为空
        if len(self.datas) == 0:
            if dic["type"] == "num":
                self.datas.append(dic)
                self.show_data.emit(dic["data"])
            return None


        # 判断控制键
        if dic["type"] == "control":
            if dic["data"] == "%" and self.datas[-1]["type"] == "num":
                self.datas[-1]["data"] = str(float(self.datas[-1]["data"]) / 100)
                self.show_data.emit(self.datas[-1]["data"])
            elif dic["data"] == "+/-" and self.datas[-1]["type"] == "num":
                self.datas[-1]["data"] = str(float(self.datas[-1]["data"]) * -1)
                self.show_data.emit(self.datas[-1]["data"])
            return None

        # 判断 =
        if dic["type"] == "equal":
            self.equal()
            return None

        # 判断数据键
        if dic["type"] == "num":
            if self.datas[-1]["type"] == dic["type"]:
                self.datas[-1]["data"] += dic["data"]
            else:
                self.datas.append(dic)
            self.show_data.emit(self.datas[-1]["data"])

        if dic["type"] == "operator":
            if self.datas[-1]["type"] == dic["type"]:
                self.datas[-1]["data"] = dic["data"]
            else:
                self.caculate()
                self.datas.append(dic)

    def clear(self):
        self.datas = []
        self.result = 0.0
        self.show_data.emit("0.0")

    def caculate(self):
        expression = ""
        for data_dic in self.datas:
            expression += data_dic["data"]
        result = str(eval(expression))
        self.show_data.emit(result)
        return result


    def equal(self):
        result = self.caculate()
        self.datas = [{"type": "num", "data": result}]