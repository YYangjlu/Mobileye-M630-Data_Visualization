from canlib import Frame

'''解析CAN报文，返回的是字典'''
class CAN_Msg_Analysis:
    def __init__(self):
        pass

    def analysis(self,ID, Bytearry_list, DBC):
        '''
        :param ID:报文ID；
        :param Bytearry_list:bytearry格式的数据列表；
        :param DBC:加载的DBC文件；
        :return:返回一个字典{信号名：数值, ...}
        '''
        signals_value = {}
        # signals_unit = {}
        frame = Frame(id_=ID, data=Bytearry_list)
        Message = DBC.interpret(frame)
        for Signal in Message:
            signals_value.setdefault(Signal.name,'{}'.format(Signal.value)) # Signal.phys, Signal.raw, Signal value,Signal.unit
            # signals_unit.setdefault(Signal.name, '{}'.format(Signal.unit))#这个返回信号名和单位{信号名：单位, ...}
        return signals_value #[signals_value, signals_unit]