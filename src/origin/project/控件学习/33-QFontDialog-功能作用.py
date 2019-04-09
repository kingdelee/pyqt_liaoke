from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog的学习")
        self.resize(500, 500)




        self.setup_ui()

    def setup_ui(self):



        # fd = QFontDialog(self)
        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        # # fd = QFontDialog(font, self)
        # fd = QFontDialog(self)
        # fd.setCurrentFont(font)
        # # fd.setOption(QFontDialog.NoButtons)
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        # print(fd.testOption(QFontDialog.MonospacedFonts))
        # print(fd.testOption(QFontDialog.ScalableFonts))

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)

        # fd.show()

        label = QLabel(self)
        label.move(200, 100)
        label.setText("社会顺哥")

        fd = QFontDialog(self)
        for child in fd.children():
            if child.inherits("QDialogButtonBox"):
                for c in child.children():
                    if c.inherits("QPushButton"):
                        if c.text().lower() == "ok":
                            c.setText("确定呀")
                        else:
                            c.setText("取消呀")
        fd.show()

        def font_sel():
            pass
        # result = QFontDialog.getFont(self)
        #     result = QFontDialog.getFont(font,self,"选择一个好看的字体")
        #     if result[1]:
        #         label.setFont(result[0])
        #         label.adjustSize()
        # btn.clicked.connect(font_sel)

        # def cfc(font):
        #     label.setFont(font)
        #     label.adjustSize()
        # fd.currentFontChanged.connect(cfc)

        # def font_sel():
        #     print("字体已经被选择", fd.selectedFont().family())

        # btn.clicked.connect(lambda :fd.open(font_sel))

        # if fd.exec():
        #     print(fd.selectedFont().family())






if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    translator = QTranslator()
    locale = QLocale.system().name()
    print(QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    translator.load('qt_%s' % locale, QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    window = Window()
    window.show()


    sys.exit(app.exec_())