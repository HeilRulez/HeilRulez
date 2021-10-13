from tkinter import *

def entryThis(event):
    entry.delete(0, END)
    i = list.curselection()
    entry.insert(0, list.get(i))


def entryList(event):
    list.insert(0, entry.get())
    entry.delete(0, END)

root = Tk()

entry = Entry()

list = Listbox()

entry.bind('<Return>', entryList)
entry.pack()
list.bind('<Double-Button-1>', entryThis)
list.pack()

root.mainloop()
