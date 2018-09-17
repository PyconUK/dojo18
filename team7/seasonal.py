import time

WIDTH = 600
HEIGHT = 600

SPRING = (0, 255, 0)
SUMMER = (255, 255, 25)  # Laser lemon. Yes, really.
AUTUMN = (255, 0, 0)
WINTER = (255, 255, 255)

YEAR_STARTED = False

LEAF_ON_A_BREEZE = 1
RED_WEED = 2
OOLAA = 1.5

def draw():
    global YEAR_STARTED
    if not YEAR_STARTED:
       YEAR_STARTED = True
       start_winter()


def start_spring():
    screen.fill(SPRING)
    clock.schedule_unique(start_summer, LEAF_ON_A_BREEZE)


def start_summer():
    screen.fill(SUMMER)
    clock.schedule_unique(start_autumn, LEAF_ON_A_BREEZE)


def start_autumn():
    screen.fill(AUTUMN)
    clock.schedule_unique(more_to_life, RED_WEED)


def more_to_life():
    screen.draw.text("No, Nathaniel, no.", (130, 40))
    clock.schedule_unique(restore_to_life, OOLAA)


def restore_to_life():
    screen.draw.text("There must be more to life.", (130, 60))


def start_winter():
    screen.fill(WINTER)
    clock.schedule_unique(start_spring, LEAF_ON_A_BREEZE)
