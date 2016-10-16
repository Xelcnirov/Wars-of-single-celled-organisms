from random import choice


class Unit:
    def __init__(self, x, y, r=50, shooting_range=150, speed=10):
        self.x = x
        self.y = y
        self.r = r
        self.id = str(id(self))
        self.group = self.__class__.__name__
        self.shooting_range = shooting_range  # may be subclass attribute
        self.speed = speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
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
