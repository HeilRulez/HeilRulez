from tkinter import *
import random as rd
def move_bt():
         x = rd.random()
         y = rd.random()
         bt.place(relx=x, rely=y)


root = Tk()

img = PhotoImage(file='tenor.gif')

bt = Button(image=img, command=move_bt)
bt.place(width=50, height=50)

root.mainloop()
