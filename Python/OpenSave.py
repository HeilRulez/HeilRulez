from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def insert_text():
         try:
                  file_name = fd.askopenfilename()
                  f = open(file_name)
                  s = f.read()
                  text.insert(1.0, s)
                  f.close()
                  
         except FileNotFoundError:
                  mb.showerror("Вниманее!", "Файл не выбран.")
                  

def extract_text():
         try:
                  file_name = fd.asksaveasfilename(
                           filetypes=(("TXT files", "*.txt"),
                                      ("HTML files", "*.html;*.htm"),
                                      ("ALL file", "*.*")))
                  f = open(file_name, 'w')
                  s = text.get(1.0, END)
                  f.write(s)
                  f.close()

         except FileNotFoundError:
                  mb.showerror("Вниманее!", "Документ не сохранён.")

def claner_text():
         answer = mb.askyesno("Вопрос", "Очистить поле?")
         if answer:
                  text.delete(1.0, END)

root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insert_text)
b1.grid(row=1, sticky=W)
b2 = Button(text="Сохранть", command=extract_text)
b2.grid(row=1, columnspan=2)
b3 = Button(text="Очистить", command=claner_text)
b3.grid(row=1, column=1, sticky=E)

root.mainloop()
