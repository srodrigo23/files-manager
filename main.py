import sys

from PySide6 import QtCore, QtWidgets, QtGui
import PySide6.QtCore
from PySide6.QtWidgets import QPushButton, QGridLayout, QFileSystemModel, QTreeView, QHBoxLayout, QVBoxLayout

class MyPanel(QtWidgets.QWidget):

    def __init__(self, color="red") -> None:
        super().__init__()

        # self.resize(100, 100)
        # self.button = QtWidgets.QPushButton(text="Click me!")
        # self.text = QtWidgets.QLabel(
        #     text = "Hello World",
        #     alignment = QtCore.Qt.AlignCenter
        # )
        # self.setObjectName("siki")
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.layout = QtWidgets.QVBoxLayout(self)
        
        # self.layout.addWidget(self.button)
        # self.layout.addWidget(self.text)
        self.layout.addWidget(self.tree)
        # self.setStyleSheet(f"background-color: {color}")


class RightPanel(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        previewPanel = PreviewFilePanel()
        controlPanel = ControlPanel()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(previewPanel)
        self.layout.addWidget(controlPanel)


class PreviewFilePanel(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.preview = QtWidgets.QLabel(
            text = "Preview",
            alignment = QtCore.Qt.AlignCenter
        )
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.preview)


class ControlPanel(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.uploadButton = QtWidgets.QPushButton(text="Upload")
        self.uploadButton.setIcon(QtGui.QIcon('icons/upload.png'))

        self.deleteButton = QtWidgets.QPushButton(text="Delete")
        self.deleteButton.setIcon(QtGui.QIcon('icons/delete.png'))

        self.moveButton = QtWidgets.QPushButton(text="Move")
        self.moveButton.setIcon(QtGui.QIcon('icons/app.png'))
        # self.panel = QtWidgets.QWidget()
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.uploadButton)
        self.layout.addWidget(self.deleteButton)
        self.layout.addWidget(self.moveButton)
        # self.panel.setLayout(layout)
        # layout.addWidget(self.panel)

        # self.uploadButton = QtWidgets.QLabel(
        #     text = "Hello World",
        #     # alignment = QtCore.Qt.AlignCenter
        # )
        # self.layout = QtWidgets.QVBoxLayout(self)
        # layout.addWidget(self.panel)
        



class Main(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        # self.resize(800, 600)
        self.layout = QHBoxLayout(self)
        self.setWindowTitle("This is a test")
        self.setWindowIcon(QtGui.QIcon('icons/app.png'))
        self.panel1 = MyPanel()
        self.panel1.setObjectName("myPanel")

        self.rightPanel = RightPanel()
        self.rightPanel.setObjectName("panel2")

        # self.panel1.setStyleSheet("color: blue; background-color: yellow")
        # panel2.setStyleSheet("color: blue; background-color: yellow")

        self.layout.addWidget(self.panel1, stretch=1)
        self.layout.addWidget(self.rightPanel, stretch=1)
        
        # self.setStyleSheet("QWidget#panel1 { background-color: red }")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Main()
    sys.exit(app.exec())
