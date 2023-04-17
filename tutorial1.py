from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 500, 300) # xcoord, ycoord, height, width
    win.setWindowTitle("Test")

    #creating a label
    label = QtWidgets.QLabel(win)
    label.setText("Text")
    label.move(450, 250)

    win.show()
    sys.exit(app.exec_())   # for the cross button to work


window()