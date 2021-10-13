from tkinter import *

def motion():
    c.move(ball, 1, 0)
    if c.coords(ball)[2] < 300:
        root.after(10, motion)

def her(event):
    c.itemconfig(rec, x=event.x, y=event.y)

    

root = Tk()

c = Canvas(root, width=300, height=200, bg='white')
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

rec = c.create_rectangle(0, 20, 20, 40, fill='black', outline='white')

root.bind('<Button-1>', her)

motion()
root.mainloop()
