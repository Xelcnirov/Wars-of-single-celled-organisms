from Units import Unit


class Projectile(Unit):
    def __init__(self, x, y, target_x, target_y):
        Unit.__init__(self, x, y, r=7, shooting_range=300, speed=15, colour='red')
        self.target_x = target_x
        self.target_y = target_y
        self.step = self.shooting_range/self.speed
        self.proj_calc(target_x, target_y)

    def proj_calc(self, target_x, target_y):
        slip_x = target_x - self.x
        slip_y = target_y - self.y
        self.breaker = 1
        self.side = True
        self.check_shot = True
        if slip_x < 0:
            slip_x *= -1
        if slip_y < 0:
            slip_y *= -1
        if slip_x > slip_y:
            self.breaker = slip_y / slip_x
            self.side = True
        elif slip_x < slip_y:
            self.breaker = slip_x / slip_y
            self.side = False
        elif slip_x == 0 and slip_y == 0:
            self.check_shot = False
        if target_x > self.x:
            self.speed_x = self.speed # one
        elif target_x < self.x:
            self.speed_x = -self.speed
        else:
            self.speed_x = 0
        if target_y > self.y:
            self.speed_y = self.speed
        elif target_y < self.y:
            self.speed_y = -self.speed
        else:
            self.speed_y = 0
        self.tick()

    def tick(self):
        if self.step and self.check_shot:
            #animation.delete_obj(self)
            if self.side:
                self.x += self.speed_x
                self.y += self.speed_y * self.breaker
                #animation.draw(self)

            else:
                self.y += self.speed_y
                self.x += self.speed_x * self.breaker
                #animation.draw(self)

            self.step -= 1
            #animation.screen.after(10, Projectile.proj_mot, self, check_shot, speed_x, speed_y, breaker, side)

        #else:
            #animation.delete_obj(self)

    def collide(self):
        self.step = 0
