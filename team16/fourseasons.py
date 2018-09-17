import pgzrun
from math import sin
import random

WIDTH = 800
HEIGHT = 600
SNOWFLAKES = 128

# landscape_colours = [(128,128,128),
#                      (128, 255, 128),
#                      (128, 128, 255),
#                      (255, 128, 128)]

landscape_colours = ['#c6c6c6',
                     '#80f442',
                     '#60e21b',
                     '#ffb677']

snowflakes = []

season = 0
season_ticker = 0
SEASON_UPDATE_TIME = 120

snake_direction = 1

seasons = [
    'winter',
    'spring',
    'summer',
    'autumn'
]

tree = Actor(seasons[0])
tree.pos = WIDTH/ 2, 450
tree.anchor = 'center', 'bottom'

pylogo = Actor('pylogo')
pylogo.pos = WIDTH / 2, 150



def draw():
    screen.fill('blue')
    landscape_colour = 'pink'

    for x in range(WIDTH):
        h = 20 * sin(x*0.01)
        screen.draw.line((x, h + 500), (x, HEIGHT), landscape_colours[season])

    if seasons[season] is 'winter':
        draw_snow()

    pylogo.draw()
    tree.draw()


def update():
    walk = (5 * sin(pylogo.x*0.1))
    pylogo.x = (pylogo.x + snake_direction)% WIDTH
    pylogo.y = (20 * sin(pylogo.x*0.01)) + 500 + walk
    pylogo.angle -= snake_direction % 360
    global season_ticker
    season_ticker += 1
    if season_ticker == SEASON_UPDATE_TIME:
        season_change()


def season_change():
    global season
    global season_ticker
    season_ticker = 0
    season += 1
    season = season % len(seasons)
    tree.image = seasons[season ]


def on_mouse_down():
    global snake_direction
    snake_direction *= -1

def draw_snow():
    global snowflakes
    if season_ticker % 8 == 0:
        snowflakes = []
        for n in range(SNOWFLAKES):
            position = (random.randint(0, WIDTH),
                        random.randint(0, HEIGHT))
            snowflakes.append(position)
    for p in snowflakes:
        screen.draw.text("*", p, alpha=1)


pgzrun.go()

