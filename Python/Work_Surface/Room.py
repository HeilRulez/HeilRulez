"""Основной класс программы подщёта площади
    для оклеивания обоями"""


import WinDoor
from WinDoor import WinDoor


class Room:
    def __init__(self, x, y, z):
        """Принимает параметры комнаты.
        Ширина, длинна, высота"""
        self.width = x
        self.lenght = y
        self.height = z
        self.wd = []

    def addWD(self, w, h):
        """Принимает ширину и высоту проёма.
        Добавляет площадь проёма, для подсчёта"""
        self.wd.append(WinDoor(w, h))

    def workSurface(self):
        """Рассчитывает площадь оклейки"""
        new_square = self.square()
        for i in self.wd:
            new_square -= i.square
        return new_square

    def square(self):
        """Возвращает 'сырую' площадь помещения"""
        square = 2 * self.height * (self.width + self.lenght)
        return square


if __name__ == '__main__':
    print("Токрыт как самостоятельная программа")
    print("Здесь должен был быть приведён интерфейс программы")
