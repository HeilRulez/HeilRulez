from tkinter import *

def changeFont(font):
    l['font'] = font

root = Tk()

l = Label(text='Hellow World')
l.pack()
Button(command=lambda f='Verdana': changeFont(f)).pack()
Button(command=lambda f='Times': changeFont(f)).pack()

root.mainloop()
