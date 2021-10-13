"""Программа считает площадь под обои и кол-во рулонов"""


from Room import Room as R
import math

def oboi(a, b):
    s = r.workSurface()
    kol_vo = s / (a * b)
    return math.ceil(kol_vo)

input("Введите параметры: (для продолжения нажмите 'Enter')")
x = float(input("Ширина комнаты?\n"))
y = float(input("Длинна комнаты?\n"))
z = float(input("Высота комнаты?\n"))

r = R(x, y, z)

out = 1

while out == 1:
    i = int(input("Добавить проём?\nДа - 1\nНет - 0\n"))
    if i == 1:
        xp = float(input("Ширина проёма?\n"))
        yp = float(input("Высота проёма?\n"))
        r.addWD(xp, yp)
    elif i == 0:
        out = 0

a = float(input("Длинна рулона обоев?\n"))
b = float(input("Ширина рулона обоев?\n"))


print("Оклеиваемая площадь {} м\кв из {} м\кв." .format(round(r.workSurface(), 2), round(r.square(), 2)))
print("Необходимо {} рулонов обоеа." .format(oboi(a, b)))





