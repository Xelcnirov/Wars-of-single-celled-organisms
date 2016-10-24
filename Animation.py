from tkinter import *
from World import camera_size
#from Units import Unit
#from Camera import Camera

#camera = Unit(1, 1)


class Animation:
    def __init__(self, camera):
        self.camera = camera
        self.screen = Canvas(width=camera_size['width'], height=camera_size['height'], bg='black')
        self.screen.pack()
        self.screen.focus_set()

    def draw(self, object):
        object.visual = self.screen.create_oval([object.x - object.r - self.camera.x,
                                                 object.y - object.r - self.camera.y],
                                                [object.x + object.r - self.camera.x,
                                                 object.y + object.r - self.camera.y],
                                                fill=object.colour)

    #def draw_hero(self, H1, H2, H3, H4):
        #self.screen.create_oval(H1, H2, H3, H4, fill='blue')

    def delete_obj(self, object):
        self.screen.delete(object.visual)
        object.visual = None

    def flash(self, object):
        if self.screen.itemcget(object.visual, 'fill') == 'yellow':
            self.screen.itemconfig(object.visual, fill='red')
            self.screen.update()
        else:
            self.screen.itemconfig(object.visual, fill='yellow')
            self.screen.update()

    def kill(self, object, count=0):
        count = count
        if count < 5:
            self.flash(object)
            count += 1
            self.screen.after(300, self.kill, object, count)
        else:
            self.delete_obj(object)
'''
test = Animation()
test1 = Unit(100, 100)
test2 = Unit(200, 200)
test.draw(test1)
test.kill(test1, 0)
test.draw(test2)
test.kill(test2, 0)
test.draw(test2)
mainloop()
'''
