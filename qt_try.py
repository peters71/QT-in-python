from PyQt5.QtWidgets import QApplication,QWidget,QLCDNumber,QDesktopWidget,QVBoxLayout
import time,sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()
    def update_time(self):
        self.lcd.display(time.strftime("%X",time.localtime()))
    def init_timer(self):
        self.timer=QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)
    def initUI(self):
        self.resize(250,150)
        self.setWindowTitle("三丫的电子时钟")
        self.move_center()
        self.lcd=QLCDNumber()
        self.lcd.setDigitCount(10)
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(time.strftime("%X",time.localtime()))

        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.lcd)
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.main_layout)

        self.main_p=QPalette()
        self.main_p.setColor(QPalette.Background,Qt.darkGray)
        self.setAutoFillBackground(True)
        self.setPalette(self.main_p)

        self.show()
    def move_center(self):
        m_rect=self.frameGeometry()
        w_center_point=QDesktopWidget().availableGeometry().center()
        m_rect.moveCenter(w_center_point)
        self.move(m_rect.topLeft())


if __name__=='__main__':
    app=QApplication(sys.argv)
    m_time=MyTime()

    sys.exit(app.exec_())
