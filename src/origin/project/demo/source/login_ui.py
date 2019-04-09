# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(534, 408)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(534, 408))
        Form.setMaximumSize(QtCore.QSize(534, 408))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("background-color: rgb(170, 170, 127);")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("color: rgb(138, 138, 138)")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 30, -1, 10)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 45))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QComboBox:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QComboBox:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;    \n"
"    width: 60px;\n"
"    height: 40px;               \n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/lk/down_arrow.png);\n"
"    width: 60px;\n"
"    height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    min-height: 60px;\n"
"}\n"
"QComboBox QAbstractItemView:item {\n"
"    color: lightblue;\n"
"}")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/lk/python_jh.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/lk/python_gui.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    font-size: 20px;\n"
"    border: none;\n"
"    border-bottom: 1px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 1px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom: 1px solid rgb(18, 183, 245);\n"
"}\n"
"")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox.setStyleSheet("color: rgb(149, 149, 149);")
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setStyleSheet("color: rgb(149, 149, 149);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(33, 174, 250);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(72, 203, 250);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(85, 85, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/lk/dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 50))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_3.setStyleSheet("border-image: url(:/lk/gui_qq_group.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 5)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.show_register)
        self.pushButton.clicked.connect(Form.check_login)
        self.pushButton_3.clicked.connect(Form.join_qq_group)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册账号"))
        self.comboBox.setItemText(0, _translate("Form", "635040761"))
        self.comboBox.setItemText(1, _translate("Form", "931363918"))
        self.checkBox.setText(_translate("Form", "自动登录"))
        self.checkBox_2.setText(_translate("Form", "记住密码"))
        self.pushButton.setText(_translate("Form", "安全登录"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

