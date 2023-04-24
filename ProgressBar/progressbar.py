import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer

class ProgressBarDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40 ,200 ,25)

        self.start_btn = QPushButton('Start', self)
        self.start_btn.move(30, 80)
        self.start_btn.clicked.connect(self.startProgress)

        self.reset_btn = QPushButton('Reset', self)
        self.reset_btn.move(120, 80)
        self.reset_btn.clicked.connect(self.resetBar)

        self.timer = QBasicTimer()
        self.step = 0


    def resetBar(self):
        self.step = 0
        self.progress_bar.setValue(0)
    
    def startProgress(self):
        if self.timer.isActive():
            self.timer.stop()
            self.start_btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.start_btn.setText('Stop')

    
    def timerEvent(self, event):
        if self.step >= 100:
            self.timer.stop()
            self.start_btn.setText('Start')
            return
        
        self.step += 1
        self.progress_bar.setValue(self.step)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ProgressBarDemo()
    demo.show()
    sys.exit(app.exec_())