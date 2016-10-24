from Units import Unit
from World import start, world, hero_speed


class Hero(Unit):
    def __init__(self):
        Unit.__init__(self, x=start['x'], y=start['y'], r=40, speed=hero_speed, colour='blue')
        self.counter = 0

    def tick(self):  # for fun
        if self.colour == 'green':
            self.counter += 1
        if self.counter > 15:
            self.counter = 0
            self.colour = 'blue'

    def move_up(self):
        if self.y - self.speed <= world['y'] + self.r:
            self.y = world['y'] + self.r
        else:
            self.y -= self.speed

    def move_down(self):
        if self.y + self.speed >= world['height'] - self.r:
            self.y = world['height'] - self.r
        else:
            self.y += self.speed
            # if self.y + self.speed <= world['height'] - camera_size['height']//2:
            #    self.y += self.speed

    def move_left(self):
        if self.x - self.speed <= world['x'] + self.r:
            self.x = world['x'] + self.r
        else:
            self.x -= self.speed
            # if self.x - self.speed >= world['x'] + camera_size['width']//2:
            #    self.x -= self.speed

    def move_right(self):
        if self.x + self.speed >= world['width'] - self.r:
            self.x = world['width'] - self.r
        else:
            self.x += self.speed
            # if self.x + self.speed <= world['width'] - camera_size['width']//2:
            #    self.x += self.speed

    def collide(self, another_object):
        self.colour = 'green'
