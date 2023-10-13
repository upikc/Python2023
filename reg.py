import sys
import time

from PyQt5.QtWidgets import *
from tkinter.messagebox import showerror, showwarning, showinfo

class EnterWindow(QWidget):
    def __init__(self , log , pas):
        super().__init__()
        self.setWindowTitle("чвк редан")
        self.lab = QTextEdit(self)
        self.lab.setGeometry(0 , 0 , 200 ,200)
        self.lab.setText("ваш логин: "+log + "\nваш пароль: " + pas)

class Window(QWidget):
    def __init__(self, SinWork , RegWork):
        super().__init__()
        self.SinWork = SinWork
        self.RegWork = RegWork
        if RegWork:
            self.setWindowTitle("reg")
        self.Desi()
        self.CharBan = []
        for i in range(ord('а'), ord('я')+1):
            self.CharBan.append(chr(i))
        self.CharBan.append("ё")
        self.CharBan.append(" ")
        print(self.CharBan)



    def Desi(self):
        self.setFixedSize(200 , 250)

        self.REGtext = QLabel(self)
        self.REGtext.move(20,20)
        self.REGtext.setText("логин")

        self.REGline = QLineEdit(self)
        self.REGline.move(20,50)

        self.REGtext = QLabel(self)
        self.REGtext.move(20, 80)
        self.REGtext.setText("пароль")

        self.LOGline = QLineEdit(self)
        self.LOGline.move(20, 110)


        self.BtnReg = QPushButton(self)
        self.BtnReg.setText("регистрация")
        self.BtnReg.move(20 , 200)
        self.BtnReg.clicked.connect(self.register)

        if self.SinWork:
            self.BtnLog = QPushButton(self)
            self.BtnLog.setText("вход")
            self.BtnLog.move(20, 170)
            self.BtnLog.clicked.connect(self.login)

    def login(self):
        BoolEnter = True
        file = open("xxx.txt",encoding="utf-8")
        for line in file:
            if line == (self.REGline.text() + " " + self.LOGline.text())+"\n":
            #if line[:line.find(" "):] ==  self.REGline.text() and line[line.find(" ")+1:-1:]  == self.LOGline.text():
                print("вы зашли")
                BoolEnter = False
                showinfo("", "ВЫ ЗАШЛИ")
                self.Ewin = EnterWindow(self.REGline.text() , self.LOGline.text())
                self.Ewin.show()
                self.Ewin.setFixedSize(200, 250)
                break;
        if BoolEnter:
            showerror("", "не верные данные")
        file.close()




    def register(self):


        if self.RegWork:
            bool = True
            for RegChar in self.REGline.text():
                if RegChar in self.CharBan:
                    bool = False
                    showerror("", "без кирилицы и пробелов в пароле")
                    return
            for LOGChar in self.LOGline.text():
                if LOGChar in self.CharBan:
                    bool = False
                    showerror("", "без кирилицы и пробелов в логине")
                    return
            if self.REGline.text() == "" or self.LOGline.text() == "":
                bool = False
                showwarning("", "пустные поля")
            file = open("xxx.txt", "r",encoding="utf-8")
            for line in file:
                #print(self.REGline.text() + " ")
                #print(line[:line.find(" ")+1 :])
                if (self.REGline.text()+" ") == line[:line.find(" ")+1 :]:
                    bool = False
                    showerror("", "такой логин уже существует")
                    break
            file.close()
            if bool:
                file = open("xxx.txt" ,"a",encoding="utf-8")
                file.write('\n' + self.REGline.text()+ " " + self.LOGline.text()+"\n")
                showinfo("" , "вы успешно зарегались")
                file.close()
                self.Mainf = Window(True , False)
                self.Mainf.show()
                self.close()
        else:
            self.RegForm = Window(False , True)
            self.RegForm.show()
            self.close()

def start():
    app = QApplication(sys.argv)
    win = Window(True , False) #логин / регистер
    win.setWindowTitle("log")
    win.show()
    sys.exit(app.exec_())

start()