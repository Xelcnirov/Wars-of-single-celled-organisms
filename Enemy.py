from Units import Unit


class Enemy(Unit):
    def __init__(self, x, y):
        Unit.__init__(self, x, y, colour='#6d2f84')
