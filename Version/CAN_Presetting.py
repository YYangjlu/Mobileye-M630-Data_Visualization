import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import qdarkstyle

class CAN_Presetting(QWidget):
    '''
    Signal_load_BDC：加载DBC文件按钮信号；
    Signal_Ini_CAN：初始CAN设别按钮信号；
    Signal_Close_CAN：关闭CAN设备按钮信号；
    Signal_Ped_Show：画行人图像按钮信号；
    Signal_Veh_Show：画车辆图像按钮信号；
    Signal_Lane_Show：画车道线按钮信号；
    Signal_Save_Data：保存CAN数据；
    Signal_Clear_Show：清除所有图像按钮信号；
    '''
    Signal_load_BDC = pyqtSignal()
    Signal_Ini_CAN = pyqtSignal()
    Signal_Close_CAN = pyqtSignal()
    Signal_Ped_Show = pyqtSignal()
    Signal_Veh_Show = pyqtSignal()
    Signal_Lane_Show = pyqtSignal()
    Signal_Clear_Show = pyqtSignal()
    Signal_Record_Data = pyqtSignal()
    Signal_Save_Data = pyqtSignal()
    Signal_Record_Video = pyqtSignal()
    Signal_Save_Video = pyqtSignal()
    Signal_Open_Vedio = pyqtSignal()
    Signal_Close_Vedio = pyqtSignal()

    def __init__(self,parent=None):
        super(CAN_Presetting, self).__init__(parent)
        self.SetUI()

    def SetUI(self):
        self.setWindowTitle("PRE SETTING")
        self.resize(700,250)
        self.Font = QFont()
        self.Font.setPixelSize(20)
        self.FixedHeight = 30

        self.Load_DBC = QPushButton('LOAD DBC')
        self.Load_DBC.setFixedHeight(self.FixedHeight)
        self.Line_Load_DBC = QLineEdit()
        self.Line_Load_DBC.setEnabled(False)
        self.Line_Load_DBC.setFont(self.Font)

        self.Ini_CAN = QPushButton('INITIAL CAN')
        self.Ini_CAN.setFixedHeight(self.FixedHeight)
        self.Line_Ini_CAN = QLineEdit()
        self.Line_Ini_CAN.setEnabled(False)
        self.Line_Ini_CAN.setFont(self.Font)

        self.Close_CAN = QPushButton('CLOSE CAN')
        self.Close_CAN.setFixedHeight(self.FixedHeight)
        self.Line_Close_CAN = QLineEdit('CAN DEVICE NOT OPEN')
        self.Line_Close_CAN.setEnabled(False)
        self.Line_Close_CAN.setFont(self.Font)

        self.Button = QVBoxLayout()
        self.Button.addWidget(self.Load_DBC)
        self.Button.addWidget(self.Ini_CAN)
        self.Button.addWidget(self.Close_CAN)

        self.Line = QVBoxLayout()
        self.Line.addWidget(self.Line_Load_DBC)
        self.Line.addWidget(self.Line_Ini_CAN)
        self.Line.addWidget(self.Line_Close_CAN)

        self.HB = QHBoxLayout()
        self.HB.addLayout(self.Line)
        self.HB.addLayout(self.Button)

        self.Ped_Show = QPushButton('PEDESTIAN FIGURE')
        self.Ped_Show.setFixedHeight(self.FixedHeight)

        self.Veh_Show = QPushButton('VEHICLE FIGURE')
        self.Veh_Show.setFixedHeight(self.FixedHeight)

        self.Lane_Show = QPushButton('LANE FIGURE')
        self.Lane_Show.setFixedHeight(self.FixedHeight)

        self.Clear_Show = QPushButton('CLEAR ALL FIGURES')
        self.Clear_Show.setFixedHeight(self.FixedHeight)

        self.Record_Data = QPushButton('RECORE DATA')
        self.Record_Data.setFixedHeight(self.FixedHeight)

        self.Save_Data = QPushButton('SAVE DATA')
        self.Save_Data.setFixedHeight(self.FixedHeight)

        self.Open_Video = QPushButton("OPEN VIDEO")
        self.Open_Video.setFixedHeight(self.FixedHeight)

        self.Close_Video = QPushButton("CLOSE VIDEO")
        self.Close_Video.setFixedHeight(self.FixedHeight)

        self.Record_Video = QPushButton("RECORD VIDEO")
        self.Record_Video.setFixedHeight(self.FixedHeight)

        self.Save_Video = QPushButton("SAVE VIDEO")
        self.Save_Video.setFixedHeight(self.FixedHeight)

        self.HB_Show1 = QHBoxLayout()
        self.HB_Show1.addWidget(self.Ped_Show)
        self.HB_Show1.addWidget(self.Veh_Show)
        self.HB_Show1.addWidget(self.Lane_Show)
        self.HB_Show1.addWidget(self.Clear_Show)

        self.HB_Show2 = QHBoxLayout()
        self.HB_Show2.addWidget(self.Record_Data)
        self.HB_Show2.addWidget(self.Save_Data)
        self.HB_Show2.addWidget(self.Open_Video)
        self.HB_Show2.addWidget(self.Close_Video)
        self.HB_Show2.addWidget(self.Record_Video)
        self.HB_Show2.addWidget(self.Save_Video)

        self.VB_Total = QVBoxLayout()
        self.VB_Total.addLayout(self.HB)
        self.VB_Total.addLayout(self.HB_Show1)
        self.VB_Total.addLayout(self.HB_Show2)

        self.setLayout(self.VB_Total)

        self.Load_DBC.clicked.connect(self._DBC_Path_Signal)
        self.Ini_CAN.clicked.connect(self._Ini_CAN_Signal)
        self.Close_CAN.clicked.connect(self._Close_CAN_Signal)
        self.Ped_Show.clicked.connect(self._Ped_Show_Signal)
        self.Veh_Show.clicked.connect(self._Veh_Show_Signal)
        self.Lane_Show.clicked.connect(self._Lane_Show_Signal)
        self.Clear_Show.clicked.connect(self._Clear_Show)
        self.Record_Data.clicked.connect(self._Record_Data)
        self.Save_Data.clicked.connect(self._Save_Data)
        self.Record_Video.clicked.connect(self._Record_Video)
        self.Save_Video.clicked.connect(self._Save_Video)
        self.Open_Video.clicked.connect(self._Open_Vedio)
        self.Close_Video.clicked.connect(self._Close_Vedio)


    def _DBC_Path_Signal(self):
        self.Signal_load_BDC.emit()

    def _Ini_CAN_Signal(self):
        self.Signal_Ini_CAN.emit()

    def _Close_CAN_Signal(self):
        self.Signal_Close_CAN.emit()

    def _Ped_Show_Signal(self):
        self.Signal_Ped_Show.emit()

    def _Veh_Show_Signal(self):
        self.Signal_Veh_Show.emit()

    def _Lane_Show_Signal(self):
        self.Signal_Lane_Show.emit()

    def _Clear_Show(self):
        self.Signal_Clear_Show.emit()

    def _Record_Data(self):
        self.Signal_Record_Data.emit()

    def _Save_Data(self):
        self.Signal_Save_Data.emit()

    def _Record_Video(self):
        self.Signal_Record_Video.emit()

    def _Save_Video(self):
        self.Signal_Save_Video.emit()

    def _Open_Vedio(self):
        self.Signal_Open_Vedio.emit()

    def _Close_Vedio(self):
        self.Signal_Close_Vedio.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    Mainwindow = CAN_Presetting()
    Mainwindow.show()
    sys.exit(app.exec_())


