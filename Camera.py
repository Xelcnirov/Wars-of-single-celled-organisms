from World import world, start, camera_size, hero_speed


class Camera:

    def __init__(self, width=camera_size['width'], height=camera_size['height'], speed=hero_speed):
        self.x = start['x'] - width//2
        self.y = start['y'] - height//2
        self.w = width  # start['x'] + width//2
        self.h = height  # start['y'] + height//2
        self.speed = speed

    def camleft(self):
        if self.x - self.speed <= world['x'] - self.w//2 + start['hero_r']:
            self.x = world['x'] - self.w//2 + start['hero_r']
        else:
            self.x -= self.speed

    def camright(self):
        if self.x + self.w + self.speed >= world['width'] + self.w//2 - start['hero_r']:
            self.x = world['width'] - self.w//2 - start['hero_r']
        else:
            self.x += self.speed

    def camup(self):
        if self.y - self.speed <= world['y'] - self.h//2 + start['hero_r']:
            self.y = world['y'] - self.h//2 + start['hero_r']
        else:
            self.y -= self.speed

    def camdown(self):
        if self.y + self.h + self.speed >= world['height'] + self.h//2 - start['hero_r']:
            self.y = world['height'] - self.h//2 - start['hero_r']
        else:
            self.y += self.speed
