from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def openfile():
         try:
                  file_name = fd.askopenfilename()
                  file = open(file_name)
                  s = file.read()
                  text.insert(1.0, s)
                  file.close()
         except FileNotFoundError:
                  mb.showerror("Ошибка", "Файл не выбран.")
                  

def savefile():
         try:
                  file_name = fd.asksaveasfilename(filetypes=(
                           ("TXT", "*.txt"), ("HTML", "*.html;*.hml"),
                           ("ALL", "*.*")))
                  file = open(file_name, 'w')
                  s = text.get(1.0, END)
                  file.write(s)
                  file.close()
         except FileNotFoundError:
                  mb.showerror("Ошибка", "Не сохранено.")
         

def claner():
         text.delete(1.0, END)

def popup(event):
         contmenu.post(event.x_root, event.y_root)

root = Tk()

text = Text(root)
text.pack()


mainmenu = Menu(root, tearoff=0)

mainmenu.add_command(label="Открыть", command=openfile)
mainmenu.add_command(label="Сохранить", command=savefile)

text.bind('<Button-3>', popup)

contmenu = Menu(root, tearoff=0)
contmenu.add_command(label="Очистить", command=claner)

root.config(menu=mainmenu)

root.mainloop()
