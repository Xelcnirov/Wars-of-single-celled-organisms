from tkinter import *

world = {'x': 0, 'y': 0, 'w': 550, 'h': 550}


class Unit:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def godown(self):
        self.y += 5
        self.x += 5


def click(event):
    un.godown()
    if (un.x > world['x'] - un.r or un.y > world['y'] - un.r) and \
            (un.x < world['w'] + un.r or un.y < world['h'] + un.r):
        c.delete('all')
        c.create_oval([un.x - un.r, un.y - un.r], [un.x + un.r, un.y + un.r], fill='yellow')

un = Unit(0, -55, 50)

c = Canvas(width=500, height=500, bg='black')
c.pack()

c.bind('<Button-1>', click)

mainloop()

