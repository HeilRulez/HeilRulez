from tkinter import *

def insert_text ():
    s = 'Helow World!'
    text.insert(1.0, s)

def get_text ():
    s = text.get(1.0, END)
    label['text'] = s

def delete_text ():
    text.delete(1.0, END)

root = Tk()

fr = Frame()
fr.pack()

text = Text(fr, width=20, height=7)
text.pack(side=LEFT)


scroll = Scrollbar(fr, command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)

frame = Frame()
frame.pack()

Button(frame, text='Вставить', command=insert_text).pack(side=LEFT)
Button(frame, text='Взять', command=get_text).pack(side=LEFT)
Button(frame, text='Удалить', command=delete_text).pack(side=LEFT)

text.tag_add('title', 1.0, '1.end')
text.tag_config('title', justify=CENTER, font=('Verdana', 24, 'bold'))

label = Label()
label.pack()

root.mainloop()
