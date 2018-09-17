import time
import pygame

WIDTH = 600
HEIGHT = 600

SPRING = (0, 255, 0)
SUMMER = (255, 255, 25)  # Laser lemon. Yes, really.
AUTUMN = (255, 0, 0)
WINTER = (255, 255, 255)

YEAR_STARTED = False

LEAF_ON_A_BREEZE = 0.5
RED_WEED = 2
OOLAA = 1.5
THUNDERCHILD = 0.001

season_colors = [
    WINTER, SPRING, SUMMER, AUTUMN
]

ci = 0
current_color = season_colors[0]
target_color = season_colors[1]


def draw():
    global YEAR_STARTED
    if not YEAR_STARTED:
       YEAR_STARTED = True
       move_colors()


def get_closer_color(src_color, target_color):
    """
    e.g. is src is (128, 0, 0) and target is (64, 64, 0), will output (127, 1, 0)
    movin all rgb components closer to target
    """

    result_color = list(src_color)
    for i in range(3):
        if result_color[i] == target_color[i]:
            continue
        elif result_color[i] > target_color[i]:
            result_color[i] -= 1
        else:
            result_color[i] += 1

    return tuple(result_color)


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

def move_colors():
    def move_it():
        global ci
        global current_color
        global target_color

        if current_color == target_color:
            ci = (ci + 1) % len(season_colors)
            print('ci = {}'.format(ci))
            current_color = season_colors[ci]
            target_color = season_colors[(ci + 1) % len(season_colors)]

        current_color = get_closer_color(current_color, target_color)
        print(current_color, target_color)
        screen.fill(current_color)

        print('Filthy hack a')
        if current_color != season_colors[-1]:
            print('Filthy hack b')
            clock.schedule_unique(move_it, THUNDERCHILD)
        else:
            clock.schedule_unique(more_to_life, RED_WEED)

    move_it()
