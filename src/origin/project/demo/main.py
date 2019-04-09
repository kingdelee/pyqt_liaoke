# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:       Sz
   WeChat:       百川一页
-------------------------------------------------
"""
__author__ = 'Sz'
from PyQt5.Qt import *
from login_pane import LoginPane
from register_pane import RegisterPane
from Caculator_pane import CaculatorPane


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    login = LoginPane()

    register_pane = RegisterPane(login)
    register_pane.resize(login.size())
    register_pane.move(0, login.height())

    c_win = CaculatorPane()
    c_win.resize(500, 500)


    def show_r():
        animation = QPropertyAnimation(app)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, login.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start()

    login.show_register_signal.connect(show_r)

    def check_Login(account, pwd):
        print(account, pwd)
        if account == "931363918" and pwd == "itlike":
            c_win.show()
            login.hide()
        else:
            login.account_error_animation()

    login.check_login_signal.connect(check_Login)

    login.show()

    sys.exit(app.exec_())