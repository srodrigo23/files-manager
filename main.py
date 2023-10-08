import sys

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import QDir
from PySide6.QtWidgets import QPushButton, QGridLayout, QFileSystemModel, QTreeView, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPicture, QPixmap
class FilesExplorerPanel(QtWidgets.QWidget):

    def __init__(self, color="green") -> None:
        super().__init__()
        self.path = '/Users/sergiorodrigo'
        self.text = QtWidgets.QLabel(
            # text = QDir.currentPath(),
            text=self.path,
            alignment = QtCore.Qt.AlignCenter
        )
        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(self.path))
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setColumnHidden(1, True)
        self.tree.setColumnHidden(2, True)
        self.tree.setColumnHidden(3, True)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.tree)
        
        # self.setStyleSheet(f"background-color: {color}")

class SidePanel(QtWidgets.QWidget):

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
        self.preview.setPixmap(
            QPixmap('icons/media/audio/mp3.png')\
                .scaled(128, 128, 
                    QtCore.Qt.KeepAspectRatio
                )
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
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addWidget(self.uploadButton)
        self.layout.addWidget(self.deleteButton)
        self.layout.addWidget(self.moveButton)


class Main(QtWidgets.QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.layout = QHBoxLayout(self)
        # self.resize(800, 400)
        self.setWindowTitle("Files Manager")
        self.setWindowIcon(QtGui.QIcon('icons/app.png'))
        self.filesExplorerPanel = FilesExplorerPanel()
        # self.panel1.setObjectName("myPanel")

        self.sidePanel = SidePanel()
        # self.rightPanel.setObjectName("panel2")

        # self.panel1.setStyleSheet("color: blue; background-color: yellow")
        # panel2.setStyleSheet("color: blue; background-color: yellow")

        self.layout.addWidget(self.filesExplorerPanel, stretch=1)
        self.layout.addWidget(self.sidePanel, stretch=2)
        
        # self.setStyleSheet("QWidget#panel1 { background-color: red }")
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Main()
    sys.exit(app.exec())
