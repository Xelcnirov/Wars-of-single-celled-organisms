from Units import Unit


class Enemy(Unit):
    def __init__(self, x, y, vision_range=150, level=0, health=1, exp=0, damage=0):
        Unit.__init__(self, x, y, colour='#6d2f84')
        self.logic = {1: {'r': 14, 'speed': 0, 'vision_range': 50, 'health': 1, 'damage': 0},
                      2: {'r': 32, 'speed': 12, 'vision_range': 100, 'health': 2, 'damage': 1},
                      3: {'r': 47, 'speed': 10, 'vision_range': 150, 'health': 3, 'damage': 2},
                      4: {'r': 65, 'speed': 8, 'vision_range': 180, 'health': 4, 'damage': 3},
                      5: {'r': 80, 'speed': 4, 'vision_range': 200, 'health': 6, 'damage': 3}}
        self.vision_range = vision_range
        self.level = level
        self.health = health
        self.exp = exp
        self.damage = damage
        self.level_up()

    def get_ability(self):
        pass

    def level_up(self):
        self.level += 1
        self.r = self.logic[self.level]['r']
        self.speed = self.logic[self.level]['speed']
        self.vision_range = self.logic[self.level]['vision_range']
        self.health = self.logic[self.level]['health']
        self.damage = self.logic[self.level]['damage']
        self.get_ability()
        self.exp = 0

    def collide(self, another_object):
        if another_object.group == 'Hero':
            print('hoho')
            Unit.collide(self, another_object)
        else:
            if self.level - another_object.level == (1 or 2):
                another_object.kill()
                self.exp += 1
            else:
                # another_object.health -= self.logic[self.level]['damage']
                # if another_object.health <= 0:
                #     another_object.kill()
                #     self.exp += 1
                Unit.collide(self, another_object)

    def tick(self):
        Unit.tick(self)
        if self.exp >= 5 > self.level:
            self.level_up()
