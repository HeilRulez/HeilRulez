from tkinter import *

def play(event):
         x = ent_x.get()
         y = ent_y.get()
         if x.isdigit() and y.isdigit():
                  tex.configure(width=x, height=y)

def focus_t(event):
         if str(event.type) == 'FocusIn':
                  tex['bg'] = 'white'
         elif str(event.type) == 'FocusOut':
                  tex['bg'] = 'lightgrey'
         

root = Tk()

fr1 = Frame()

ent_x = Entry(fr1, width=2)
ent_y = Entry(fr1, width=2)



btn = Button(fr1, text='Изменить')

tex = Text(bg='lightgrey')
btn.pack(padx=5, pady=5, side=RIGHT)
ent_x.pack()

ent_y.pack()


btn.bind('<Button-1>', play)
ent_x.bind('<Return>', play)
ent_y.bind('<Return>', play)

tex.bind('<FocusIn>', focus_t)
tex.bind('<FocusOut>', focus_t)

fr1.pack()

tex.pack()

tex.configure(width=10, height=5)

root.mainloop()
