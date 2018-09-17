import pgzero

WIDTH = 570
HEIGHT = 380
tick=0


def update():
    global tick
    tick += 1
    if tick == 1:
        screen.blit('summer_christmas', (0, 0))
    elif tick == 300:
        screen.blit('spring_autumn', (-555, 0))
    elif tick == 600:
        tick = 0

