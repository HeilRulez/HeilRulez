from tkinter import *
root = Tk()
def select():
    if var.get():
        lbox['selectmode'] = EXTENDED
    else:
        lbox['selectmode'] = ''

def udalit():
    sel = list(lbox.curselection())
    sel.reverse()
    for i in sel:
        lbox.delete(i)


var = BooleanVar()
var.set(0)

cb = Checkbutton(text='Количество строк', variable=var,
                 onvalue=1, offvalue=0, command=select)
cb.pack()


lbox = Listbox(width=15, height=8)
lbox.pack(side=LEFT)

sb = Scrollbar(command=lbox.yview)

sb.pack(side=LEFT, fill=Y)

lbox.config(yscrollcommand=sb.set)

for i in ('one', 'two', 'tree', 'four',
          'five', 'six', 'seven'):
    lbox.insert(END, i)

bt = Button(text='Удалить выбранное', command=udalit)
bt.pack(side=LEFT, fill=X)
root.mainloop()
