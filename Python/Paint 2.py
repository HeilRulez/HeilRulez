from tkinter import *

def play():
    c.create_rectangle(30, 39, 49, 59)

root = Tk()

c = Canvas(width=400, height=300, bg='white')
c.pack()


btn = Button(text='fsfs', command=play)
btn.pack()

root.mainloop()
