from random import randint
from itertools import cycle

WIDTH = 800
HEIGHT = 600


class Colours:
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (0, 192, 0)
    WHITE = (255, 255, 255)
    AUTUMN = (204, 153, 0)


class Particle:
    def __init__(self, pos, size=10):
        self.pos = pos
        self.size = size

    def draw(self):
        screen.draw.filled_circle(self.pos, self.size, Colours.WHITE)

    @classmethod
    def random(cls):
        return cls((randint(0, WIDTH), randint(0, HEIGHT)), size=randint(5, 20))


class Season:
    COLOURS = {
        'spring': Colours.LIGHT_GREEN,
        'summer': Colours.GREEN,
        'autumn': Colours.AUTUMN,
        'winter': Colours.WHITE,
    }
    generator = cycle(['spring', 'summer', 'autumn', 'winter'])


SEASON = 'spring'


def draw():
    global SEASON

    screen.clear()
    screen.fill(Season.COLOURS[SEASON])

    for i in range(50):
        Particle.random().draw()

#    screen.draw.text(globals(), (100, 100), color="orange")


def update():
    global SEASON

    if SEASON == 'spring':
        pass
    elif SEASON == 'summer':
        pass
    elif SEASON == '':
        pass


def on_key_down(key, mod, unicode):
    global SEASON
    if key == keys.SPACE:
        SEASON = next(Season.generator)
