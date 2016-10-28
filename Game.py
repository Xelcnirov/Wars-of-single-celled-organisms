from math import sqrt
from random import randint
from Enemy import Enemy
from tkinter import mainloop
from World import world, enemies, DELAY
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
    animation.screen.delete('all')
    for x in good_shots + bad_units + [hero]:
        #animation.delete_obj(x)
        animation.insight(x)
    for u1 in bad_units + [hero]:
        for u2 in bad_units:
            if u1 == u2:
                pass
            elif colliding(u1, u2):
                u1.collide(u2)
                u2.collide(u1)
    for x in good_shots:
        if x.step == 0:
            animation.delete_obj(x)
            good_shots.remove(x)
    for u1 in bad_units:
        for u2 in good_shots:
            if colliding(u1, u2):
                # u1.collide(u2)
                u2.collide()
    for unit in bad_units:
        # if unit.exp >= 5 > unit.level:
        #     unit.level_up()
        if 1 < unit.level < 5:
            for x in bad_units:
                if get_distance(unit, x) <= unit.vision_range:
                    if unit.level - x.level == (1 or 2):
                        unit.move_to(x)
                        # print('moving')
                        # break
        else:
            unit.tick()
    for x in good_shots:
        x.tick()
    hero.tick()
    animation.screen.after(DELAY, ticks)


hero = Hero()
good_units = []
bad_units = [Enemy(*random_coords(), level=randint(0, 1)) for x in range(enemies)]
good_shots = []
bad_shots = []
camera = Camera()
animation = Animation(camera)
controls = Controls(camera, hero, animation.screen, good_shots)


def where(event):
    print(camera.x, camera.y, '\n', camera.x + camera.w, camera.y + camera.h)


# for i in bad_units:
#     print(i.x, i.y)

#animation.draw(hero)
ticks()
animation.screen.bind('<space>', where)
animation.screen.bind('<Key>', controls.key_pressed)  # <KeyPress>
animation.screen.bind('<KeyRelease>', controls.key_release)  # <KeyRelease>
animation.screen.bind('<Button-1>', controls.click)
#screen.bind('<Motion>', ticks)
#screen.screen.focus_set()

mainloop()
