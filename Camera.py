from tkinter import *
import random

world = {'x': 0, 'y': 0, 'w': 1000, 'h': 1000}
SPEED = 20

class Unit:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def moveleft(self):
        self.x -= SPEED

    def moveright(self):
        self.x += SPEED

    def moveup(self):
        self.y -= SPEED

    def movedown(self):
        self.y += SPEED


class Camera:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def moveleft(self):
        self.x -= SPEED

    def moveright(self):
        self.x += SPEED

    def moveup(self):
        self.y -= SPEED

    def movedown(self):
        self.y += SPEED


def InSight():

    c.delete('all')
    for object in Objects:
        if (object.x > camera.x - object.r or object.y > camera.y - object.r) and \
                (object.x < camera.x + camera.w + object.r or object.y < camera.y + camera.h + object.r):
            Draw(object)

def Draw(object):

        c.create_oval([object.x - object.r - camera.x, object.y - object.r - camera.y], [object.x + object.r - camera.x, object.y + object.r - camera.y], fill='yellow')

def camleft(event):
    camera.moveleft()
    InSight()
    if camera.x < world['x']:
        camera.x = world['x']

def camright(event):
    camera.moveright()
    InSight()
    if camera.x + camera.w > world['w']:
        camera.x = world['w'] - camera.w

def camup(event):
    camera.moveup()
    InSight()
    if camera.y < world['y']:
        camera.y = world['y']

def camdown(event):
    camera.movedown()
    InSight()
    if camera.y + camera.h > world['h']:
        camera.y = world['h'] - camera.h

def where(event):
    print(camera.x, camera.y, '\n', camera.x + camera.w, camera.y + camera.h)

camera = Camera(100, 100, 500, 500)
Objects = [Unit(random.randint(50, 950), random.randint(50, 950), 50) for x in range(5)]
for i in Objects:
    print(i.x, i.y)

c = Canvas(width=500, height=500, bg='black')
c.pack()
InSight()

c.bind('a', camleft)
c.bind('d', camright)
c.bind('w', camup)
c.bind('s', camdown)
c.bind('<space>', where)

c.focus_set()

mainloop()

