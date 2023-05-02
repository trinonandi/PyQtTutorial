import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTabWidget, QGridLayout, QVBoxLayout


class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        main_layout = QGridLayout()
        v_layout1 = QVBoxLayout()

        # Tab 1.1
        self.tab1_1 = QWidget()
        self.tab1_1.layout = QVBoxLayout()
        self.tab1_1.layout.addWidget(QLabel('<font size=8><b>Type Something</font>'))

        self.line_edit = QLineEdit()
        self.btn_print = QPushButton('Print')
        self.btn_print.clicked.connect(self.type_something)
        self.tab1_1.layout.addWidget(self.line_edit)
        self.tab1_1.layout.addWidget(self.btn_print)

        self.tab1_1.setLayout(self.tab1_1.layout)

        # Tab 1.2
        self.btn = QPushButton('A Button')
        self.btn.clicked.connect(lambda: print('Hello world'))

        self.tab1_2 = QWidget()
        self.tab1_2.layout = QVBoxLayout()
        self.tab1_2.layout.addWidget(self.btn)
        self.tab1_2.setLayout(self.tab1_2.layout)

        # Tab 1 Parent 
        self.tabs1 = QTabWidget()
        self.tabs1.addTab(self.tab1_1, 'Tab 1.1')
        self.tabs1.addTab(self.tab1_2, 'Tab 1.2')

        #Tab 2 Parent
        self.btn2 = QPushButton('B Button')
        self.btn2.clicked.connect(lambda: print('B Button Clicked'))
        self.tabs2 = QTabWidget()
        self.tabs2.addTab(self.btn2, 'Tab 2')

        main_layout.addWidget(self.tabs1, 0, 0)
        main_layout.addWidget(self.tabs2, 0, 1) 
        self.setLayout(main_layout)
    
    
    def type_something(self):
        print(self.line_edit.text())


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec_())