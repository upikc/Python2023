import sys
from PyQt5.QtWidgets import QApplication, QWidget , QPushButton
import random


class MyBtn(QPushButton):
    def __init__(self):
        super().__init__()

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.InstAll()

    def InstAll(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('bebra')
        self.buttons = []

        for i in range(5):
            button = QPushButton(self)
            button.resize(50, 50)
            button.setText(str(i))
            button.move(random.randint(0, 250), random.randint(0, 250))
            self.buttons.append(button)

        def clik(self, qwe):
            print(qwe)

        self.buttons[0].clicked.connect(lambda: self.clik(0))
        self.buttons[1].clicked.connect(lambda: self.clik(1))
        self.buttons[2].clicked.connect(lambda: self.clik(2))
        self.buttons[3].clicked.connect(lambda: self.clik(3))
        self.buttons[4].clicked.connect(lambda: self.clik(4))

        self.window()
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())