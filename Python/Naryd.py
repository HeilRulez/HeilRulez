from tkinter import *
from tkinter import messagebox

def open_click():
         #messagebox.showinfo('Этеншн', 'Нажал ты открыть!')

def add_list():
         #фенкция добавления в лист наряда на день
         

root = Tk()
root.title('Серёгина прога')
root.geometry()

date_now = Entry() #поле с указанием даты с которой добовляется наряд
detail = Entry()  # поле ввода номера детали
operation = Entry()  # номер пореации
quantity = Entry()  # количество штук
rem = Checkbutton()  #гулочка ремонтная деталь







'''
main_menu = Menu()

file_menu = Menu(tearoff=0) #параметр отсоединения меню

file_menu.add_command(label='Новый')
file_menu.add_command(label='Открыть', command=open_click)
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Выход')


main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Првка')
main_menu.add_cascade(label='Вид')

'''

root.config(menu=main_menu)
root.mainloop()
