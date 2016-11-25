from random import choice, randint
from World import world, SLAM_RATE, ENEMY_MAX_SPEED


class Unit:
    def __init__(self, x, y, r=50, shooting_range=150, speed=10, visual=True, colour='yellow'):
        self.x = x
        self.y = y
        self.r = r
        self.id = str(id(self))
        self.group = self.__class__.__name__
        self.shooting_range = shooting_range  # may be subclass attribute
        # self.speed = speed
        self.visual = visual
        self.colour = colour
        self.moving = {'up': False,
                       'down': False,
                       'right': False,
                       'left': False}
        self.speed = {'y_up': 0,
                      'y_down': 0,
                      'x_right': 0,
                      'x_left': 0}
        self.max_speed = ENEMY_MAX_SPEED

    def move_up(self):
        # if self.y - self.r - self.speed >= world['y']:
        #     self.y -= self.speed
        if self.moving['up']:
            if self.speed['y_up'] - 1 >= -self.max_speed:
                self.speed['y_up'] -= 1
        else:
            if self.speed['y_up'] + 1 <= 0:
                self.speed['y_up'] += 1
        if self.y + self.speed['y_up'] <= world['y'] + self.r:
            self.y = world['y'] + self.r
        else:
            self.y += self.speed['y_up']

    def move_down(self):
        # if self.y + self.r + self.speed <= world['height']:
        #     self.y += self.speed
        if self.moving['down']:
            if self.speed['y_down'] + 1 <= self.max_speed:
                self.speed['y_down'] += 1
        else:
            if self.speed['y_down'] - 1 >= 0:
                self.speed['y_down'] -= 1
        if self.y + self.speed['y_down'] >= world['height'] - self.r:
            self.y = world['height'] - self.r
        else:
            self.y += self.speed['y_down']

    def move_left(self):
        # if self.x - self.r - self.speed >= world['x']:
        #     self.x -= self.speed
        if self.moving['left']:
            if self.speed['x_left'] - 1 >= -self.max_speed:
                self.speed['x_left'] -= 1
        else:
            if self.speed['x_left'] + 1 <= 0:
                self.speed['x_left'] += 1
        if self.x + self.speed['x_left'] <= world['x'] + self.r:
            self.x = world['x'] + self.r
        else:
            self.x += self.speed['x_left']

    def move_right(self):
        # if self.x + self.r + self.speed <= world['width']:
        #     self.x += self.speed
        if self.moving['right']:
            if self.speed['x_right'] + 1 <= self.max_speed:
                self.speed['x_right'] += 1
        else:
            if self.speed['x_right'] - 1 >= 0:
                self.speed['x_right'] -= 1
        if self.x + self.speed['x_right'] >= world['width'] - self.r:
            self.x = world['width'] - self.r
        else:
            self.x += self.speed['x_right']

    def collide(self, another_object):  # need World's collide func
        self.move_away(another_object)

    # def tick(self):  # frame actions here
    #     choice([self.move_down, self.move_up, self.move_left, self.move_right])()

    # def tick(self):  # frame actions here
    #     a = choice([self.move_down, self.move_up, self.hold])
    #     b = choice([self.move_left, self.move_right, self.hold])
    #     c = randint(1, 2)
    #     for i in range(c):
    #         a()
    #         b()

    def hold(self):
        pass

    # def kill(self):  # Object destruction function
    #     # canvas.delete(self)
    #     pass

    # def move_to(self, another_object):
    #     if self.x > another_object.x:
    #         self.move_left()
    #     elif self.x < another_object.x:
    #         self.move_right()
    #     if self.y > another_object.y:
    #         self.move_up()
    #     elif self.y < another_object.y:
    #         self.move_down()

    # def move_away(self, another_object):
    #     if self.x > another_object.x:
    #         self.move_right()
    #     elif self.x < another_object.x:
    #         self.move_left()
    #     if self.y > another_object.y:
    #         self.move_down()
    #     elif self.y < another_object.y:
    #         self.move_up()
    def move_away(self, another_object):
        if self.x > another_object.x and self.x + self.r + SLAM_RATE <= world['width']:
            # self.move_right()
            self.x += SLAM_RATE
        elif self.x < another_object.x and self.x - self.r - SLAM_RATE >= world['x']:
            # self.move_left()
            self.x -= SLAM_RATE
        if self.y > another_object.y and self.y + self.r + SLAM_RATE <= world['height']:
            # self.move_down()
            self.y += SLAM_RATE
        elif self.y < another_object.y and self.y - self.r - SLAM_RATE >= world['y']:
            # self.move_up()
            self.y -= SLAM_RATE

    def shoot(self):  # Doesn't need args, always shoots at hero
        pass
