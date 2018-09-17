import random as rnd
import math
import time as tm


HEIGHT = 500
WIDTH = 800
# Autumn, Winter, Spring, Summer = 0, 1, 2, 3
SEASON = 0
DAY = True
DAY_BACK = [(247, 216, 255), (87, 103, 127), (90, 210, 220), (188, 250, 255)]
counter = 0

x_coords = [rnd.random() for _ in range(10)]

def draw():
    global SEASON
    global counter
    global DAY
    counter += 1
    
    if counter % 500 == 0:
        SEASON = (SEASON + 1) % 4
        counter = 0
    if counter % 125 == 0:
        DAY = not(DAY)
    if DAY:
        background = DAY_BACK[SEASON]
    else:
        background = (0, 0, 0)
        
    if SEASON == 0:
        #screen.fill((100, 0, 200))
        screen.fill(background)
        draw_falling_objects((244, 144, 66))
    elif SEASON == 1:
        #screen.fill((0, 0, 150))
        screen.fill(background)
        draw_falling_objects((255, 255, 255))
    elif SEASON == 2:
        screen.fill(background)
        #screen.fill((0, 0, 100))
        draw_falling_objects((33, 80, 150))
    elif SEASON == 3:
        screen.fill(background)
        
        if DAY:
            screen.draw.filled_circle((WIDTH*counter/125 % WIDTH, HEIGHT*0.1), 30, (244, 244, 66))
            screen.draw.filled_rect(Rect((WIDTH*0.75, HEIGHT*0.05), (WIDTH*0.25, HEIGHT*0.2)), (255, 255, 255))
            screen.draw.filled_rect(Rect((WIDTH*0.25, HEIGHT*0.07), (WIDTH*0.25, HEIGHT*0.2)), (255, 255, 255))        
        
def draw_falling_objects(color):
    for y in range(counter+1):
        for x in x_coords:
            x = math.sin(y-counter)
            screen.draw.filled_circle((x*WIDTH, y), 2, color)
    

def update():
    draw()
    
    
