from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # QMessageBox.about(self, "xx1", "xx2")
        # QMessageBox.aboutQt(self, "xx1")
        result = QMessageBox.question(self, "xx1", "xx2", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        print(result, "xxx")

        return None
        mb = QMessageBox(self)
        # mb = QMessageBox(QMessageBox.Warning, "xx1", "<h2>xx2</h2>",QMessageBox.Ok | QMessageBox.Discard, self)
        # mb.setModal(False)
        # mb.setWindowModality(Qt.NonModal)

        mb.setWindowTitle("消息提示")
        # mb.setIcon(QMessageBox.Information)
        mb.setIconPixmap(QPixmap("xxx.png").scaled(50, 50))
        # mb.setTextFormat(Qt.PlainText)
        mb.setText("<h3>文件内容已经被修改</h3>")
        mb.setInformativeText("<h4>是否直接关闭, 不保存?</h4>")
        mb.setCheckBox(QCheckBox("下次不再提醒", mb))
        mb.setDetailedText("<h4>你修改的内容是给每一行代码加了一个分号</h4>")


        # mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        mb.addButton(QPushButton("xx1", mb), QMessageBox.YesRole)
        mb.addButton(QPushButton("xx2", mb), QMessageBox.NoRole)
        # btn2 = mb.addButton("xx2", QMessageBox.NoRole)

        # mb.removeButton(btn2)
        # mb.setDefaultButton(btn2)
        # mb.setEscapeButton(btn2)

        # print(btn)
        # print(btn2)
        # yes_btn = mb.button(QMessageBox.Yes)
        # no_btn = mb.button(QMessageBox.No)

        # print(yes_btn, no_btn)
        mb.setTextInteractionFlags(Qt.TextEditorInteraction)
        def test(btn):
            role = mb.buttonRole(btn)
            if role == QMessageBox.YesRole:
                print("1")
            elif role == QMessageBox.NoRole:
                print("2")

            # print(btn)
            # if btn == yes_btn:
            #     print("点击了第1个按钮")
            # else:
            #     print("点击了第2个按钮")
        mb.buttonClicked.connect(test)

        mb.open()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())