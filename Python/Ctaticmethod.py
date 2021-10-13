from math import pi


class Cylinder:
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle*2 + side, 2)

    def __init__(self, diameter, high):
        self.dia = diameter
        self.h = high
        self.__area = self.make_area(diameter, high)

    def __setattr__(self, attr, value):
        if attr == 'dia':
            self.__dict__[attr] = value
            
        elif attr == 'h':
            self.__dict__[attr] = value
            
        elif attr == '_Cylinder__area':
            self.__dict__[attr] = value
            
        else:
            print('Не ломай прогу')
        

    def get_area(self):
        self.__area = self.make_area(self.dia, self.h)
        return self.__area

a = Cylinder(1, 2)
print(a.get_area())
a.dia = 3
print(a.get_area())




print(a.make_area(2, 2))


