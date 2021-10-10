from tkinter import *

def add_f():
         win_2 = Toplevel()
         win_2.geometry('+400+200')
         global var, x1, y1, x2, y2, des

         Label(win_2, text='x1', font=12).grid(row=0, column=1, pady=3, sticky=E)
         Label(win_2, text='y1', font=12).grid(row=0, column=3, pady=3, sticky=E)
         Label(win_2, text='x2', font=12).grid(row=1, column=1, pady=3, sticky=E)
         Label(win_2, text='y2', font=12).grid(row=1, column=3, pady=3, sticky=E)

         ent_x1 = Entry(win_2, width=5, textvariable=x1)\
                  .grid(row=0, column=2, pady=3, sticky=W)
         ent_y1 = Entry(win_2, width=5, textvariable=y1)\
                  .grid(row=0, column=4, pady=3, sticky=W)
         ent_x2 = Entry(win_2, width=5, textvariable=x2)\
                  .grid(row=1, column=2, pady=3, sticky=W)
         ent_y2 = Entry(win_2, width=5, textvariable=y2)\
                  .grid(row=1, column=4, pady=3, sticky=W)


         rb1 = Radiobutton(win_2, text='Прямоугольник', variable=var, value=0)\
               .grid(row=2, column=2, columnspan=4, sticky=W)
         rb2 = Radiobutton(win_2, text='Овал', variable=var,
                           value=1)\
               .grid(row=3, column=2, columnspan=4, sticky=W)

         btn_pain = Button(win_2, text='Нарисовать', command=pain)\
                    .grid(row=4, column=0, columnspan=5, ipadx=5, ipady=3, sticky=W+E)
         des = win_2

         
def pain():
         if var.get() == 0:
                  c.create_rectangle(x1.get(), y1.get(), x2.get(), y2.get())
                  des.destroy()
         elif var.get() == 1:
                  c.create_oval(x1.get(), y1.get(), x2.get(), y2.get())
                  des.destroy()
         
         
root = Tk()
root.title('Рисовалка')

var = IntVar()
var.set(0)

x1 = StringVar()
y1 = StringVar()
x2 = StringVar()
y2 = StringVar()

des = None

c = Canvas(root, width=400, height=300, bg='white')

btn = Button(root, text='Добавить фигуру', command=add_f)

c.pack()
btn.pack(ipadx=5, ipady=3)

root.mainloop()
