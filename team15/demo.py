import pgzrun

SUMMER = 255, 255, 0
WINTER = 255, 255, 255
FALL = 193, 82, 17
SPRING = 8, 160, 10

# https://www.vectorstock.com/royalty-free-vector/trees-of-four-seasons-vector-1837612


WIDTH = 550
HEIGHT = 466

c = 255
winter = Actor('winter', anchor=('left', 'top'))
summer = Actor('summer', anchor=('left', 'top'))
spring = Actor('spring', anchor=('left', 'top'))
fall = Actor('fall', anchor=('left', 'top'))
winter2 = Actor('winter', anchor=('left', 'top'))

images = [winter, spring, summer, fall, winter2]

delta = 5
elapse = 0


def draw():
    for season in images:
        season.draw()


def update():
    global elapse, delta

    for index, season in enumerate(images):
        season.x = index * 550 - elapse

    elapse += delta
    if elapse > 4 * 550:
        elapse = 0


pgzrun.go()
