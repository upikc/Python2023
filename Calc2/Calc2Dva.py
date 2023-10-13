import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

MyFont = QFont("Arial", 30)
numb1 = 0
WriteSign = "+"
AfterDot = 6


class MyBtn(QPushButton):
    def __init__(self, char):
        super().__init__()
        self.setText(str(char))
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.setFont(MyFont)


class BtnNumber(MyBtn):
    def __init__(self, Numb):
        super().__init__(Numb)
        self.clicked.connect(lambda: self.NumberClik(self.text()))

    def NumberClik(self, BtnText_NUMB):
        TextLine.setText(TextLine.text() + BtnText_NUMB)


class otherBtn(MyBtn):
    def BtnC(self):
        TextLine.setText("")
        numb1 = 0

    def BtnEntrSignСhange(self, sign):
        if TextLine.text().replace(".", "", 1).isnumeric() and TextLine.text()[-1] != ".":
            TextLine.setText(TextLine.text() + sign)
            global WriteSign
            WriteSign = sign

    def DotPress(self):
        if TextLine.text().isnumeric():
            TextLine.setText(TextLine.text() + ".")
        else:
            if TextLine.text().find(WriteSign) == "-1":
                INDX = False
            else:
                INDX = True
            if TextLine.text().rfind(".") < TextLine.text().find(WriteSign) and INDX and TextLine.text()[
                -1].isnumeric():
                TextLine.setText(TextLine.text() + ".")

    def OneNumbOper(self, Oper):
        if TextLine.text()[-1] != "." and TextLine.text().replace(".", "").isnumeric():
            # начало вычислений
            match Oper:
                case "sin":
                    TextLine.setText(str(round(math.sin(float(TextLine.text())), AfterDot)))
                case "cos":
                    TextLine.setText(str(round(math.cos(float(TextLine.text())), AfterDot)))
                case "tan":
                    TextLine.setText(str(round(math.tan(float(TextLine.text())), AfterDot)))
                case "²":
                    TextLine.setText(str(float(TextLine.text()) * float(TextLine.text())))

    def СплитПриколДляРовно(self, text, Sign):
        return text.split(Sign)

    def РовноКнопка(self):
        if TextLine.text().find(WriteSign) != -1 and TextLine.text()[-1].isnumeric():
            ExitSplit = self.СплитПриколДляРовно(TextLine.text(), WriteSign)
            match WriteSign:
                case "-":
                    TextLine.setText(str(round(float(ExitSplit[0]) - float(ExitSplit[1]), AfterDot)))
                case "+":
                    TextLine.setText(str(round(float(ExitSplit[0]) + float(ExitSplit[1]), AfterDot)))
                case "/":
                    if float(ExitSplit[1]) != 0:
                        TextLine.setText(str(round(float(ExitSplit[0]) / float(ExitSplit[1]), AfterDot)))
                case "*":
                    TextLine.setText(str(round(float(ExitSplit[0]) * float(ExitSplit[1]), AfterDot)))
                case "^":
                    TextLine.setText(str(round(float(ExitSplit[0]) ** float(ExitSplit[1]), AfterDot)))
                case "√":
                    TextLine.setText(str(round(float(ExitSplit[0]) ** (1 / float(ExitSplit[1])), AfterDot)))

    def __init__(self, char):
        super().__init__(char)
        match char:
            case "C":
                self.clicked.connect(lambda: self.BtnC())
            case "←":
                self.clicked.connect(lambda: TextLine.setText(TextLine.text()[0: -1: 1]))
            case "-" | "+" | "/" | "*" | "^" | "√":
                self.clicked.connect(lambda: self.BtnEntrSignСhange(char))
            case "=":
                self.clicked.connect(lambda: self.РовноКнопка())
                pass
            case ".":
                self.clicked.connect(lambda: self.DotPress())
            case "sin" | "cos" | "tan" | "²":
                self.clicked.connect(lambda: self.OneNumbOper(char))


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.InsAll()
        self.show()

    def InsAll(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 300)

        BtnLayout = QGridLayout()

        global TextLine
        TextLine = QLineEdit()
        TextLine.setFont(MyFont)
        BtnLayout.addWidget(TextLine, 0, 0, 1, 6)

        for i in range(10):
            BtnLayout.addWidget(BtnNumber(i), i // 3 + 1, i % 3)

        BtnLayout.addWidget(otherBtn("."), 4, 1)
        BtnLayout.addWidget(otherBtn("C"), 1, 3)
        BtnLayout.addWidget(otherBtn("←"), 2, 3)
        BtnLayout.addWidget(otherBtn("="), 4, 2)

        BtnLayout.addWidget(otherBtn("√"), 1, 4)
        BtnLayout.addWidget(otherBtn("^"), 1, 5)

        BtnLayout.addWidget(otherBtn("sin"), 2, 4)
        BtnLayout.addWidget(otherBtn("cos"), 2, 5)
        BtnLayout.addWidget(otherBtn("tan"), 3, 5)
        BtnLayout.addWidget(otherBtn("²"), 4, 5)

        for sign in range(4):
            BtnLayout.addWidget(otherBtn(("+", "-", "*", "/")[sign]), 3 + sign // 2, 3 + sign % 2)

        self.setLayout(BtnLayout)


app = QApplication(sys.argv)
Calc = Calc()
sys.exit(app.exec_())
