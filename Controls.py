from Projectile import Projectile
from World import DELAY


class Controls:

    def __init__(self, camera, hero, screen, good_shots):
        self.keys = {'w': [0, self.up, self.stop_up],
                     's': [0, self.down, self.stop_down],
                     'a': [0, self.left, self.stop_left],
                     'd': [0, self.right, self.stop_right]}
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
            # self.keys[event.char][2](event.char)

    def up(self, char):
        if self.keys[char][0]:
            self.hero.moving['up'] = True
            self.hero.move_up()
            # self.camera.camup(self.hero.speed['y_up'])
            #print('y', self.camera.y, self.hero.y)
            self.screen.after(DELAY, self.keys[char][1], char)
        else:
            self.keys[char][2](char)

    def down(self, char):
        if self.keys[char][0]:
            self.hero.moving['down'] = True
            self.hero.move_down()
            # self.camera.camdown(self.hero.speed['y_down'])
            #print('y', self.camera.y, self.hero.y)
            self.screen.after(DELAY, self.keys[char][1], char)
        else:
            self.keys[char][2](char)

    def left(self, char):
        if self.keys[char][0]:
            self.hero.moving['left'] = True
            self.hero.move_left()
            # self.camera.camleft(self.hero.speed['x_left'])
            #print('x', self.camera.x, self.hero.x)
            self.screen.after(DELAY, self.keys[char][1], char)
        else:
            self.keys[char][2](char)

    def right(self, char):
        if self.keys[char][0]:
            self.hero.moving['right'] = True
            self.hero.move_right()
            # self.camera.camright(self.hero.speed['x_right'])
            #print('x', self.camera.x, self.hero.x)
            self.screen.after(DELAY, self.keys[char][1], char)
        else:
            self.keys[char][2](char)

    def stop_up(self, char):
        if not self.keys[char][0]:
            self.hero.moving['up'] = False
            if self.hero.speed['y_up'] < 0:
                self.hero.move_up()
                # self.camera.camup(self.hero.speed['y_up'])
                #print('y2', self.camera.y, self.hero.y)
                self.screen.after(DELAY, self.keys[char][2], char)
            # else:
            #     self.hero.speed['y_up'] = 0

    def stop_down(self, char):
        if not self.keys[char][0]:
            self.hero.moving['down'] = False
            if self.hero.speed['y_down'] > 0:
                self.hero.move_down()
                # self.camera.camdown(self.hero.speed['y_down'])
                #print('y2', self.camera.y, self.hero.y)
                self.screen.after(DELAY, self.keys[char][2], char)
            # else:
            #     self.hero.speed['y_down'] = 0

    def stop_left(self, char):
        if not self.keys[char][0]:
            self.hero.moving['left'] = False
            if self.hero.speed['x_left'] < 0:
                self.hero.move_left()
                # self.camera.camleft(self.hero.speed['x_left'])
                #print('x2', self.camera.x, self.hero.x)
                self.screen.after(DELAY, self.keys[char][2], char)
            # else:
            #     self.hero.speed['x_left'] = 0

    def stop_right(self, char):
        if not self.keys[char][0]:
            self.hero.moving['right'] = False
            if self.hero.speed['x_right'] > 0:
                self.hero.move_right()
                # self.camera.camright(self.hero.speed['x_right'])
                #print('x2', self.camera.x, self.hero.x)
                self.screen.after(DELAY, self.keys[char][2], char)
            # else:
            #     self.hero.speed['x_right'] = 0

    def click(self, event):
        self.good_shots.append(Projectile(self.hero.x, self.hero.y,
                                          event.x + self.camera.x, event.y + self.camera.y,
                                          'Good_shots'))
        print(event.x, event.y)
