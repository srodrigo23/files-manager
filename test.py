import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QGridLayout)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(800, 600)
        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")


        # layout = QGridLayout(self)
        self.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 1, 0, 1, 2)
        layout.addWidget(button4, 2, 0)
        layout.addWidget(button5, 2, 1)

        # self.setLayout(layout)
        

        # self.button = QPushButton("My Button", self)
        # self.button.clicked.connect(self.handleButton)
        # self.setWindowIconText("send me a q       ")
        # self.setWindowIcon(QIcon('icons/app.png'))
        self.show()



    def handleButton(self):
        self.button.setText("Ready")

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    # mainWindow.show()
    sys.exit(app.exec())