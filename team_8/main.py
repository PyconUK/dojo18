from colorsys import hls_to_rgb
from random import randint, choice, random
from itertools import cycle

WIDTH = 800
HEIGHT = 600


class Colours:
    GREEN = (0, 255, 0)
    LIGHT_GREEN = (0, 192, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    AUTUMN = (204, 153, 0)
    BROWN = (102, 78, 0)
    BROWN_2 = (99, 95, 0)
    BROWN_3 = (132, 100, 0)
    BROWNS = [
        BROWN,
        BROWN_2,
        BROWN_3,
    ]


class Particle:
    def __init__(self, pos, size=10, colour=Colours.WHITE):
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.colour = colour

    @property
    def pos(self):
        return (self.x, self.y)

    def draw(self):
        screen.draw.filled_circle(self.pos, self.size, self.colour)

    @classmethod
    def random(cls, colour=Colours.WHITE):
        return cls(
            (randint(0, WIDTH), randint(0, HEIGHT)),
            size=randint(5, 20),
            colour=colour
        )


def flower_colour():
    return choice([
        'red', 'green', 'blue', 'yellow', 'orange',
    ])

    inputs = (random(), 0.5, 0.1)
    value = tuple([int(255 * c) for c in hls_to_rgb(*inputs)])
    return value


LEAVES = [Particle.random(colour=choice(Colours.BROWNS)) for i in range(30)]
FLOWERS = [Particle.random(colour=flower_colour()) for i in range(500)]


class Season:
    COLOURS = {
        'spring': Colours.LIGHT_GREEN,
        'summer': Colours.GREEN,
        'autumn': Colours.AUTUMN,
        'winter': Colours.BLACK,
    }
    generator = cycle(['spring', 'summer', 'autumn', 'winter'])


SEASON = 'spring'


def draw():
    global SEASON

    screen.clear()
    screen.fill(Season.COLOURS[SEASON])
    {
        'spring': draw_spring,
        'summer': draw_summer,
        'autumn': draw_autumn,
        'winter': draw_winter,
    }[SEASON]()


def draw_spring():
    pass


def draw_summer():
    for flower in FLOWERS:
        flower.draw()


def draw_autumn():
    for leaf in LEAVES:
        leaf.draw()


def draw_winter():
    for i in range(50):
        Particle.random().draw()


def update_spring():
    pass


def update_summer():
    pass


def update_autumn():
    for leaf in LEAVES:
        leaf.x += randint(4, 7)
        leaf.y += 3
        if leaf.x > WIDTH:
            leaf.x = -leaf.size
        elif leaf.y > HEIGHT:
            leaf.y = -leaf.size


def update_winter():
    pass


def update():
    global SEASON
    {
        'spring': update_spring,
        'summer': update_summer,
        'autumn': update_autumn,
        'winter': update_winter,
    }[SEASON]()


def on_key_down(key, mod, unicode):
    global SEASON
    if key == keys.SPACE:
        SEASON = next(Season.generator)
