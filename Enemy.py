from Units import Unit


class Enemy(Unit):
    def __init__(self, x, y, listed, vision_range=150, level=0, health=1, exp=0, damage=0):
        Unit.__init__(self, x, y, colour='#6d2f84')
        self.logic = {1: {'r': 14, 'speed': 2, 'vision_range': 50, 'health': 1, 'damage': 0, 'colour': '#6d2f84'},
                      2: {'r': 32, 'speed': 12, 'vision_range': 140, 'health': 2, 'damage': 1, 'colour': '#753e58'},
                      3: {'r': 47, 'speed': 10, 'vision_range': 160, 'health': 3, 'damage': 2, 'colour': '#774e2c'},
                      4: {'r': 65, 'speed': 8, 'vision_range': 200, 'health': 4, 'damage': 3, 'colour': '#a39b49'},
                      5: {'r': 80, 'speed': 4, 'vision_range': 220, 'health': 6, 'damage': 3, 'colour': '#6aa349'}}
        self.vision_range = vision_range
        self.level = level
        self.health = health
        self.exp = exp
        self.damage = damage
        self.level_up()
        self.alive = True
        self.counter = 0
        self.listed = listed

    def get_ability(self):
        pass

    def level_up(self):
        self.level += 1
        self.r = self.logic[self.level]['r']
        self.speed = self.logic[self.level]['speed']
        self.vision_range = self.logic[self.level]['vision_range']
        self.health = self.logic[self.level]['health']
        self.damage = self.logic[self.level]['damage']
        self.colour = self.logic[self.level]['colour']
        self.get_ability()
        self.exp = 0

    def collide(self, another_object):
        if another_object.group == 'Hero':
            # print('hoho')
            Unit.collide(self, another_object)
        elif another_object.group == 'Good_shots':
            # print('yeye')
            pass
        else:
            if 1 < self.level < 5:
                if self.level - another_object.level == 1 or self.level - another_object.level == 2:
                    another_object.alive = False
                    self.exp += 1
                else:
                    # another_object.health -= self.logic[self.level]['damage']
                    # if another_object.health <= 0:
                    #     another_object.kill()
                    #     self.exp += 1
                    Unit.collide(self, another_object)
            else:
                Unit.collide(self, another_object)

    def tick(self):
        self.counter += 1
        if self.counter > 3:
            Unit.tick(self)
            self.counter = 0
        if not self.alive:
            self.listed.remove(self)
        if self.exp >= 3 and self.level < 5:
            self.level_up()

    def move_to(self, another_object):
        if 1 < self.level < 5:
            if self.x > another_object.x:
                self.move_left()
            elif self.x < another_object.x:
                self.move_right()
            if self.y > another_object.y:
                self.move_up()
            elif self.y < another_object.y:
                self.move_down()

    def kill(self):  # Object destruction function
        # canvas.delete(self)
        pass
