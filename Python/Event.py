from tkinter import *

def enter_leave(event):
         if str(event.type) == 'Enter':
                  event.widget['text'] = 'IN'
         elif str(event.type) == 'Leave':
                  event.widget['text'] = 'OUT'


root = Tk()

lab1 = Label(width=20, height=3, bg='white')
lab1.pack()
lab1.bind('<Enter>', enter_leave)
lab1.bind('<Leave>', enter_leave)

lab2 = Label(width=20, height=3, bg='black', fg='white')
lab2.pack()
lab2.bind('<Enter>', enter_leave)
lab2.bind('<Leave>', enter_leave)
root.mainloop()
