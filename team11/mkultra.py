
import math

WIDTH=800
HEIGHT=800

RED = 200, 0, 0
BLUE = 0, 0, 200
GREEN = 0, 200, 0
WHITE = 255, 255, 255
BROWN = 139, 69, 19
YELLOW = 255, 215, 0
BLACK = 0, 0, 0

BOX1 = Rect((20, 20), (380, 380))
BOX2 = Rect((400,20), (380, 380))
BOX3 = Rect((20,400), (380, 380))
BOX4 = Rect((400,400), (380, 380))

t = 0

def draw():
    screen.draw.filled_rect(BOX1, GREEN)
    screen.draw.filled_rect(BOX2, YELLOW)
    screen.draw.filled_rect(BOX3, BROWN)
    screen.draw.filled_rect(BOX4, WHITE)
    screen.draw.text("SPRING", (180, 30), color="black")
    screen.draw.text("SUMMER", (580, 30), color="black")
    screen.draw.text("AUTUMN", (180, 410), color="black")
    screen.draw.text("WINTER", (580, 410), color="black")   

    # Spring
    draw_branch(max_depth=3)
    # Summer
    draw_branch(start=(600, 400), max_depth=5)
    # Autumn
    draw_branch(start=(200, 800), max_depth=3)
    # Winter
    draw_branch(start=(600, 800), max_depth=2)

trunk_length = 200
twig_length_compared_to_trunk = 1/2
twigs_per_branch = 4
spread = math.radians(200)


def draw_branch(start=(200, 400), length=trunk_length, rotation=0, depth=0, max_depth=4):
    if depth > max_depth:
        return
    
    start_x, start_y = start
    end_x = math.sin(rotation) * length + start_x
    end_y = -1 * math.cos(rotation) * length + start_y
    end = end_x, end_y

    screen.draw.line(start, end, BLACK)
    
    twig_length = twig_length_compared_to_trunk * length

    angle_between_twigs = spread / (twigs_per_branch - 1)
    twig_angles = [angle_between_twigs * x for x in range(twigs_per_branch)]
    twig_angles = [twig_angle - spread / 2 for twig_angle in twig_angles]
    twig_angles = [twig_angle + rotation for twig_angle in twig_angles]



    for twig_angle in twig_angles:
        draw_branch(start=end, length=twig_length, rotation=twig_angle, depth=depth + 1, max_depth=max_depth)


