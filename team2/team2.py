import itertools
import pathlib
import time

WIDTH = 1280
HEIGHT = 800

backgrounds = itertools.cycle(sorted((p.stem
                                      for p in pathlib.Path('images').iterdir()),
                                     key=lambda s: 'sp su au wi'.index(s[:2])
                                     ))

def draw():
    background = next(backgrounds)
    screen.clear()
    screen.blit(background,(0, 0))



#def update():
#    time.sleep(3)

def on_key_down(key):
    if key == keys.P:
        music.play('four_seasons')
    if key == keys.SPACE:
        draw()
