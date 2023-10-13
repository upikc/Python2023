from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

a = 1


class Mybtn(QPushButton):

    def __init__(self):
        super().__init__()
        global a
        self.font = QFont()
        self.font.setPointSize(19)
        self.setMinimumHeight(45)
        self.setText(str(a))
        self.setFont(self.font)
        a += 1


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    Dot = False

    def initUI(self):

        grid = QGridLayout()
        self.font = QFont()
        self.font.setPointSize(17)

        self.button1 = Mybtn()
        grid.addWidget(self.button1, 1, 0)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(1))
        self.button1 = Mybtn()
        grid.addWidget(self.button1, 1, 1)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(2))
        self.button1 = Mybtn()
        grid.addWidget(self.button1, 1, 2)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(3))

        self.button1 = Mybtn()
        grid.addWidget(self.button1, 2, 0)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(4))
        self.button1 = Mybtn()
        grid.addWidget(self.button1, 2, 1)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(5))
        self.button1 = Mybtn()
        grid.addWidget(self.button1, 2, 2)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(6))

        self.button1 = Mybtn()
        grid.addWidget(self.button1, 3, 0)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(7))
        self.button1 = Mybtn()
        grid.addWidget(self.button1, 3, 1)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(8))
        self.button1 = QPushButton("0")
        grid.addWidget(self.button1, 4, 1)
        self.button1.setMinimumHeight(45)
        self.button1.setFont(self.font)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(0))
        self.button1 = Mybtn()
        grid.addWidget(self.button1, 3, 2)
        self.button1.clicked.connect(lambda: self.BtnClikNumber(9))

        self.button2 = QPushButton("+")
        grid.addWidget(self.button2, 1, 4)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(lambda: self.BtnClikSign("+"))
        self.button2 = QPushButton("-")
        grid.addWidget(self.button2, 2, 4)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(lambda: self.BtnClikSign("-"))
        self.button2 = QPushButton("*")
        grid.addWidget(self.button2, 3, 4)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(lambda: self.BtnClikSign("*"))
        self.button2 = QPushButton("/")
        grid.addWidget(self.button2, 4, 4)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(lambda: self.BtnClikSign("/"))

        self.button2 = QPushButton("=")
        grid.addWidget(self.button2, 5, 0, 0, 3)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(lambda: self.end())

        self.button2 = QPushButton(".")
        grid.addWidget(self.button2, 4, 2)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(self.PresDot)

        self.button2 = QPushButton("C")
        grid.addWidget(self.button2, 4, 0)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(self.clear)

        vbox = QVBoxLayout()
        self.LCDNum = QLCDNumber()
        self.LCDNum.setMinimumHeight(100)

        self.font.setPointSize(10)
        self.TexSign = QLabel("")
        self.TexSign.setFont(self.font)
        self.TexSign.autoFillBackground()
        self.TexSign.setMaximumHeight(12)

        self.button2 = QPushButton("???")
        grid.addWidget(self.button2, 5, 4)
        self.button2.setMinimumHeight(45)
        self.button2.setFont(self.font)
        self.button2.clicked.connect(lambda: print(str(self.LCDNum.value())))

        vbox.addWidget(self.TexSign)
        vbox.addWidget(self.LCDNum)
        vbox.addLayout(grid)

        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Cal')
        self.show()

    def BtnClikNumber(self, value):
        print(str(float(self.LCDNum.value())) + "  " + str(float(int(self.LCDNum.value()))))
        if self.Dot:
            self.LCDNum.display(self.LCDNum.value() + value / 10)
            self.Dot = False
        else:
            if float(int(self.LCDNum.value())) == float(self.LCDNum.value()):
                print("true")
                self.LCDNum.display(self.LCDNum.value() * 10 + value)
            else:
                print("false")
                self.LCDNum.display(str(self.LCDNum.value()) + str(value))

    def BtnClikSign(self, Sign):
        self.FNumber = self.LCDNum.value()
        self.TexSign.setText(self.TexSign.text()+str(self.FNumber) + Sign)
        self.Reply = True
        self.LCDNum.display(0)
        self.Dot=False

    def clear(self):
        self.LCDNum.display("")
        self.Reply = True
        self.TexSign.setText("")

    def PresDot(self):
        self.LCDNum.display(str(self.LCDNum.value()))
        self.Dot = True

    Reply = True

    def end(self):

        if self.LCDNum.value() != 0 and self.TexSign.text() and self.Reply:
            boof = str(self.LCDNum.value())
            try:
                self.LCDNum.display(eval(self.TexSign.text() + str(self.LCDNum.value())))
            except ZeroDivisionError:
                self.TexSign.setText("")    
                self.LCDNum.display("eror")
                return
            self.TexSign.setText(self.TexSign.text() + boof + " =")
            self.Reply = False

            print(self.TexSign.text() + " " + str(self.LCDNum.value()))
        else:
            self.LCDNum.display("eror")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
