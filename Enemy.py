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