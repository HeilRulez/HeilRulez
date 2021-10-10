'''
import turtle

turtle.shape('classic')
for v in range (0, 7600, 10):
    turtle.forward(v)
    turtle.right(90)
'''
'''
import turtle
n = 0
turtle.shape('turtle')
for i in range (10):
    for h in range (4):
        turtle.forward(n*2+10)
        turtle.left(90)
    n += 10
    turtle.penup()
    turtle.goto(-n, -n)
    turtle.pendown()
'''
'''
turtle.shape('turtle')
for i in range (12):
    turtle.left(-30)
    turtle.forward(200)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(200)
    turtle.left(180) 
'''


import turtle
turtle.shape('turtle')
k=1
fi_rad=0.1
fi_degr=fi_rad*(180/3.14)
for i in range (0,1000):
    ro=k*fi_rad
    turtle.forward(ro)
    turtle.left(fi_degr)
    fi_rad+=0.1
    ro+=ro


'''    
import turtle

turtle.shape('turtle')
turtle.speed(1)

def triangle (length=20, kolvo=3, h=0):
    ugl = 360/kolvo
    turtle.left(kolvo*10)
    for i in range(kolvo):
        turtle.left(ugl)
        turtle.forward(length)
    turtle.right(h)
    turtle.penup()
    turtle.forward(10)
   # turtle.left(90)
    turtle.pendown()


kol = 3
le = 20
h = 30
for i in range (10):
    triangle(le, kol, h)
    kol +=1
    le += 10
    h = 30/kol-h

'''






