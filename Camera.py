from World import world, spawn


class Camera:
    """
    def __init__(self, x=100, y=100, width=500, height=500, speed=20):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.speed = speed
    """
    def __init__(self, width=200, height=200, speed=20):
        self.x = spawn['x'] - width
        self.y = spawn['y'] - height
        self.w = spawn['x'] + width
        self.h = spawn['y'] + height
        self.speed = speed

    def camleft(self):
        if self.x - self.speed <= world['x']:
            self.x = world['x']
        else:
            self.x -= self.speed

    def camright(self):
        if self.x + self.w + self.speed >= world['width']:
            self.x = world['width'] - self.w
        else:
            self.x += self.speed

    def camup(self):
        if self.y - self.speed <= world['y']:
            self.y = world['y']
        else:
            self.y -= self.speed

    def camdown(self):
        if self.y + self.h + self.speed >= world['height']:
            self.y = world['height'] - self.h
        else:
            self.y += self.speed

