from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class EnterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("чурка")

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Создадим виджет и сохраним ссылку на него
        self.dialog = EnterWindow()
        self.dialog.resize(200, 200)

        self.button_show = QPushButton('Show')
        self.button_show.clicked.connect(self.show_dialog)

        self.button_hide = QPushButton('Hide')
        self.button_hide.clicked.connect(self.hide_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.button_show)
        layout.addWidget(self.button_hide)
        layout.addStretch()

        self.setLayout(layout)

    def show_dialog(self):
        self.dialog.show()

    def hide_dialog(self):
        self.dialog.hide()


class Dialog(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    app = QApplication([])

    w = MainWidget()
    w.resize(200, 100)
    w.show()

    app.exec()
