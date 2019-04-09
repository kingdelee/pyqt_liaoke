from source.login_ui import Ui_Form
from PyQt5.Qt import *

class LoginPane(QWidget, Ui_Form):
    show_register_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

        movie = QMovie("./source/login_top_bg.gif")
        movie.setScaledSize(QSize(539, 170))
        self.label.setMovie(movie)
        movie.start()



    def show_register(self):
        self.show_register_signal.emit()


    def account_error_animation(self):
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.widget_2)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.widget_2.pos())
        animation.setKeyValueAt(0.3, self.widget_2.pos() + QPoint(-10, 0))
        animation.setKeyValueAt(0.5, self.widget_2.pos())
        animation.setKeyValueAt(0.7, self.widget_2.pos() + QPoint(10, 0))
        animation.setKeyValueAt(1, self.widget_2.pos())
        animation.setDuration(120)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def check_login(self):
        account = self.comboBox.lineEdit().text()
        pwd = self.lineEdit.text()
        self.check_login_signal.emit(account, pwd)

    def join_qq_group(self):
        QDesktopServices.openUrl(QUrl('http://shang.qq.com/wpa/qunwpa?idkey=d3e27c90a382e7752d603003bec42c3effae3a33a9c009eb9f95ec0a13efbae4'))

