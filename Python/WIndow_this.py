from tkinter import *

def about():
         a = Toplevel()
         a.geometry('200x150+300+300')
         a['bg'] = 'grey'
         a.overrideredirect(True)
         Label(a, text='You this').pack(expand=1)
         a.after(5000, lambda: a.destroy())

root = Tk()
root.title('Главное окно')

Button(text='Klick Mi', width=40,
       height=5, bg='green',
       fg='red', font=20, command=about).pack()

root.mainloop()
