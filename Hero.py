from Units import Unit
from World import spawn, camera_size, world


class Hero(Unit):
    def __init__(self):
        Unit.__init__(self, x=spawn['x'], y=spawn['y'], r=40, speed=20)

    def tick(self): pass

    def move_up(self):
        if self.y - self.speed >= world['y'] + camera_size['height']//2:
            self.y -= self.speed

    def move_down(self):
        if self.y + self.speed <= world['height'] - camera_size['height']//2:
            self.y += self.speed

    def move_left(self):
        if self.x - self.speed >= world['x'] + camera_size['width']//2:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.speed <= world['width'] - camera_size['width']//2:
            self.x += self.speed
