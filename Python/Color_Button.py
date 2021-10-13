from tkinter import *

color = [('#ff0000', 'красный'), ('#ff7d00', 'оранжевый'),
    ('#ffff00', 'желтый'), ('#00ff00', 'зеленый'),
        ('#007dff', 'голубой'), ('#0000ff', 'синий'),
         ('#7d00ff', 'фиолетовый')]

def b0_K ():
    lb['text'] = color[0][1]
    en.delete(0, END)
    en.insert(0, color[0][0])

def b1_O ():
    lb['text'] = color[1][1]
    en.delete(0, END)
    en.insert(0, color[1][0])

def b2_Y ():
    lb['text'] = color[2][1]
    en.delete(0, END)
    en.insert(0, color[2][0])

def b3_G ():
    lb['text'] = color[3][1]
    en.delete(0, END)
    en.insert(0, color[3][0])

def b4_B ():
    lb['text'] = color[4][1]
    en.delete(0, END)
    en.insert(0, color[4][0])

def b5_S ():
    lb['text'] = color[5][1]
    en.delete(0, END)
    en.insert(0, color[5][0])

def b6_F ():
    lb['text'] = color[6][1]
    en.delete(0, END)
    en.insert(0, color[6][0])


root = Tk()
lb = Label(width=15)
en = Entry(width=15, justify=CENTER)

lb.pack()
en.pack(expand=1, fill=X)

text = Text(width=25, height=5, bg='darkgreen', fg='white', wrap=WORD)
text.pack(side=BOTTOM)

d0 = Button(bg=color[0][0], width=2, height=1, command=b0_K).pack(side=LEFT, expand=1)
d1 = Button(bg=color[1][0], width=2, height=1, command=b1_O).pack(side=LEFT, expand=1)
d2 = Button(bg=color[2][0], width=2, height=1, command=b2_Y).pack(side=LEFT, expand=1)
d3 = Button(bg=color[3][0], width=2, height=1, command=b3_G).pack(side=LEFT, expand=1)
d4 = Button(bg=color[4][0], width=2, height=1, command=b4_B).pack(side=LEFT, expand=1)
d5 = Button(bg=color[5][0], width=2, height=1, command=b5_S).pack(side=LEFT, expand=1)
d6 = Button(bg=color[6][0], width=2, height=1, command=b6_F).pack(side=LEFT, expand=1)


root.mainloop()
