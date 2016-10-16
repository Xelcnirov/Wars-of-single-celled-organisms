from math import sqrt
from random import randint
# from Enemy import Enemy
from Units import Unit
from tkinter import *

world = {'x': 0,
         'y': 0,
         'w': 1000,
         'h': 1000}

enemies = 6  # count of enemies


def get_distance(u1, u2):
    return sqrt((u1.x - u2.x)**2 + (u1.y - u2.y)**2)


def colliding(u1, u2):
    dist = get_distance(u1, u2)
    return dist <= u1.r + u2.r


def random_coords():
    x, y = randint(100, world['w']-100), randint(100, world['h']-100)
    return x, y


def ticks():
    for u1 in bad_units:
        for u2 in bad_units:
            if colliding(u1, u2):
                u1.collide(u2)
    for unit in bad_units:
        unit.tick()


good_units = []
bad_units = [Unit(*random_coords()) for x in range(enemies)]  # replace Unit by Enemy
good_shots = []
bad_shots = []


SPEED = 20


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
    ticks()
    for object in bad_units:
        if (object.x > camera.x - object.r or object.y > camera.y - object.r) and \
                (object.x < camera.x + camera.w + object.r or object.y < camera.y + camera.h + object.r):
            Draw(object)


def Draw(object):
    c.create_oval([object.x - object.r - camera.x, object.y - object.r - camera.y],
                  [object.x + object.r - camera.x, object.y + object.r - camera.y], fill='yellow')


def camleft(event):
    if camera.x <= world['x']:
        camera.x = world['x']
    else:
        camera.moveleft()
        InSight()


def camright(event):
    if camera.x + camera.w >= world['w']:
        camera.x = world['w'] - camera.w
    else:
        camera.moveright()
        InSight()


def camup(event):
    if camera.y <= world['y']:
        camera.y = world['y']
    else:
        camera.moveup()
        InSight()


def camdown(event):
    if camera.y + camera.h >= world['h']:
        camera.y = world['h'] - camera.h
    else:
        camera.movedown()
        InSight()


def where(event):
    print(camera.x, camera.y, '\n', camera.x + camera.w, camera.y + camera.h)


camera = Camera(100, 100, 500, 500)
# Objects = [Enemy(*random_coords()) for x in range(enemies)]
for i in bad_units:
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

