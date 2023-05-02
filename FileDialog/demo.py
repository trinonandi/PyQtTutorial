import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QFileDialog, QVBoxLayout


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 400
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.options = ('Get File Name', 'Get File Names', 'Get Folder Dir', 'Save File Name')
        self.combo = QComboBox()
        self.combo.addItems(self.options)
        layout.addWidget(self.combo)

        btn = QPushButton('Launch')
        btn.clicked.connect(self.launch_dialog)
        layout.addWidget(btn)

    def launch_dialog(self):
        option = self.options.index(self.combo.currentText())

        match option:
            case 0:
                response = self.get_filename()
                print(response)
            case 1:
                response = self.get_filenames()
                print(response)
            case 2:
                response = self.get_folder_dir()
                print(response)
            case 3:
                response = self.get_save_filename()
            case _:
                print('Got Nothing')

    def get_filename(self):
        #cancel will return empty string
        file_filter = 'Data file (*.txt *csv *.xlsx *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileName(parent=self, caption='Select a file', directory=os.getcwd(), filter=file_filter, initialFilter='Data file (*.txt *csv *.xlsx *.dat)')
        return response[0]
    
    def get_filenames(self):
        # cancel will return empty list
        file_filter = 'Data file (*.txt *csv *.xlsx *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getOpenFileNames(parent=self, caption='Select a file', directory=os.getcwd(), filter=file_filter, initialFilter='Data file (*.txt *csv *.xlsx *.dat)')
        return response[0]
    
    def get_folder_dir(self):
        response = QFileDialog.getExistingDirectory(self, caption='Select a Folder')
        return response
    
    def get_save_filename(self):
        file_filter = 'Data file (*.txt *csv *.xlsx *.dat);; Excel File (*.xlsx *.xls)'
        response = QFileDialog.getSaveFileName(parent=self, caption='Select a file', directory='file_name.txt', filter=file_filter, initialFilter='Data file (*.txt *csv *.xlsx *.dat)')
        return response[0]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
            QWidget {
                font-size: 18px;
            }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
