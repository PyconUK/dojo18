import time

WIDTH = 600
HEIGHT = 600

SPRING = (0, 255, 0)
SUMMER = (255, 255, 25)  # Laser lemon. Yes, really.
AUTUMN = (255, 0, 0)
WINTER = (255, 255, 255)
YEAR_STARTED = False


def draw():
    global YEAR_STARTED
    if not YEAR_STARTED:
       YEAR_STARTED = True
       start_winter()


def start_spring():
    screen.fill(SPRING)
    clock.schedule_unique(start_summer, 1)


def start_summer():
    screen.fill(SUMMER)
    clock.schedule_unique(start_autumn, 1)


def start_autumn():
    screen.fill(AUTUMN)
    # TODO: No, Nathaniel, no.


def start_winter():
    screen.fill(WINTER)
    clock.schedule_unique(start_spring, 1)
