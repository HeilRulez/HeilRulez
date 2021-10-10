import random
from random import randint

class unit:
         def __init__(self, id, cd):
                  self.id = id
                  self.comand = cd

class hero(unit):
         lv = 0
         def lavel(self):
                  self.lv += 1


class soldier(unit):
         def goTo(self, hero):
                  print("Sold id: ", self.id, "Hero id: ", hero.id)


h1 = hero(0, 'rad')
h2 = hero(1, 'blue')

radG = []
blueG = []

def start():
         rad = [h1]
         blue = [h2]
         for i in range(2, 22):

                  if random.randint(0, 100)%2 == 0:
                           rad.append(soldier(i, 'rad'))
                  else:
                           blue.append(soldier(i, 'blue'))
                  
         if len(rad) < len(blue):
                  h2.lavel()
                  print("Lavel hero in Blue: ", h2.lv)
         elif len(rad) > len(blue):
                  h1.lavel()
                  print("Lavel hero in Rad: ", h1.lv)
         else:
                  print("Ничья")
         print(len(rad), len(blue))
         global radG, blueG
         radG = rad
         blueG = blue
i = 0
while i == 0:
         start()
         i = int(input())
sold = radG[1]
sold.goTo(h1)

