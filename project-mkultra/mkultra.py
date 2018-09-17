from itertools import cycle

WIDTH = 1024
HEIGHT = 768

seasons = ('autumn', 'winter', 'spring', 'summer')

imgs = cycle(Actor(f'{season}{n}') for season in seasons for n in range(1, 11))

t = 0

def update(dt):
    global t
    t += dt
    if t > 0.3:
        img = next(imgs)
        img.draw()
        t = 0