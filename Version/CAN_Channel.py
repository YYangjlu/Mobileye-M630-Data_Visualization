import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle

class CAN_Channel(QDialog):
    '''
    Signal_Save:点击保存按钮的信号；
    Signal_Cancel：点击取消保存按钮的信号
    '''
    Signal_Save = pyqtSignal()
    Signal_Cancel = pyqtSignal()
    def __init__(self,parent=None):
        super(CAN_Channel, self).__init__(parent)
        self.SetUI()

    def SetUI(self):
        self.resize(400,50)
        self.setWindowTitle("CAN SETTING")
        self.Font = QFont()
        self.Font.setPixelSize(18)
        self.FixedHeight = 30

        self.Channel_Label = QLabel('CAN CHANNEL')
        self.Channel_Label.setFont(self.Font)
        self.Timer0_Label = QLabel('TIMER0')
        self.Timer0_Label.setFont(self.Font)
        self.Timer1_Label = QLabel('TIMER1')
        self.Timer1_Label.setFont(self.Font)

        self.Channel_Line = QLineEdit()
        self.Channel_Line.setText('0')
        self.Channel_Line.setFont(self.Font)
        self.Timer0_Line = QLineEdit()
        self.Timer0_Line.setText('0x00')
        self.Timer0_Line.setFont(self.Font)
        self.Timer1_Line = QLineEdit()
        self.Timer1_Line.setText('0x1c')
        self.Timer1_Line.setFont(self.Font)

        self.VB_Label = QVBoxLayout()
        self.VB_Label.addWidget(self.Channel_Label)
        self.VB_Label.addWidget(self.Timer0_Label)
        self.VB_Label.addWidget(self.Timer1_Label)

        self.VB_Line = QVBoxLayout()
        self.VB_Line.addWidget(self.Channel_Line)
        self.VB_Line.addWidget(self.Timer0_Line)
        self.VB_Line.addWidget(self.Timer1_Line)

        self.HB = QHBoxLayout()
        self.HB.addLayout(self.VB_Label)
        self.HB.addLayout(self.VB_Line)

        self.Save = QPushButton('Save and Open')
        self.Save.setFixedHeight(self.FixedHeight)
        self.Cancel = QPushButton('Reset')
        self.Cancel.setFixedHeight(self.FixedHeight)
        self.HB_Button = QHBoxLayout()
        self.HB_Button.addWidget(self.Save)
        self.HB_Button.addWidget(self.Cancel)

        self.VB = QVBoxLayout()
        self.VB.addLayout(self.HB)
        self.VB.addLayout(self.HB_Button)

        self.setLayout(self.VB)

        self.Save.clicked.connect(self.Save_signal)
        self.Cancel.clicked.connect(self.Cancel_signal)

    def Save_signal(self):
        self.Signal_Save.emit()

    def Cancel_signal(self):
        self.Signal_Cancel.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Mainwindow = CAN_Channel()
    Mainwindow.show()
    sys.exit(app.exec_())



