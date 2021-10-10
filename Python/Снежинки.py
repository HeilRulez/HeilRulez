class Snow:
         def __init__(self):        #поле с исходным кол-во снежинок
                  self.snow = 64

         def __call__(self, z):     #вызов в нотации функции
                  self.snow = z

         def __add__(self, x):      #переопределение сложения
                  self.snow += x

         def __sub__(self, x):      #переопределение вычитания
                  self.snow -= x

         def __mul__(self, x):      #переопределение умножения
                  self.snow *= x

         def __truediv__(self, x):  #переопределение деления с округлением
                  self.snow = round(self.snow / x)

         def makeSnow(self, p):     #выводит снежинки :)
                  out = p * "*" + '\n'
                  print(int(self.snow / p) * out)


#s = Snow()   пример создания объекта
#s.makeSnow(8) вывод с восемью снежинками в ряд
#s(32)  пример вызова в нотации функции, с присвоением полю общего числа снежинок
#s+4    пример увеличения общего числа на 4, сложением
