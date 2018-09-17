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


def create_star(*pos):
    star = Actor('flower')
    star.pos = pos
    return star


def draw_stars():

    height_pos = 50
    width_pos = 50
    stars = list()
    for i in range(10):
        star = create_star(width_pos, height_pos)
        width_pos += 50*Random().randint(1, 3)
        height_pos = height_pos-20 if i%2 else height_pos+20
        stars.append(star)
    return stars

def update_stars(stars):
    for star in stars:
        star.bottom += Random().randint(1, 20)
        if star.top > HEIGHT:
            star.top = 0

starz = draw_stars()

def update():
    update_stars(starz)





def draw():
    global bg
    screen.clear()
    bg.draw()
    rocket.draw()
    
    for star in starz:
        star.draw()
    
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