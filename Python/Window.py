from tkinter import *

root = Tk()
root.title('Главное окно')

Button(text='Button', width=40,).pack()
Label(text='Label', width=40, height=3).pack()
Button(text='Button', width=40).pack()

root.update_idletasks()    #перезагружает данные размера окна, после отрисовки виджетов
s = root.geometry()
s = s.split('+')
s = s[0].split('x')
width_root = int(s[0])
height_root = int(s[1])

w = root.winfo_screenwidth()   #возвращает количество пикселей
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w-width_root//2
h = h-height_root//2

root.geometry('+{}+{}'.format(w, h))
root.resizable(False, False)     #запред изменения размера окна

root.mainloop()
