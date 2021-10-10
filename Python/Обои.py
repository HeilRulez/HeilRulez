import math


class WinDoor:
         def __init__(self, x, y):
                  self.squareWD = x * y  #выщитывает площадь неоклеиваемых проёмов


class Room:
         '''
                  Основной класс
         '''
         def __init__(self, x, y, z): #размеры помещения
                  self.width = x
                  self.lenght = y
                  self.height = z
                  self.wd = []

         def square(self): #расчёт площади помещения
                  square = 2 * self.height * (self.width + self.lenght)
                  return square

         def addWD(self, w, h):  #добавление площади проёма в список
                  self.wd.append(WinDoor(w, h))

         def workSurface(self):  #вычетание проёмов из общеё площади
                  new_square = self.square()
                  for i in self.wd:
                           new_square -= i.squareWD  #вычитание одного элемента списка
                  return new_square

         def rulon(self, x, y):  #расчёи площади рулона. округление вверх
                  rul = math.ceil(self.workSurface() / (x * y))
                  return rul

x = float(input('Введите длинну комнаты: '))
y = float(input('Введите ширину комнаты: '))
z = float(input('Введите высоту комнаты: '))
r1 = Room(x, y, z)
i = int(input('Добавить проём - 1.\nДалее - 0.\n'))

while i == 1:  
         x = float(input('Высота проёма: '))
         y = float(input('Ширна проёма: '))
         r1.addWD(x, y)
         i = int(input('Добавить проём - 1.\nДалее - 0.\n'))

plo = r1.workSurface()

x = float(input('Введите ширину рулона обоев: '))
y = float(input('Ввдите длинну обоев: '))
rul = r1.rulon(x, y)

print(f'Площадъ оклеиваемой поверхности: {plo}.')
print(f'Необходимо {rul} рулонов обоев.')
