import numpy as np

'''坐标计算，将距离和角度转化为摄像头坐标系的X-Y坐标'''
class Coordinate:
    def __init__(self):
        pass

    def XY_Calculate(self, Angle, Distance):
        '''
        :param Angle: 所有点的方位角向量；
        :param Distance: 所有点距离摄像头的距离向量；
        :return:X和Y坐标；
        X: 返回所有点的X坐标向量，与Y一一对应；
        Y: 返回所有点的Y坐标向量，与X一一对应；
        '''
        self.X = Distance * np.cos(Angle * (np.pi / 180))
        self.Y = Distance * np.sin(Angle * np.pi / 180)
        return [self.X, self.Y]

    def Lane_XY_Calculate(self,Lane_C0, Lane_C1, Lane_C2, Lane_C3):
        '''
        :param Lane_C0:拟合参数C0，列向量；
        :param Lane_C1:拟合参数C1，列向量；
        :param Lane_C2:拟合参数C2，列向量；
        :param Lane_C3:拟合参数C3，列向量；
        :return:返回所有车道线的X和Y坐标；
        '''
        self.X_Lane = np.arange(0,50,1)*np.ones([2,50])
        self.Y_Lane = Lane_C0 + Lane_C1*self.X_Lane + Lane_C2*pow(self.X_Lane,2)+ Lane_C3*pow(self.X_Lane,3)
        return [self.X_Lane, self.Y_Lane]