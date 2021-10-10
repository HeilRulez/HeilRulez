from tkinter import *

root = Tk()

c = Canvas(root, width=400, height=400, bg='white')
c.pack()

c.create_line(10, 10, 190, 50)

c.create_line(100, 180, 100, 60, fill='green',
              width=5, arrow=LAST, dash=(10, 2),
              activefill='lightgreen',
              arrowshape='10 20 10')

c.create_rectangle(10, 10, 190, 60)

c.create_rectangle(160, 180, 240, 290,
                   fill='yellow',
                   outline='green',
                   width=3,
                   activedash=(5, 4))

c.create_polygon(100, 10, 20, 90,
                 180, 90)

c.create_polygon((40, 110),
                 (160, 110),
                 (190, 180),
                 (10, 180),
                 fill='orange', outline='black')

c.create_oval(50, 10, 150, 110, width=20)

c.create_oval(10, 120, 190, 190, fill='grey70', outline='white')

root.mainloop()
