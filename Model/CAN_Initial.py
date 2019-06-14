from ctypes import *

class CAN_INITIAL:
    def __init__(self,CANlib, nDeviceType, nDeviceInd, nCANInd, nReserved, vic):
        '''
        :param CANlib:动态链接库;
        :param nDeviceType:CAN设备类型号;
        :param nDeviceInd:CAN设备索引号;
        :param nCANInd:CAN设备通道号;
        :param nReserved:保留位;
        :param RefType:参考类型，当设备类型为PCI-5010-U、PCI-5020-U、USBCAN-E-U、USBCAN-2E-U时，
        参考类型RefType设置0对应CAN的波特率设置;
        '''
        self._Open_CAN(CANlib, nDeviceType, nDeviceInd, nReserved)
        self._Initial_CAN(CANlib, nDeviceType, nDeviceInd, nCANInd, vic)
        self._Start_CAN(CANlib, nDeviceType, nDeviceInd, nCANInd)
        self._Clear_Buffer(CANlib, nDeviceType, nDeviceInd, nCANInd)
        self.CAN_INITIAL_Result()

    '''打开CAN设备的函数'''
    def _Open_CAN(self, CANlib, nDeviceType, nDeviceInd, nReserved):
        '打开CAN设备'
        self._Open_CAN_Result =CANlib.VCI_OpenDevice(nDeviceType, nDeviceInd, nReserved)
        if self._Open_CAN_Result == 1:
            return 'OPEN CAN SUCCESSFULLY'
        else:
            return 'OPEN CAN  FAILED'

    '''初始化CAN设备函数'''
    def _Initial_CAN(self, CANlib, nDeviceType, nDeviceInd, nCANInd, vic):
        vic_Address = pointer(vic)
        self._Ini_CAN_Result = CANlib.VCI_InitCAN(nDeviceType, nDeviceInd, nCANInd, vic_Address)
        if self._Ini_CAN_Result  == 1:
            return 'INITIAL CAN SUCCESSFULLY'
        else:
            return 'INITIAL CAN FAILED'

    '''启动CAN设备函数'''
    def _Start_CAN(self, CANlib, nDeviceType, nDeviceInd, nCANInd):
        self._Start_CAN_Result = CANlib.VCI_StartCAN(nDeviceType, nDeviceInd, nCANInd)
        if self._Start_CAN_Result  == 1:
            return 'START CAN SUCCESSFULLY'
        else:
            return 'START CAN FAILED'

    '''清除CAN通道缓存'''
    def _Clear_Buffer(self, CANlib, nDeviceType, nDeviceInd, nCANInd):
        self._Clear_Buffer_Result =  CANlib.VCI_ClearBuffer(nDeviceType, nDeviceInd, nCANInd)
        if self._Clear_Buffer_Result  == 1:
            return 'CLEAR CAN BUFFER SUCCESSFULLY'
        else:
            return 'CLEAR CAN BUFFER FAILED'

    def CAN_INITIAL_Result(self):
        if self._Open_CAN_Result == 1  and self._Ini_CAN_Result == 1 and self._Start_CAN_Result == 1 and self._Clear_Buffer_Result == 1:
            return [1, 'INITIAL CAN DEVICE SUCCESSFULLY']
        else:
            return [0, 'INITIAL CAN DEVICE FAILED']

    '''关闭CAN设别的函数'''
    def CAN_Close(self, CANlib, nDeviceType, nDeviceInd):
        self._Close_CAN_Device = CANlib.VCI_CloseDevice(nDeviceType, nDeviceInd)
        if self._Close_CAN_Device == 1:
            return 'CLOSE CAN DEVICE SUCCESSFULLY'
        else:
            return 'CLOSE CAN DEVICE FAILED'