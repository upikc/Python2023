import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from tkinter.messagebox import *
from time import *
from qt_material import apply_stylesheet

txt = open('text.txt', 'r+', encoding="utf8")
txt123 = txt.readlines()
if txt123 == "\n" or "":
    txt.write("\n\n")

class mainn(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350,250)
        self.setMinimumHeight(150)
        self.setMinimumWidth(250)
        self.setMaximumWidth(400)
        self.setMaximumHeight(250)
        self.setWindowTitle("вход")
        mainlay = QtWidgets.QVBoxLayout()
        labellay = QtWidgets.QVBoxLayout()

        label1 = QtWidgets.QLineEdit(self)
        label2 = QtWidgets.QLineEdit(self)

        labellay.addWidget(QtWidgets.QLabel())
        labellay.addWidget(label1)
        labellay.addWidget(QtWidgets.QLabel())
        labellay.addWidget(label2)
        labellay.addWidget(QtWidgets.QLabel())


        buttonlay = QtWidgets.QHBoxLayout()
        btn1 = QtWidgets.QPushButton("войти")
        btn2 = QtWidgets.QPushButton("регистрация")



        buttonlay.addWidget(btn1)
        buttonlay.addWidget(QtWidgets.QLabel())
        buttonlay.addWidget(btn2)

        mainlay.addLayout(labellay)
        mainlay.addLayout(buttonlay)
        self.setLayout(mainlay)

        btn1.clicked.connect(lambda: self.enter(label1.text(), label2.text()))
        btn2.clicked.connect(self.btn2_clc)

    def enter(self, a, b):
        a = a.strip()
        b = b.strip()
        print(a)
        print(b)

        if a == "" or b =="":
            QtWidgets.QMessageBox.about(self, "ошибка", "!! поля не могут быть пусты !!")
        elif " " in a or " " in b:
            QtWidgets.QMessageBox.about(self, "ошибка", "!! логин и пароль не могут содержать пробелы !!")
        else:
            txt = open('text.txt', 'r+', encoding="utf8")
            txt1 = txt.read().splitlines()
            buf = True
            for i in range(len(txt1)):
                if txt1[i] == a and txt1[i+1] ==b:
                    # QtWidgets.QMessageBox.about(self, "поздравляю", f"!! ваш логин: {txt1[i]} !!\n !! ваш пароль: {txt1[i+1]} !!")
                    buf = False
                    break
            if buf:
                QtWidgets.QMessageBox.about(self, "ошибка", "такого пользователя нет")
            else:
                self.window3 = mainn3()
                self.window3.show()
                
            txt.close()


    def btn2_clc(self):
        self.hide()
        self.window2 = mainn2()
        self.window2.show()




class mainn2(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350, 250)
        self.setMinimumHeight(150)
        self.setMinimumWidth(250)
        self.setMaximumWidth(400)
        self.setMaximumHeight(250)
        self.setWindowTitle("регистрация")
        mainlay = QtWidgets.QVBoxLayout()

        labellay = QtWidgets.QVBoxLayout()
        label3 = QtWidgets.QLineEdit()
        label4 = QtWidgets.QLineEdit()
        labellay.addWidget(QtWidgets.QLabel())

        labellay.addWidget(label3)
        labellay.addWidget(QtWidgets.QLabel())
        labellay.addWidget(label4)
        labellay.addWidget(QtWidgets.QLabel())

        buttonlay = QtWidgets.QHBoxLayout()

        btn3 = QtWidgets.QPushButton("регистрация")
        btn4 = QtWidgets.QPushButton("назад")
        buttonlay.addWidget(btn4)
        buttonlay.addWidget(QtWidgets.QLabel())
        buttonlay.addWidget(btn3)

        mainlay.addLayout(labellay)
        mainlay.addLayout(buttonlay)
        self.setLayout(mainlay)
        btn3.clicked.connect(lambda: self.reg(label3.text(), label4.text()))
        btn4.clicked.connect(self.back)
    def back(self):
        self.close()
        window = mainn()
        window.show()
    # ???????????????????


    def reg(self, a, b):

        a = a.strip()
        b = b.strip()

        if a == "" or b =="":
            QtWidgets.QMessageBox.about(self, "ошибка", "!! поля не могут быть пусты !!")
        elif " " in a or " " in b:
            QtWidgets.QMessageBox.about(self, "ошибка", "!! логин и пароль не могут содержать пробелы !!")
        # elif a in
        else:
            txt = open('text.txt', 'r+', encoding="utf8")
            txtlist = txt.readlines()
            abuf = a + "\n"
            print(3)
            bull = True
            for i in range(len(txtlist)):
                if txtlist[i] == abuf and txtlist[i-1] == "\n":
                    QtWidgets.QMessageBox.about(self, "ошибка", "такой пользователь уже есть")
                    bull = False

                    break
            if bull:
                print(2)
                txt.write(f"\n{a}\n{b}\n")
                QtWidgets.QMessageBox.about(self, "поздравляю", "вы успешно зарегистрированы")
                self.close()
                txt.close()
                window = mainn()
                window.show()

class mainn3(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 100)
        self.setMinimumHeight(150)
        self.setMinimumWidth(250)
        self.setMaximumWidth(400)
        self.setMaximumHeight(250)
        self.setWindowTitle("вы вошли")
        print("weqwe")
        mainlay = QtWidgets.QVBoxLayout()
        labellay = QtWidgets.QVBoxLayout()

        label1 = QtWidgets.QLineEdit(self)
        label2 = QtWidgets.QLineEdit(self)
        label1.setText("boba")
        label2.setText("sheli")
        labellay.addWidget(QtWidgets.QLabel())
        labellay.addWidget(label1)
        labellay.addWidget(QtWidgets.QLabel())
        labellay.addWidget(label2)
        labellay.addWidget(QtWidgets.QLabel())
        mainlay.addLayout(labellay)
        print("qweewq")
        self.setLayout(mainlay)
        print("qweewq")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='Dark_lightgreen.xml')
    window = mainn()
    window.show()
    app.exec()