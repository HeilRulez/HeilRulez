from tkinter import *

def str_float (str):
         if str.isnumeric():
                  return int(str)
         else:
                  try:
                           flo = float(str)
                           return flo
                  except ValueError:
                           return False

def plus ():
         en1 = ent_1.get()
         en2 = ent_2.get()
         if str_float(en1) and str_float(en2):
         
                  lab['text'] = (str_float(en1)+str_float(en2))
         else:
                  lab['text'] = 'Ошибка'

def minus ():
         en1 = ent_1.get()
         en2 = ent_2.get()
         if str_float(en1) and str_float(en2):
                  
                  lab['text'] = (str_float(en1)-str_float(en2))
         else:
                  lab['text'] = 'Ошибка'

def umn ():
         en1 = ent_1.get()
         en2 = ent_2.get()
         if str_float(en1) and str_float(en2):
                  
                  lab['text'] = (str_float(en1)*str_float(en2))
         else:
                  lab['text'] = 'Ошибка'

def deli ():
         en1 = ent_1.get()
         en2 = ent_2.get()
         if str_float(en1) and str_float(en2):
                  
                  lab['text'] = (str_float(en1)/str_float(en2))
         else:
                  lab['text'] = 'Ошибка'
root = Tk()

ent_1 = Entry()
ent_2 = Entry()



plus = Button(text='+', width=15, command=plus)
minus = Button(text='-', width=15, command=minus)
umn = Button(text='*', width=15, command=umn)
deli = Button(text='/', width=15, command=deli)

lab = Label()

ent_1.pack()
ent_2.pack()
plus.pack()
minus.pack()
umn.pack()
deli.pack()
lab.pack()

root.mainloop()
