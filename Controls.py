from Hero import Hero
from tkinter import *
from Camera import Camera

camera = Camera()
c = Canvas(width=camera.w, height=camera.h, bg='black')

hero = Hero()


def key_pressed(event):
    #print(repr(event.char))
    if event.char in keys:
        if not keys[event.char][0]:
            keys[event.char][0] = 1
            keys[event.char][1](event.char, camera, hero, c)


def key_release(event):
    print('release', repr(event.char))
    if event.char in keys:
        keys[event.char][0] = 0


def up(char):  # camera, hero, c
    print('y', camera.y, hero.y)
    hero.move_up()
    camera.camup()
    if keys[char][0]:
        c.after(200, up, char)


def down(char):
    print('y', camera.y, hero.y)
    hero.move_down()
    camera.camdown()
    if keys[char][0]:
        c.after(200, keys[char][1], char)


def left(char):
    print('x', camera.x, hero.x)
    hero.move_left()
    camera.camleft()
    if keys[char][0]:
        c.after(200, keys[char][1], char)


def right(char):
    print('x', camera.x, hero.x)
    hero.move_right()
    camera.camright()
    if keys[char][0]:
        c.after(200, keys[char][1], char)

keys = {'w': [0, up],
        's': [0, down],
        'a': [0, left],
        'd': [0, right]}

#c.pack()

#c.bind('<Key>', key_pressed)  # <KeyPress>
#c.bind('<KeyRelease>', key_release)  # <KeyRelease>
#c.focus_set()
#mainloop()
