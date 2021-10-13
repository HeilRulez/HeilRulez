from tkinter import *


def paint():
    if v == 0:
        c.create_rectangle(20, 20, 50, 50)
    

def new_f():
    var = IntVar()
    var.set(0)
    win_two = Toplevel()
    win_two.geometry('+400+200')
    Label(win_two, text='x1').grid(row=0, column=0, sticky='N')
    Label(win_two, text='y1').grid(row=0, column=2, sticky='N')
    Label(win_two, text='x2').grid(row=1, column=0, sticky='N')
    Label(win_two, text='y2').grid(row=1, column=2, sticky='N')

    entry_x1 = Entry(win_two, width=4)
    entry_y1 = Entry(win_two, width=4)
    entry_x2 = Entry(win_two, width=4)
    entry_y2 = Entry(win_two, width=4)

    entry_x1.grid(row=0, column=1, sticky='W')
    entry_y1.grid(row=0, column=3, sticky='W')
    entry_x2.grid(row=1, column=1, sticky='W')
    entry_y2.grid(row=1, column=3, sticky='W')

    rb_rect = Radiobutton(win_two, text='Прямоугольник',
                     variable=var, value=0)
    rb_chr = Radiobutton(win_two, text='Овал',
                         variable=var, value=1)

    rb_rect.grid(row=2, columnspan=4, sticky='W')
    rb_chr.grid(row=3, columnspan=4, sticky='W')

    btn_pain = Button(win_two, text='Рисовать',
                      command=paint)\
               .grid(row=4, columnspan=4)


root = Tk()

c = Canvas(root, width=400, height=400, bg='white')
btn = Button(root, text='Добавить фигуру', font=12, command=new_f)

c.pack()
btn.pack(ipadx=8, ipady=2)

root.mainloop()
