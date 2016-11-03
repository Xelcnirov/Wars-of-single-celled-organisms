from tkinter import *
from World import camera_size, world


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
                                                fill='#1c2635', width=5, outline=object.colour)

    def draw_border_left(self):
        self.line = self.screen.create_line([world['x'] - self.camera.x, world['y'] - self.camera.y],
                                            [world['x'] - self.camera.x, world['height'] - self.camera.y],
                                            width=5, fill='#427c0b')

    def draw_border_up(self):
        self.line = self.screen.create_line([world['x'] - self.camera.x, world['y'] - self.camera.y],
                                            [world['width'] - self.camera.x, world['y'] - self.camera.y],
                                            width=5, fill='#427c0b')

    def draw_border_right(self):
        self.line = self.screen.create_line([world['width'] - self.camera.x, world['height'] - self.camera.y],
                                            [world['width'] - self.camera.x, world['y'] - self.camera.y],
                                            width=5, fill='#427c0b')

    def draw_border_down(self):
        self.line = self.screen.create_line([world['width'] - self.camera.x, world['height'] - self.camera.y],
                                            [world['x'] - self.camera.x, world['height'] - self.camera.y],
                                            width=5, fill='#427c0b')

    def insight(self, object):
        if (object.x > self.camera.x - object.r and object.y > self.camera.y - object.r) and \
                (object.x < self.camera.x + self.camera.w + object.r and
                         object.y < self.camera.y + self.camera.h + object.r):
            self.draw(object)

    def check_border(self):
        if world['y'] - self.camera.h // 2 <= self.camera.y:
            self.draw_border_left()
        if world['x'] - self.camera.w // 2 <= self.camera.x:
            self.draw_border_up()
        if world['width'] <= self.camera.x + self.camera.w:
            self.draw_border_right()
        if world['height'] <= self.camera.y + self.camera.h:
            self.draw_border_down()

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
