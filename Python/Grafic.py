from tkinter import *


clicks = 0

def click_button():
    global clicks
    clicks += 1
    btn.config(text="Clicks {}" .format(clicks))


def click_0():
    global clicks
    clicks = 0
    btn.config(text="Clicks {}" .format(clicks)) 



root = Tk()
root.title("Grafic")
root.geometry("600x400")

btn = Button(root, text="Clicks 0",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             command = click_button
             )
btn.pack(fill=X)

btn_2 = Button(root, text='Two clicker',
               background='#333',
               foreground='#fff',
               padx='20',
               pady='8',
               font='16',
               command = click_0
               )
btn_2.place(anchor='nw', y=100)

'''
for r in range(3):
    for c in range(3):
        btn_1 = Button(root, text='{}-{}' .format(r, c))
        btn_1.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)
'''

lable_1 = Label(text='Hello Python', fg='#eee', bg='#333')
lable_1.pack()

poetry = "skjflkhflkghlkhgkhglkuhfsklfsksfh"

lable_2 = Label(text=poetry, justify=LEFT)
lable_2.place(relx=.2, rely=.3)

root.mainloop()





