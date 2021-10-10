from tkinter import *

def left_giper():
         sel = list(Li_1.curselection())
         sel.reverse()
         for i in sel:
                  Li_2.insert(0, Li_1.get(i))
                  Li_1.delete(i)


def right_giper():
         sel = list(Li_2.curselection())
         sel.reverse()
         for i in sel:
                  Li_1.insert(0, Li_2.get(i))
                  Li_2.delete(i)


list_bay = ["Помидор", "Огурец",
            "Салат", "Сметана",
            "Соль", "Перец", "Хлеб",
            "Чай", "Печение", "Молоко"]

root = Tk()

frame = Frame()

Li_1 = Listbox(selectmode=EXTENDED)
Li_2 = Listbox(selectmode=EXTENDED)

butt_left = Button(frame, text='>>>', command=left_giper)
butt_riht = Button(frame, text='<<<', command=right_giper)

Li_1.pack(side=LEFT)
frame.pack(side=LEFT)
butt_left.pack(ipadx=10)
butt_riht.pack(ipadx=10)
Li_2.pack(side=LEFT)
for i in list_bay:
         Li_1.insert(END, i)

root.mainloop()
