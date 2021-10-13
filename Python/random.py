from random import *
from random import randint

def interg():
    try:
        a = int(input("Начало диапазона: "))
        b = int(input("Конец диапазона: "))
        c = randint(a, b)
        print(c)
    except ValueError:
        print("Неверные данные")
        interg()
    except AttributeError:
        print("Неверный диапазон")
        interg()

def flo():
    try:
        a = float(input("Начало диапазона: "))
        b = float(input("Конец диапазона: "))
        c = random() * (b -  a) + a
        print(c)
    except ValueError:
        print("Неверные данные")
        flo()
    except AttributeError:
        print("Неверный диапазон")
        flo()


def select():
    try:
        sel = int(input("0 - Вещественное\n1 - Целое\n"))
        if sel == 0:
            flo()
        elif sel == 1:
            interg()
        else:
            print("Неподходящий вариант")
            var()
            
    except ValueError:
        print("Введи число")
        select()

def var():
    var = input("X - Для выхода\nN - Для повтора\n")
    if var == 'X' or var == 'x':
        return
    elif var == 'N' or var == 'n':
        select()
    else:
        var_return()

def var_return():
    print("Неподходящий вариант")
    var()



select()

