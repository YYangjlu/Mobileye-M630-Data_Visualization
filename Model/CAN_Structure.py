from ctypes import *

'''CAN设备初始化结构体定义'''
class VCI_INIT_CONFIG(Structure):
    '''
    AccCode = 0x00000000；
    AccMask = 0xffffffff；
    这两个是用来进行ID滤波的，默认值接收全部CAN报文；
    Filter = 0；滤波器，1表示单滤波，0表示双滤波；
    Timing0 = 0x00
    Timing1 = 0x1c；这个波特率对应500Kbps，其他波特率参考二次开发库函数介绍文档；
    这两个参数设置波特率 对于USBCAN1和USBCAN2类型的CAN卡是这样设置，另外有六个CAN卡通过其他方式设置；
    Mode = 0  # 0正常节点，1只听模式
    '''
    _fields_ = [('AccCode', c_ulong),
                ('AccMask', c_ulong),
                ('Reserved', c_ulong),
                ('Filter', c_ubyte),
                ('Timing0', c_ubyte),
                ('Timing1', c_ubyte),
                ('Mode', c_ubyte)]

class VCI_CAN_OBJ(Structure):
    _fields_ = [('ID', c_uint),
                ('TimeStamp', c_uint),
                ('TimeFlag', c_byte),
                ('SendType', c_byte),
                ('RemoteFlag', c_byte),
                ('ExternFlag', c_byte),
                ('DataLen', c_byte),
                ('Data', c_byte*8),
                ('Reserved', c_byte*3)]

class CAN_Device_Inf(Structure):
    '''
    nDeviceType:设备类型号，USNCAB2 对应4，其他类型参考接口卡设备类型定义；
    nDeviceInd:设备索引号，从0开始编号;
    nReserved:保留位;
    nCANInd:CAN通道号;
    '''
    _fields_ = [('nDeviceType', c_uint),
                ('nDeviceInd', c_uint),
                ('nReserved', c_uint),
                ('nCANInd', c_uint)]