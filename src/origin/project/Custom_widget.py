
from PyQt5.Qt import *
class Btn(QPushButton):
    right_clicked = pyqtSignal()
    def hitButton(self, point):
        # print(point)
        # if point.x() > self.width() / 2:
        #     return True
        # return False

        # 通过给定的一个点坐标, 计算与圆心的距离
        yuanxin_x = self.width() / 2
        yuanxin_y = self.height() / 2

        hit_x = point.x()
        hit_y = point.y()

        # ((x1 - x2) 平方 + (y1 - y2) 平方) 开平方
        import math
        distance = math.sqrt(math.pow(hit_x - yuanxin_x, 2) + math.pow(hit_y - yuanxin_y, 2))
        if distance < self.width() / 2:
            return True

        # 如果距离 < 半径  True
        # 返回 False
        return False

    def paintEvent(self, evt):
        super().paintEvent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100, 150, 200), 6))

        painter.drawEllipse(self.rect())


