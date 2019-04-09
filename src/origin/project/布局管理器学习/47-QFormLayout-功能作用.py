from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        name_label = QLabel("姓名(&n):")
        age_label = QLabel("年龄(&g):")

        name_le = QLineEdit()
        age_sb = QSpinBox()

        # name_label.setBuddy(name_le)
        # age_label.setBuddy(age_sb)

        sex_label = QLabel("性别")
        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn = QPushButton("提交")

        # 1. 创建布局管理器
        layout = QFormLayout()

        # 2. 把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        # 3. 把需要布局的子控件交给布局管理器进行布局
        # layout.addRow(name_label, name_le)
        layout.addRow("姓名(&n)", name_le)
        layout.addRow(sex_label, h_layout)
        # layout.addRow("性别:", h_layout)
        layout.addRow(age_label, age_sb)
        # layout.addRow("年龄(&g)", age_sb)
        layout.addRow(submit_btn)

        print(layout.labelForField(name_le).setText("xxx"*10))
        print(layout.formAlignment() == Qt.AlignLeft | Qt.AlignTop)
        layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.setLabelAlignment(Qt.AlignRight)
        layout.setHorizontalSpacing(60)

        layout.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)


        layout.setVerticalSpacing(60)
        # layout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        # layout.insertRow(-1, "性别:", h_layout)
        #
        # print(layout.rowCount())
        # print(layout.getWidgetPosition(male_rb))
        # print(layout.getLayoutPosition(h_layout))

        # layout.setWidget(0, QFormLayout.LabelRole, name_label)
        # layout.setWidget(0, QFormLayout.FieldRole, name_le)
        # layout.addRow(name_label)
        # print(layout.getWidgetPosition(name_label))
        # layout.setWidget(0, QFormLayout.LabelRole, name_le)

        age_sb.destroyed.connect(lambda :print("年龄步长被释放"))
        age_label.destroyed.connect(lambda :print("年龄标签被释放"))


        # layout.removeRow(h_layout)
        # layout.removeWidget(age_label)
        # age_label.setParent(None)
        # layout.removeRow(2)
        # print(layout.takeRow(2).labelItem.widget())
        # print(layout.takeRow(2).fieldItem)
        # age_sb.hide()
        # age_label.hide()
        # print(dir(QFormLayout.TakeRowResult))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())