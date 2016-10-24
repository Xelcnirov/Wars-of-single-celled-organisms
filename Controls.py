#from Hero import Hero
#from tkinter import *
#from Camera import Camera

#camera = Camera()
#screen = Canvas(width=camera.w, height=camera.h, bg='black')
#hero = Hero()
from Projectile import Projectile

class Controls:

    def __init__(self, camera, hero, screen, good_shots):
        self.keys = {'w': [0, self.up],
                     's': [0, self.down],
                     'a': [0, self.left],
                     'd': [0, self.right]}
        self.camera = camera
        self.hero = hero
        self.screen = screen
        self.good_shots = good_shots

    def key_pressed(self, event):  # camera, hero, screen
        # print(repr(event.char))
        if event.char in self.keys:
            if not self.keys[event.char][0]:
                self.keys[event.char][0] = 1
                self.keys[event.char][1](event.char)

    def key_release(self, event):
        print('release', repr(event.char))
        if event.char in self.keys:
            self.keys[event.char][0] = 0

    def up(self, char):
        if self.keys[char][0]:
            self.hero.move_up()
            self.camera.camup()
            print('y', self.camera.y, self.hero.y)
            self.screen.after(100, self.up, char)

    def down(self, char):
        if self.keys[char][0]:
            self.hero.move_down()
            self.camera.camdown()
            print('y', self.camera.y, self.hero.y)
            self.screen.after(100, self.keys[char][1], char)

    def left(self, char):
        if self.keys[char][0]:
            self.hero.move_left()
            self.camera.camleft()
            print('x', self.camera.x, self.hero.x)
            self.screen.after(100, self.keys[char][1], char)

    def right(self, char):
        if self.keys[char][0]:
            self.hero.move_right()
            self.camera.camright()
            print('x', self.camera.x, self.hero.x)
            self.screen.after(100, self.keys[char][1], char)

    def click(self, event):
        self.good_shots.append(Projectile(self.hero.x, self.hero.y, event.x + self.camera.x, event.y + self.camera.y))
        print(event.x, event.y)
'''

def key_release(event):
    print('release', repr(event.char))
    if event.char in keys:
        keys[event.char][0] = 0


def up(char):  # camera, hero, screen
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
'''
#screen.pack()

#screen.bind('<Key>', a.key_pressed)  # <KeyPress>
#screen.bind('<KeyRelease>', a.key_release)  # <KeyRelease>
#screen.focus_set()
#mainloop()
