from tkinter import *
from tkinter import messagebox

def edit_click():
         messagebox.showinfo('Этеншн', 'Нажал ты открыть!')

root = Tk()
root.title('Серёгина прога')
root.geometry('300x250')

main_menu = Menu()

file_menu = Menu(tearoff=0) #параметр отсоединения меню

file_menu.add_command(label='Новый')
file_menu.add_command(label='Открыть', command=edit_click)
file_menu.add_command(label='Сохранить')
file_menu.add_separator()
file_menu.add_command(label='Выход')


main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Првка')
main_menu.add_cascade(label='Вид')

root.config(menu=main_menu)
root.mainloop()
