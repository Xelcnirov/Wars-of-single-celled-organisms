from Units import Unit
from World import start, world, HERO_MAX_SPEED


class Hero(Unit):
    def __init__(self):
        Unit.__init__(self, x=start['x'], y=start['y'], r=40, colour='blue')
        self.counter = 0
        self.speed_x = 0
        self.speed_y = 0
        self.max_speed = HERO_MAX_SPEED
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def tick(self):  # for fun
        if self.colour == 'green':
            self.counter += 1
        if self.counter > 15:
            self.counter = 0
            self.colour = 'blue'

    def move_up(self):
        if self.moving_up:
            if self.speed_y - 1 > -self.max_speed:
                self.speed_y -= 1
            else:
                self.speed_y = -self.max_speed
        else:
            if self.speed_y + 1 < 0:
                self.speed_y += 1
            else:
                self.speed_y = 0
        if self.y + self.speed_y <= world['y'] + self.r:
            self.y = world['y'] + self.r
        else:
            self.y += self.speed_y

    def move_down(self):
        if self.moving_down:
            if self.speed_y + 1 < self.max_speed:
                self.speed_y += 1
            else:
                self.speed_y = self.max_speed
        else:
            if self.speed_y - 1 > 0:
                self.speed_y -= 1
            else:
                self.speed_y = 0
        if self.y + self.speed_y >= world['height'] - self.r:
            self.y = world['height'] - self.r
        else:
            self.y += self.speed_y

    def move_left(self):
        if self.moving_left:
            if self.speed_x - 1 > -self.max_speed:
                self.speed_x -= 1
            else:
                self.speed_x = -self.max_speed
        else:
            if self.speed_x + 1 < 0:
                self.speed_x += 1
            else:
                self.speed_x = 0
        if self.x + self.speed_x <= world['x'] + self.r:
            self.x = world['x'] + self.r
        else:
            self.x += self.speed_x

    def move_right(self):
        if self.moving_right:
            if self.speed_x + 1 < self.max_speed:
                self.speed_x += 1
            else:
                self.speed_x = self.max_speed
        else:
            if self.speed_x - 1 > 0:
                self.speed_x -= 1
            else:
                self.speed_x = 0
        if self.x + self.speed_x >= world['width'] - self.r:
            self.x = world['width'] - self.r
        else:
            self.x += self.speed_x

    def collide(self, another_object):
        self.colour = 'green'
