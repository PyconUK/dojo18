import random

#IMAGES = "leaf.png", "snowflake.png", "raindrop.png",
IMAGES = "leaf.png", "snowflake.png", "raindrop.png", "sun.png"
SPEEDS = 0, 2, 10, -2
BACKGROUNDS = (105, 164, 200), (50, 50, 70), (105, 164, 200), (135, 206, 250)

#objects = []
#for s in range(50):
#    object = Actor("snowflake.png")
#    object.pos = random.randint(50, 1550), random.randint(50, 950) 
    
#    objects.append(object)

WIDTH = 1600
HEIGHT = 1000
SEASON_LENGTH = 200
counter = 0
season = -1

def new_season():
    global counter, season, objects
    counter = 0
    objects = []
    season += 1
    for _ in range(50):
        a = Actor(IMAGES[season])
        a.pos = random.randint(50, 1550), random.randint(50, 950)
        objects.append(a)

new_season()

def draw():
    screen.clear()
    screen.fill(BACKGROUNDS[season])
    for s in objects:
        s.draw()

def update():
    global counter, season
    if counter > SEASON_LENGTH:
        if season == 3:
            season = -1
        new_season()
    counter += 1
    for s in objects:
        s.y += random.randint(0, 4) + SPEEDS[season]
        if s.y > 1030:
            s.y = -20

       


