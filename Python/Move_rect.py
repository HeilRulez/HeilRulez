from tkinter import *

x_obj = 0
y_obj = 0
x_e = 0
y_e = 0

def start(event):
         global x_obj, y_obj, x_e, y_e
         x_obj = int(c.coords(rect)[2])
         y_obj = int(c.coords(rect)[3])
         x_e = int(event.x) + 20
         y_e = int(event.y) + 20
         move_obj()

def move_obj():
         global x_obj, y_obj
         if x_obj < x_e:
                  if y_obj < y_e:
                           c.move(rect, 1, 1)
                           x_obj = int(c.coords(rect)[2])
                           y_obj = int(c.coords(rect)[3])
                           root.after(10, move_obj)
                  else:
                           c.move(rect, 1, -1)
                           x_obj = int(c.coords(rect)[2])
                           y_obj = int(c.coords(rect)[3])
                           root.after(10, move_obj)
         else:
                  if y_obj < y_e:
                           c.move(rect, -1, 1)
                           x_obj = int(c.coords(rect)[2])
                           y_obj = int(c.coords(rect)[3])
                           root.after(10, move_obj)
                  else:
                           c.move(rect, -1, -1)
                           x_obj = int(c.coords(rect)[2])
                           y_obj = int(c.coords(rect)[3])
                           root.after(10, move_obj)



root = Tk()

c = Canvas(root, width=400, height=400, bg='lightgreen')

c.pack()

rect = c.create_rectangle(0, 0, 40, 40, fill='darkblue')

root.bind('<Button-1>', start)

root.mainloop()
