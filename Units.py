from random import choice
from World import world


class Unit:
    def __init__(self, x, y, r=50, shooting_range=150, speed=10, visual=True, colour='yellow'):
        self.x = x
        self.y = y
        self.r = r
        self.id = str(id(self))
        self.group = self.__class__.__name__
        self.shooting_range = shooting_range  # may be subclass attribute
        self.speed = speed
        self.visual = visual
        self.colour = colour

    def move_up(self):
        if self.y - self.r - self.speed >= world['y']:
            self.y -= self.speed

    def move_down(self):
        if self.y + self.r + self.speed <= world['height']:
            self.y += self.speed

    def move_left(self):
        if self.x - self.r - self.speed >= world['x']:
            self.x -= self.speed

    def move_right(self):
        if self.x + self.r + self.speed <= world['width']:
            self.x += self.speed

    def collide(self, another_object):  # need World's collide func
        self.move_away(another_object.x, another_object.y)

    def tick(self):  # frame actions here
        choice([self.move_down, self.move_up, self.move_left, self.move_right])()

    def kill(self):  # Object destruction function
        # canvas.delete(self)
        pass

    def move_to(self, ax, ay):
        if self.x > ax:
            self.move_left()
        elif self.x < ax:
            self.move_right()
        if self.y > ay:
            self.move_up()
        elif self.y < ay:
            self.move_down()

    def move_away(self, ax, ay):
        if self.x > ax:
            self.move_right()
        elif self.x < ax:
            self.move_left()
        if self.y > ay:
            self.move_down()
        elif self.y < ay:
            self.move_up()

    def shoot(self):  # Doesn't need args, always shoots at hero
        pass
