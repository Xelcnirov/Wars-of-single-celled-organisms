from Projectile import Projectile
from World import DELAY


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

    def key_pressed(self, event):
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
            self.hero.moving_up = True
            self.hero.move_up()
            self.camera.camup(self.hero.speed_y)
            print('y', self.camera.y, self.hero.y)
            self.screen.after(DELAY, self.keys[char][1], char)
        elif not self.keys[char][0]:
            self.hero.moving_up = False
            if self.hero.speed_y < 0 and not self.hero.moving_down:
                self.hero.move_up()
                self.camera.camup(self.hero.speed_y)
                print('y2', self.camera.y, self.hero.y)
                self.screen.after(DELAY, self.keys[char][1], char)

    def down(self, char):
        if self.keys[char][0]:
            self.hero.moving_down = True
            self.hero.move_down()
            self.camera.camdown(self.hero.speed_y)
            print('y', self.camera.y, self.hero.y)
            self.screen.after(DELAY, self.keys[char][1], char)
        elif not self.keys[char][0]:
            self.hero.moving_down = False
            if self.hero.speed_y > 0 and not self.hero.moving_up:
                self.hero.move_down()
                self.camera.camdown(self.hero.speed_y)
                print('y2', self.camera.y, self.hero.y)
                self.screen.after(DELAY, self.keys[char][1], char)

    def left(self, char):
        if self.keys[char][0]:
            self.hero.moving_left = True
            self.hero.move_left()
            self.camera.camleft(self.hero.speed_x)
            print('x', self.camera.x, self.hero.x)
            self.screen.after(DELAY, self.keys[char][1], char)
        elif not self.keys[char][0]:
            self.hero.moving_left = False
            if self.hero.speed_x < 0 and not self.hero.moving_right:
                self.hero.move_left()
                self.camera.camleft(self.hero.speed_x)
                print('x2', self.camera.x, self.hero.x)
                self.screen.after(DELAY, self.keys[char][1], char)

    def right(self, char):
        if self.keys[char][0]:
            self.hero.moving_right = True
            self.hero.move_right()
            self.camera.camright(self.hero.speed_x)
            print('x', self.camera.x, self.hero.x)
            self.screen.after(DELAY, self.keys[char][1], char)
        elif not self.keys[char][0]:
            self.hero.moving_right = False
            if self.hero.speed_x > 0 and not self.hero.moving_left:
                self.hero.move_right()
                self.camera.camright(self.hero.speed_x)
                print('x2', self.camera.x, self.hero.x)
                self.screen.after(DELAY, self.keys[char][1], char)

    def click(self, event):
        self.good_shots.append(Projectile(self.hero.x, self.hero.y, event.x + self.camera.x, event.y + self.camera.y))
        print(event.x, event.y)
