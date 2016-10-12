class Unit:
    def __init__(self, x, y, shooting_range, r=50):
        self.x = x
        self.y = y
        self.r = r
        self.id = str(id(self))
        self.shooting_range = shooting_range #may be subclass attribute

    def colliding(self, another_object):
        if another_obect is hero:
            self.kill()
        else:
            self.avoid(another_object)

    def tick(self):

    def kill(self): #Object destruction function
        canvas.delete(self)

    def move_to(self, ax, ay):
        if self.x > ax:
            self.x -= 1
        elif self.x < ax:
            self.x += 1
        if self.y > ay:
            self.y -= 1
        elif self.y < ay:
            self.y += 1

    def move_away(self, ax, ay):
        if self.x > ax:
            self.x += 1
        elif self.x < ax:
            self.x -= 1
        if self.y > ay:
            self.y += 1
        elif self.y < ay:
            self.y -= 1

    def shoot(self): #Doesnt need args, always shoots at hero
        pass

    def behavior(self): #AI
        if distance_to_hero <= number:
            self.move_to(hero.x, hero.y)
            if distance_to_hero <= self.shooting_range:
                self.shoot()

    def avoid(self, another_object):
        self.move_away(another_object.x, another_object.y)

