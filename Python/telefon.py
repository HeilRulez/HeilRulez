from tkinter import *

def show(lab):
    labus = str(lab)
    label['text'] = labus

class people():
    def __init__(self, master, name, tel):
        Radiobutton(master, text=name,
                    command=lambda i=tel: show(i),
                    variable=var, indicatoron=0,
                    value=tel, width=15).pack(side=TOP)

root = Tk()

var = IntVar()
var.set(0)
f1 = Frame()
f2 = Frame()

f1.pack(side=LEFT)
f2.pack(side=RIGHT)

people(f1, 'Вася', 79503485474)
people(f1, 'Дима', 79436486755)
people(f1, 'Маша', 79345649354)


label = Label(f2, width=20, height=5, bg='pink')
label.pack()

root.mainloop()
