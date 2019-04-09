from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动画的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        btn = QPushButton("测试按钮", self)
        btn.move(100, 100)
        btn.resize(200, 200)
        btn.setStyleSheet("background-color: cyan;")

        # 1. 创建一个动画对象, 并且设置目标 属性
        # animation = QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b"pos")
        # animation = QPropertyAnimation(btn, b"geometry", self)
        animation = QPropertyAnimation(btn, b"pos", self)

        # 2. 设置属性值 开始 插值 结束
        animation.setStartValue(QPoint(0, 0))
        # animation.setKeyValueAt(0.5, 0.5)
        # animation.setKeyValueAt(1, 1)
        animation.setEndValue(QPoint(300, 300))


        # 3. 动画时长
        animation.setDuration(3000)

        animation.setLoopCount(3)

        animation.setEasingCurve(QEasingCurve.OutBounce)
        # animation.setDirection(QAbstractAnimation.Backward)
        # 4. 启动动画
        animation.start()

        print(animation.totalDuration(), animation.duration())
        # btn.clicked.connect(lambda :print(animation.loopCount(), animation.currentLoop()))
        # btn.clicked.connect(lambda :print(animation.currentTime(), animation.currentLoopTime()))

        def animation_operation():
            if animation.state() == QAbstractAnimation.Running:
                animation.pause()
            elif animation.state() == QAbstractAnimation.Paused:
                animation.resume()
            elif animation.state() == QAbstractAnimation.Stopped:
                animation.resume()

        btn.clicked.connect(animation_operation)

        animation.currentLoopChanged.connect(lambda val:print("当前循环次数发生改变", val))
        animation.finished.connect(lambda :print("动画执行完毕"))
        animation.stateChanged.connect(lambda ns, os:print("状态发生改变", ns, os))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())