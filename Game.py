from math import sqrt
from random import randint
from Enemy import Enemy
from tkinter import mainloop
from World import world, enemies
from Hero import Hero
from Animation import Animation
from Controls import Controls
from Camera import Camera


def get_distance(u1, u2):
    return sqrt((u1.x - u2.x)**2 + (u1.y - u2.y)**2)


def colliding(u1, u2):
    dist = get_distance(u1, u2)
    return dist <= u1.r + u2.r


def random_coords():
    x, y = randint(100, world['width']-100), randint(100, world['height']-100)
    return x, y


def ticks():  # event
    #animation.screen.delete('all')
    for x in bad_units + [hero]:
        animation.delete_obj(x)
        animation.draw(x)
    #animation.draw(hero)
    for u1 in bad_units + [hero]:
        for u2 in bad_units:
            if colliding(u1, u2):
                u1.collide(u2)
                u2.collide(u1)
    #for unit in bad_units + [hero]:
    #    unit.tick()
    hero.tick()
    animation.screen.after(100, ticks)
#    InSight()


hero = Hero()
good_units = []
bad_units = [Enemy(*random_coords()) for x in range(enemies)]
good_shots = []
bad_shots = []
camera = Camera()
animation = Animation(camera)
controls = Controls(camera, hero, animation.screen)


def where(event):
    print(camera.x, camera.y, '\n', camera.x + camera.w, camera.y + camera.h)


for i in bad_units:
    print(i.x, i.y)

animation.draw(hero)
ticks()
animation.screen.bind('<space>', where)
animation.screen.bind('<Key>', controls.key_pressed)  # <KeyPress>
animation.screen.bind('<KeyRelease>', controls.key_release)  # <KeyRelease>
#screen.bind('<Motion>', ticks)
#screen.screen.focus_set()

mainloop()
