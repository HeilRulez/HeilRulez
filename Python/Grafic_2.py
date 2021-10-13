from tkinter import *
from tkinter import messagebox

languages = [('Pyyhon', 1), ('JavaScript', 2), ('C#', 3), ('Java', 4)]

def select():
    l = language.get()
    if l == 1:
        sel.config(text='Python')
    elif l == 2:
        sel.config(text='JavaScript')
    elif l == 3:
        sel.config(text='C#')
    elif l == 4:
        sel.config(text='Java')


def show_message():
    messagebox.showinfo("Gui Python", message.get() + " " + str(ismarried.get()))


root = Tk()
root.title("Grafic")
root.geometry("600x400")

message = StringVar()
language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(root, text=txt, value=val,
                variable=language, padx=15,
                pady=10, command=select)\
                .grid(row=row, sticky=W)
    row +=1

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)
    
message_entry =  Entry(root, textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor='c')

ismarried = IntVar()

ismarried_checkbutton = Checkbutton(text='Женад\Замужем', variable=ismarried)
ismarried_checkbutton.grid()

message_button = Button(text="Click Me", command=show_message)
message_button.place(relx=.5, rely=.5, anchor='c')


root.mainloop()







