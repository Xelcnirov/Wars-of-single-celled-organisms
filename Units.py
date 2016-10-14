class Unit:
    def __init__(self, x, y, shooting_range=150, r=50):
        self.x = x
        self.y = y
        self.r = r
        self.id = str(id(self))
        self.shooting_range = shooting_range #may be subclass attribute

    def colliding(self, another_object): #need World's collide func
        pass


    def tick(self): #frame actions here
        pass

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


class Enemy(Unit):
    def colliding(self, another_object): #need World's collide func
        if another_obect is Hero:
            self.kill()
        else:
            self.avoid(another_object)

    def behavior(self): #AI
        if distance_to_hero <= number:
            self.move_to(hero.x, hero.y)
            if distance_to_hero <= self.shooting_range:
                self.shoot()

    def avoid(self, another_object):
        self.move_away(another_object.x, another_object.y)

