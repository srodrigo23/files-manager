import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QPushButton, QGridLayout

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton(text="Click me!")
        self.text = QtWidgets.QLabel(
            text="Hello World",
            alignment=QtCore.Qt.AlignCenter
        )
        self.resize(800, 600)
        # self.layout = QtWidgets.QVBoxLayout(self)

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")


        layout = QGridLayout(self)
        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 1, 0, 1, 2)
        layout.addWidget(button4, 2, 0)
        layout.addWidget(button5, 2, 1)

        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)

        self.setWindowIconText('Testing')
        self.setWindowIcon(QtGui.QIcon('icons/app.png'))
        self.button.clicked.connect(self.magic)
        self.button.setIcon(QtGui.QIcon('icons/app.png'))
        # self.setGeometry(300, 300, 300, 200)
        self.show()

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    # widget.resize(800, 600)
    # widget.show()
    sys.exit(app.exec())