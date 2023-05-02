import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import os

class FileSystemView(QWidget):
    def __init__(self, dir_path):
        super().__init__()
        app_width = 800
        app_height = 300

        self.setWindowTitle('File System Viewer')
        self.setGeometry(300, 300, app_width, app_height)

        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)
        
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dir_path))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.context_menu)
        
        layout = QVBoxLayout()
        layout.addWidget(self.tree)

        self.setLayout(layout)

    def context_menu(self):
        menu = QMenu()
        open = menu.addAction("Open")
        open.triggered.connect(self.open_file)
        cursor = QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.tree.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dirpath = r'C:\Users\tnandi\Desktop\PyQt'
    demo = FileSystemView(dirpath)
    demo.show()
    sys.exit(app.exec_())