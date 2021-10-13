from tkinter import *

def open_fail():
    try:
        with open(ent.get(), 'r') as fail:
            text.delete(1.0, END)
            text.insert(END, fail.read())
    except:
        text.delete(1.0, END)
        text.insert(END, 'Фаил не найден.')


def save_fail():
    with open(ent.get(), "a") as fail:
        fail.write(text.get(1.0, END))

    
root = Tk()

frame_up = Frame()
frame_down = Frame()

frame_up.pack()
frame_down.pack()


ent = Entry(frame_up, width=20)
but_open = Button(frame_up, text='Открыть',
                  width=15, command=open_fail)
but_save = Button(frame_up, text='Сохранить',
                  width=15, command=save_fail)

ent.pack(side=LEFT)
but_open.pack(side=LEFT)
but_save.pack(side=LEFT)

text = Text(frame_down, width=50, height=20, wrap=NONE)
text.pack(side=LEFT)

scroll_Y = Scrollbar(frame_down, command=text.yview)
scroll_Y.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll_Y.set)

scroll_X = Scrollbar(orient=HORIZONTAL, command=text.xview)
scroll_X.pack(side=TOP, fill=X)
text.config(xscrollcommand=scroll_X.set)

root.mainloop()
