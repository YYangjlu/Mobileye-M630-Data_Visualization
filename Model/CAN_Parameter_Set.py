from Model.CAN_Structure import VCI_INIT_CONFIG,CAN_Device_Inf

'''设置CAN设备结构体参数'''
class CAN_Par_Set(VCI_INIT_CONFIG):
    def __init__(self, Acc_Code = 0x00000000, Acc_Mask = 0xffffffff, Filt = 0, BPS1 = 0x00, BPS2 = 0x1c, Mod = 0):
        self.AccCode = Acc_Code
        self.AccMask = Acc_Mask
        self.Filter = Filt
        self.Timing0 = BPS1
        self.Timing1 = BPS2
        self.Mode = Mod

'''设备CAN设备设备类型、设备号和通道号'''
class CAN_Device_Set(CAN_Device_Inf):
    def __init__(self, nDeviceType = 4, nDeviceInd = 0, nReserved = 0, nCANInd = 0):
        self.nDeviceType = nDeviceType
        self.nDeviceInd = nDeviceInd
        self.nReserved = nReserved
        self.nCANInd = nCANInd