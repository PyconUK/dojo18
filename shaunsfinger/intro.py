"""introduction: four seasons challeng"""
from datetime import date, timedelta
from math import sin


WIDTH = 1024
HEIGHT = 768

day = date.today()
"""current date"""

tick = 0

pizza = Actor('pizza')
"""the pizza to spin"""

landscape_a, landscape_b = Actor('landscape'), Actor('landscape')


def format_day(d):
    return d.strftime('%d %b %Y')


def position_landscape(offset):
    x = offset / 365
    # left hand side
    # x is initial offset of centre of image - full width * fraction
    landscape_a.pos = 1024 * 2 - (1024 * 4 * x), 768/2
    landscape_a.draw()

    # right hand side
    landscape_b.pos = 1024 * 6 - (1024 * 4 * x), 768/2
    landscape_b.draw()


def draw():
    offset = day.timetuple().tm_yday

    # put the background in at lowest z-index
    position_landscape(offset)

    # setup the pizza and its position
    pizza.pos = WIDTH / 2, 768 - 300 - sin(tick/20) * 50
    pizza.draw()

    screen.draw.textbox(
        format_day(day),
        Rect(
            (
                (1024/2) - 200,
                25
            ),
            (
                (1024/2) - 50,
                75
            ),
        )
    )


def update():
    global day, tick
    tick += 1
    day += timedelta(days=1)
    screen.clear()
    pizza.angle -= 360 / 365
