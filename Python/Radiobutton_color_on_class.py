from tkinter import *

def show():
    s = f'{var1.get()}, ' \
        f'{var2.get()}'
    label['text'] = s

def paint(color):
    label['bg'] = color

class RBcolor:
    def __init__(self, color, val):
        Radiobutton(text=color.capitalize(),
                    command=lambda i=color: paint(i),
                    variable=var, value=val).pack()

root = Tk()

var = IntVar()
var.set(0)
var1 = BooleanVar()
var1.set(0)
var2 = IntVar()
var2.set(-1)

frame = Frame()


RBcolor('red', 0)
RBcolor('green', 1)
RBcolor('blue', 2)

frame.pack()

c1 = Checkbutton(frame, text='First',
                 variable=var1, onvalue=1,
                 offvalue=0, command=show)

c2 = Checkbutton(frame, text='Second',
                 variable=var2, onvalue=333,
                 offvalue=0, command=show)
c1.pack(anchor=W, padx=10, side=LEFT)
c2.pack(anchor=W, padx=10, side=LEFT)

label = Label(frame, width=20, height=10, bg='pink')
label.pack(side=RIGHT)

root.mainloop()
    
