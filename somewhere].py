import random
import time

bud = Actor('bud')
flower = Actor('flower')
autumn = Actor('autumn')
snowflake1 = Actor('snowflake1')
snowflake2 = Actor('snowflake2')
WIDTH = flower.height + 300
HEIGHT = flower.height + 300

music.play("vivaldi")

sprites = []
sps = ['bud', 'flower', 'autumn', 'snowflake1']
t = time.time()

def draw():
    screen.fill((255, 255, 255))
    for sprite in sprites:
        sprite.draw()
    
def update():
    global t
    if time.time() < t+10:
        sprites.append(Actor(sps[0]))
        sprites[-1].x = random.randint(1, 300)
    else:
        sps.pop(0)
        t = time.time()
    for sprite in sprites:
        sprite.y += random.randint(1, 3)
        sprite.x += random.randint(1, 5) - 3