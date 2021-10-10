from tkinter import *

root = Tk()

c = Canvas(width=200, height=200, bg='white')
c.pack()
c.create_oval(150, 10, 190, 50, fill='orange', outline='yellow')

c.create_polygon(100, 40, 30, 100, 170, 100, fill='lightblue')

c.create_rectangle(55, 100, 145, 180, fill='lightblue', outline='lightblue')
x1 = -30
x2 = 0

for i in range(80):
         c.create_arc(x1, 175, x2, 350,
                      start=160, extent=-70,
                      style=ARC, outline='green')
         x1 +=5
         x2 +=5

root.mainloop()
