import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QMainWindow , QPushButton , QGridLayout )





class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()







        self.setWindowTitle("название")
        self.setGeometry(400, 400, 600, 400)


        self.Label1 = QtWidgets.QLabel(self)
        self.Label1.setText("текст")
        self.Label1.move(50, 100)
        self.Label1.adjustSize()


        self.btn = QPushButton(self)
        self.btn.move(50, 123)
        self.btn.setText("кнопка")
        self.btn.clicked.connect(lambda: self.BtnClick("123"))






    def BtnClick(self , i):
        print(i)

##############################################

def application():
    app = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(app.exec_())

application()
