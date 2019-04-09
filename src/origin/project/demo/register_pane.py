from source.register_ui import Ui_Form
from PyQt5.Qt import *

class RegisterPane(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground)
        self.setupUi(self)

        # 记录初始数据
        self.animation_targets = [self.pushButton_3, self.pushButton_4, self.pushButton_5]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets]
        self.main_menu_pos = self.pushButton_2.pos()
        self.show_hide(False)

    def show_hide(self, is_show):
        print("展示或者隐藏", is_show)
        if is_show:
            animation_group = QSequentialAnimationGroup(self)
            for idx, target in enumerate(self.animation_targets):
                animation = QPropertyAnimation()
                animation.setTargetObject(target)
                animation.setPropertyName(b"pos")
                animation.setStartValue(self.main_menu_pos)
                animation.setEndValue(self.animation_targets_pos[idx])
                animation.setDuration(200)
                animation.setEasingCurve(QEasingCurve.OutBounce)
                animation_group.addAnimation(animation)
            animation_group.start(QAbstractAnimation.DeleteWhenStopped)
        else:
            animation_group = QSequentialAnimationGroup(self)
            for idx, target in enumerate(self.animation_targets):
                animation = QPropertyAnimation()
                animation.setTargetObject(target)
                animation.setPropertyName(b"pos")
                animation.setEndValue(self.main_menu_pos)
                animation.setStartValue(self.animation_targets_pos[idx])
                animation.setDuration(100)
                animation.setEasingCurve(QEasingCurve.OutBounce)
                animation_group.addAnimation(animation)
            animation_group.start(QAbstractAnimation.DeleteWhenStopped)


    def menu1(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(self.parentWidget().width(), 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def menu2(self):
        print("菜单2")
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")

    def menu3(self):
        QMessageBox.about(self, "撩课学院", "www.itlike.com")