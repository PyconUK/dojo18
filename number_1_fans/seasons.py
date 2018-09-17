import pgzero
import time

VOLUME = 50
FAN_MUSIC_NAME = 'fan.wav'

WIDTH = 800
HEIGHT = 800

SEASON = 'su'


fan_actor = Actor('big_fan', center=(WIDTH/2, HEIGHT/2))


def draw():
    screen.clear()
    fan_actor.draw()


def update():
    speed = {
        'w': 1,
        'spr': 5,
        'su': 10,
        'a': 5,
    }[SEASON]
    print("speed is %d" % speed)
    fan_actor.angle -= speed


def set_volume(volume_level):
    def decorator(fn):
        def new_fn(*args, **kwargs):
            music.set_volume(volume_level)
            return fn(*args, **kwargs)
        return new_fn
    return decorator


TIME_OF_SEASON = 10



def winter():
    global next_season, SEASON
    SEASON = 'w'
    music.set_volume(0.1)
    music.play(FAN_MUSIC_NAME)
    def next_season():
        music.stop()
        spring()
    clock.schedule_unique(next_season, TIME_OF_SEASON)

next_season = None

def spring(time_to_play=10):
    global next_season, SEASON
    SEASON = 'spr'
    music.set_volume(0.6)
    music.play(FAN_MUSIC_NAME)
    def next_season():
        music.stop()
        summer()
    clock.schedule_unique(next_season, TIME_OF_SEASON)



def summer(time_to_play=10):
    global next_season, SEASON
    SEASON = 'su'
    music.set_volume(1.0)
    music.play(FAN_MUSIC_NAME)
    def next_season():
        music.stop()
        autumn()
    clock.schedule_unique(next_season, TIME_OF_SEASON)



def autumn(time_to_play=10):
    global next_season, SEASON
    SEASON = 'a'
    music.set_volume(0.5)
    music.play(FAN_MUSIC_NAME)
    def next_season():
        music.stop()
        winter()
    clock.schedule_unique(next_season, TIME_OF_SEASON)


summer()