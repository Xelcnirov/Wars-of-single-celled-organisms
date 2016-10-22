from tkinter import *
from Units import Unit
from Camera import Camera

camera = Unit(1, 1)

class Animation:
    def __init__(self):
        self.c = Canvas(width=200, height=200, bg='black')
        self.c.pack()

    def draw(self, object):
        object.visual = self.c.create_oval([object.x - object.r - camera.x, object.y - object.r - camera.y],
                      [object.x + object.r - camera.x, object.y + object.r - camera.y], fill='yellow')

    def draw_hero(self, H1, H2, H3, H4):
        self.c.create_oval(H1, H2, H3, H4, fill='blue')

    def delete_obj(self, object):
        self.c.delete(object.visual)

    def flash(self, object):
        if self.c.itemcget(object.visual, 'fill') == 'yellow':
            self.c.itemconfig(object.visual, fill='red')
            self.c.update()
        else:
            self.c.itemconfig(object.visual, fill='yellow')
            self.c.update()

    def kill(self, object, count=0):
        count = count
        if count < 5:
            Animation.flash(self, object)
            count += 1
            self.c.after(300, self.kill, object, count)
        else:
            Animation.delete_obj(self, object)

test = Animation()
test1 = Unit(100, 100)
test.draw(test1)
test.kill(test1, 0)
mainloop()