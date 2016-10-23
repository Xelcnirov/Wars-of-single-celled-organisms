from math import sqrt
from random import randint
from Enemy import Enemy
from tkinter import *
#import World
from World import world, enemies
from Hero import Hero
from Animation import Animation
from Controls import *
from Camera import Camera


def get_distance(u1, u2):
    return sqrt((u1.x - u2.x)**2 + (u1.y - u2.y)**2)


def colliding(u1, u2):
    dist = get_distance(u1, u2)
    return dist <= u1.r + u2.r


def random_coords():
    x, y = randint(100, world['width']-100), randint(100, world['height']-100)
    return x, y


#def ticks(event):
#    for u1 in bad_units:
#        for u2 in bad_units:
#            if colliding(u1, u2):
#                u1.collide(u2)
#    for unit in bad_units:
#        unit.tick()
#    InSight()

hero = Hero()
good_units = []
bad_units = [Enemy(*random_coords()) for x in range(enemies)]
good_shots = []
bad_shots = []
camera = Camera()
c = Animation()

'''
def InSight():
    c.delete('all')
    draw(hero)
    # ticks()
    for object in bad_units:
        if (object.x > camera.x - object.r or object.y > camera.y - object.r) and \
                (object.x < camera.x + camera.w + object.r or object.y < camera.y + camera.h + object.r):
            draw(object)


def draw(object):
    c.create_oval([object.x - object.r - camera.x, object.y - object.r - camera.y],
                  [object.x + object.r - camera.x, object.y + object.r - camera.y], fill='yellow')
'''


def where(event):
    print(camera.x, camera.y, '\n', camera.x + camera.w, camera.y + camera.h)


for i in bad_units:
    print(i.x, i.y)

#c = Canvas(width=camera.w, height=camera.h, bg='black')
#c.pack()


#c.bind('a', camera.camleft)
#c.bind('d', camera.camright)
#c.bind('w', camera.camup)
#c.bind('s', camera.camdown)
c.c.bind('<space>', where)
c.c.bind('<Key>', key_pressed)  # <KeyPress>
c.c.bind('<KeyRelease>', key_release)  # <KeyRelease>
#c.bind('<Motion>', ticks)

#c.c.focus_set()

mainloop()
