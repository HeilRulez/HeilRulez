import turtle
from random import *

'''
def cerkl ():
    for i in range (360):
        turtle.left(1)
        turtle.forward(1)
    for t in range (360):
        turtle.right(1)
        turtle.forward(1)

for i in range(3):
    cerkl()
    turtle.left(180/3)
'''

'''
def cerkle (x):
    for i in range(360):
        turtle.left(1)
        turtle.forward(x)
    for v in range(360):
        turtle.right(1)
        turtle.forward(x)

turtle.left(90)
x = 0.5
for i in range(10):
    cerkle(x)
    x += 0.1
'''

'''
def cerkle_max ():
    for i in range(180):
        turtle.right(1)
        turtle.forward(0.5)


def cerkle_min ():
    for i in range(180):
        turtle.right(1)
        turtle.forward(0.1)

turtle.left(90)
for i in range(5):
    cerkle_max()
    cerkle_min()
'''



'''
def krug (krug=True, d=1, color='black'):
    if krug:
        turtle.begin_fill()
        for i in range(360):
            turtle.forward(d)
            turtle.left(1)
        turtle.color(color)
        turtle.end_fill()
        turtle.color('black')
    else:
        turtle.color(color)
        for i in range(180):
            turtle.forward(d)
            turtle.right(1)


turtle.penup()
turtle.goto(50, 0)
turtle.pendown()
turtle.left(90)

krug(color='yellow')

turtle.penup()
turtle.goto(-25, 30)
turtle.pendown()

krug(d=0.15, color='blue')

turtle.penup()
turtle.goto(28, 30)
turtle.pendown()

krug(d=0.15, color='blue')

turtle.penup()
turtle.goto(-5, 15)
turtle.pendown()

turtle.left(180)
turtle.width(10)
turtle.forward(15)

turtle.penup()
turtle.goto(22, -5)
turtle.pendown()

krug(False, d=0.5, color='red')

'''

'''
def star(n):
    for i in range (n):
        if n%2==0:
            nU = 180+(360/n)
        else:
            nU = ((360/n)*(n//2))
        turtle.forward(80)
        turtle.right(nU)

star(8)

'''


'''
for i in range(100):
    turn = round(random()*100)
    if turn%2 == 0:
        turtle.left(round(random()*100))
    else:
        turtle.right(round(random()*100))
    turtle.forward(round(random()*30))

'''


A = []
for i in range (int(input())):
    A.append(int(input()))
for elem in range(len(A)):
    print(A[elem])
for elem in A:
    print(elem, end=' ')

print(' '.join(map(str, A )))












