from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cw = QCalendarWidget(self)
        # cw.setMinimumDate()
        # cw.setMaximumDate()
        cw.setDateRange(QDate(1990, 1, 1), QDate(2020, 11, 12))
        # cw.setSelectedDate(QDate(-9999, 1, 1))

        # cw.setDateEditEnabled(False)
        cw.setDateEditAcceptDelay(3000)

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(400, 100)
        #
        # showToday()
        # showSelectedDate()
        # showNextYear()
        # showPreviousYear()
        # showNextMonth()
        # showPreviousMonth()
        # setCurrentPage(int year, int month)

        # btn.clicked.connect(cw.showNextMonth)
        btn.clicked.connect(lambda :cw.setCurrentPage(2008, 8))

        # cw.activated.connect(lambda date:print(date))
        cw.clicked.connect(lambda date:print(date))
        # cw.currentPageChanged.connect(lambda y, m:print(y, m))
        cw.selectionChanged.connect(lambda :print("选中的日期发生改变", cw.selectedDate()))

        cw.setSelectedDate(QDate(2008, 8, 8))





        # btn.clicked.connect(lambda :print(cw.monthShown()))
        # btn.clicked.connect(lambda :print(cw.yearShown()))
        # btn.clicked.connect(lambda :print(cw.selectedDate()))

        # cw.setNavigationBarVisible(False)
        cw.setFirstDayOfWeek(Qt.Sunday)
        cw.setGridVisible(True)

        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(16)
        tcf.setFontUnderline(True)

        cw.setHeaderTextFormat(tcf)

        # cw.setHorizontalHeaderFormat(QCalendarWidget.NoHorizontalHeader)

        cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        t_tcf = QTextCharFormat()
        t_tcf.setFontPointSize(20)
        t_tcf.setToolTip("这是星期二")

        # cw.setWeekdayTextFormat(Qt.Tuesday, t_tcf)

        cw.setDateTextFormat(QDate(2018, 12, 12), t_tcf)

        # cw.setSelectionMode(QCalendarWidget.NoSelection)
        #
        # cw.setSelectedDate(QDate(2018, 12, 11))





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())