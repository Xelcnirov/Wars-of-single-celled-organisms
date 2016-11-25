from math import sqrt
from random import randint
from Enemy import Enemy
from tkinter import mainloop
from World import world, ENEMIES, DELAY, FOOD
from Hero import Hero
from Animation import Animation
from Controls import Controls
from Camera import Camera
import time


# def get_distance(u1, u2):
#     if abs(u1.x - u2.x) <= u1.r + u2.r >= abs(u1.y - u2.y):
#         return sqrt((u1.x - u2.x)**2 + (u1.y - u2.y)**2)
#     else:
#         return False


def colliding(u1, u2):
    dist = sqrt((u1.x - u2.x)**2 + (u1.y - u2.y)**2)
    return dist <= u1.r + u2.r


def random_coords():
    x, y = randint(100, world['width']-100), randint(100, world['height']-100)
    return x, y


flag = 1


def ticks():  # event
    t = time.time()
    food_copy = food[:]
    good_shots_copy = good_shots[:]
    # bad_shots_copy = bad_shots[:]
    bad_units_copy = bad_units[:]
    animation.screen.delete('all')
    animation.check_border()
    # len_b_units = len(bad_units_copy)
    # len_g_shots = len(good_shots_copy)

    animation.insight(food + good_shots + [hero] + bad_units)

    for shot in good_shots_copy:
        shot.tick()

    # for unit in bad_units_copy + food_copy:
    #     if abs(unit.x - hero.x) <= unit.r + hero.r >= abs(unit.y - hero.y):
    #         if colliding(unit, hero):
    #             unit.collide(hero)
    #             hero.collide(unit)
    # hero.tick()
    collide_checker = 1
    for unit_1 in bad_units_copy + food_copy:
        for unit_2 in (bad_units_copy + food_copy + good_shots_copy)[collide_checker:]:
            if abs(unit_1.x - unit_2.x) <= unit_1.vision_range >= abs(unit_1.y - unit_2.y):
                if unit_1.group == 'Enemy' and unit_2.group == 'Food':
                    if unit_1.level == 2:
                        unit_1.move_to(unit_2)
                if sqrt((unit_1.x - unit_2.x)**2 + (unit_1.y - unit_2.y)**2) < unit_1.r + unit_2.r:
                    unit_1.collide(unit_2)
                    unit_2.collide(unit_1)
        unit_1.tick()
        collide_checker += 1
        if abs(unit_1.x - hero.x) <= unit_1.r + hero.r >= abs(unit_1.y - hero.y):
            if sqrt((unit_1.x - hero.x)**2 + (unit_1.y - hero.y)**2) < unit_1.r + hero.r:
                unit_1.collide(hero)
                hero.collide(unit_1)
    hero.tick()
    # collide_checker = 0
    # for unit_1 in bad_units_copy:
    #     for unit_2 in (bad_units_copy + good_shots_copy)[collide_checker:]:
    #         # if colliding(unit_1, unit_2):
    #         if unit_2.group == 'Enemy':
    #             if unit_1.level - unit_2.level == 1 or unit_1.level - unit_2.level == 2:
    #                 if abs(unit_1.x - unit_2.x) <= unit_1.vision_range >= abs(unit_1.y - unit_2.y):
    #                     unit_1.move_to(unit_2)
    #             if unit_2.level - unit_1.level == 1 or unit_2.level - unit_1.level == 2:
    #                 if abs(unit_1.x - unit_2.x) <= unit_2.vision_range >= abs(unit_1.y - unit_2.y):
    #                     unit_2.move_to(unit_1)
    #         if abs(unit_1.x - unit_2.x) <= unit_1.r + unit_2.r >= abs(unit_1.y - unit_2.y):
    #             if colliding(unit_1, unit_2):
    #                 unit_1.collide(unit_2)
    #                 unit_2.collide(unit_1)
    #     unit_1.tick()
    #     collide_checker += 1
    t2 = int((time.time() - t) * 100)
    if flag:
        global flag
        flag = 0
        print('%.6f' % (time.time() - t), t2)
    animation.screen.after(DELAY - t2, ticks)


good_units = []
bad_units = []
good_shots = []
bad_shots = []
food = []
bad_units.extend([Enemy(*random_coords(), bad_units, level=1) for x in range(ENEMIES)])
food.extend([Enemy(*random_coords(), food, level=0) for y in range(FOOD)])

camera = Camera()
hero = Hero(camera)
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
#screen.screen.focus_set()

mainloop()
