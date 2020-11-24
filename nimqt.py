import sys
import time
from PyQt5 import uic, QtWidgets

Form, _ = uic.loadUiType('nim.ui')


class Example(QtWidgets.QWidget, Form):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
        self.pBSet.clicked.connect(self.setStone)
        self.pBRun.clicked.connect(self.runStep)
        self.lcdNumber.setStyleSheet(
            """QLCDNumber {background-color: black }""")
        self.label_msg.setText('')
        self.countSt = 0

    def setStone(self):
        self.countSt = self.spinBox.value()
        self.lcdNumber.display(self.countSt)
        self.listWidget.clear()
        self.label_msg.setText('')
        self.spinBox_2.setMaximum(3)
        x = self.step(self.countSt)
        self.listWidget.addItem('Компьтер взял - ' + str(x))
        self.countSt -= x
        self.lcdNumber.display(self.countSt)
        if self.countSt < 3:
            self.spinBox_2.setMaximum(self.countSt)
        self.pBRun.setEnabled(True)

    def runStep(self):
        x = self.spinBox_2.value()
        self.listWidget.addItem('Игрок взял - ' + str(x))
        self.countSt -= x
        self.lcdNumber.display(self.countSt)
        x = self.step(self.countSt)
        self.listWidget.addItem('Компьтер взял - ' + str(x))
        self.countSt -= x
        self.lcdNumber.display(self.countSt)
        if self.countSt == 0:
            self.pBRun.setEnabled(False)
            self.label_msg.setText('Победа компьютера!')
        elif self.countSt < 3:
            self.spinBox_2.setMaximum(self.countSt)

    def step(self, x):
        if x < 8:
            if x < 4:
                return x
            elif x % 3 == 1:
                return 3
            elif x % 3 == 2:
                return 1
            else:
                return 2
        elif 8 < x < 12:
            if x % 3 == 2:
                return 3
            elif x % 3 == 1:
                return 2
            else:
                return 1
        else:
            if x % 3 == 2:
                return 2
            elif x % 3 == 1:
                return 1
            else:
                return 3


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
