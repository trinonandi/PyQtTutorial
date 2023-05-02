import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ScrollLabel(QScrollArea):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)
 
        # making widget resizable
        self.setWidgetResizable(True)
 
        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)
 
        # vertical box layout
        lay = QVBoxLayout(content)
 
        # creating label
        self.label = QLabel(content)
 
        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
 
        # making label multi-line
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)
 
        # adding label to the layout
        lay.addWidget(self.label)
 
    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)



class DialogApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.button = QPushButton('Import XML')
        self.button.clicked.connect(self.get_xml_file)
        self.textEditor = ScrollLabel(self)


        layout = QVBoxLayout()
        layout.addWidget(self.button, 1)
        layout.addWidget(self.textEditor, 9)

        self.setLayout(layout)

    def get_xml_file(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()
            if file_name[0].endswith('.xml'):
                with open(file_name[0], 'r') as f:
                    data = f.read()
                    self.textEditor.setText(data)
                    f.close()
            else:
                pass        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DialogApp()
    demo.show()
    sys.exit(app.exec_())


