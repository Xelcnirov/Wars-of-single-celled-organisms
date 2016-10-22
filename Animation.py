from tkinter import *
from Camera import Camera


class Animation:
    def __init__(self):
        self.root = Tk()
        self.c = Canvas(width=camera.width, height=camera.height, bg='black')
        self.c.pack()
        self.root.mainloop()

    def draw(self, object_x, object_y, object_r):
        self.c.create_oval([object_x - object_r - camera.x, object_y - object_r - camera.y],
                      [object_x + object_r - camera.x, object_y + object_r - camera.y], fill='yellow')

    def draw_hero(self, H1, H2, H3, H4):
        self.c.create_oval(H1, H2, H3, H4, fill='blue')

    def delete_obj(self, object_id):
        self.c.delete(object_id)

    def flash(self, object_id):
        if self.c.itemcget(object_id, 'fill') == 'yellow':
            self.c.itemconfig(object_id, fill='red')
            self.c.update()
        else:
            self.c.itemconfig(object_id, fill='yellow')
            self.c.update()

    def kill(self, object_id, count):
        count = count
        if count < 5:
            count += 1
            self.c.after(300, self.flash, object_id, count)
        self.delete_obj(object_id)
