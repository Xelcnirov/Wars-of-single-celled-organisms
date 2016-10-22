from Units import Unit
from World import spawn


class Hero(Unit):
    def __init__(self):
        Unit.__init__(self, x=spawn['x'], y=spawn['y'], r=40, speed=20)

    def tick(self): pass
