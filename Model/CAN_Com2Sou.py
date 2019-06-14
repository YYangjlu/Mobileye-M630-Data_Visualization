'''这个方法用于将一个补码列表转换为原码'''
class Com2Sou:
    def __init__(self):
        pass

    def Nint2Pint(self,Nint):
        '''
        :param Nint:补码列表；
        :return:返回原码列表；
        '''
        Nint_sup = [''] * len(Nint)
        Pint = [''] * len(Nint)
        leng = len(Nint)
        for i in range(leng):
            Nint_sup[i] = (bin(((1 << 8) - 1) & Nint[i])[2:]).zfill(8)
            Pint[i] = int(Nint_sup[i], 2)
        return Pint