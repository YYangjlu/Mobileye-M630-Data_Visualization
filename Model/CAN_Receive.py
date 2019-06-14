from Model.CAN_Initial import *
from Model.CAN_Com2Sou import *

'''继承CAN初始化类，实例化后直接初始化'''
class CAN_Rec(CAN_INITIAL):
    def __init__(self,CANlib, nDeviceType, nDeviceInd, nCANInd, nReserved, vic):
        super(CAN_Rec,self).__init__(CANlib, nDeviceType, nDeviceInd, nCANInd, nReserved, vic)

    def CAN_Msg_Rec(self, CANlib, nDeviceType, nDeviceInd, nCANInd, vco, Frame_num = 1, Time_out = 1000):
        '''
        :param CANlib:
        :param nDeviceType:
        :param nDeviceInd:
        :param nCANInd:
        :param vco:
        :param Frame_num:每次接收的CAN报文帧数；
        :param Time_out:接收报文的等待时常；
        :return:返回一个，包含报文ID和报文原始数据；
        '''
        CANlib.VCI_Receive(nDeviceType, nDeviceInd, nCANInd, pointer(vco), Frame_num, Time_out)
        self.ID_receive = vco.ID
        self.Data = Com2Sou().Nint2Pint(list(vco.Data))
        return  [self.ID_receive,self.Data]
