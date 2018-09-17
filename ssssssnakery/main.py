import time
from random import Random
from itertools import cycle

rocket = Actor('rocket_flying')
rocket.topright = 0,10
spring = Actor('spring')
summer = Actor('summer')
autumn = Actor('autumn')
winter = Actor('winter')

WIDTH = 1024
HEIGHT = 768

seasons = cycle([summer, autumn, winter, spring])
bg = spring

start=time.time()


def draw():
    global bg
    screen.clear()
    bg.draw()
    rocket.draw()
    
def on_key_down(key, mod, unicode):
    global bg
    if key == keys.RIGHT:
        for i in range(5):
            rocket.right += i*2
            if rocket.left > WIDTH:
                end = time.time()
                bg = next(seasons)
                rocket.right
    elif key == keys.LEFT:
        for i in range(5):
            rocket.left += i*2
            if rocket.right > WIDTH:
                #background = next background
                rocket.left