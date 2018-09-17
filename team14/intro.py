mysprite = Actor('wheat')
mysprite.topright = 0, 150

WIDTH = 500
HEIGHT = mysprite.height + 300

seasons = [
    (51, 153, 51),
    (255, 255, 153),
    (255, 51, 0),
    (179, 230, 255)
]

sprites = [
    'wheat',
    'summer',
    'hay',
    'santa'
]

our_music = [
  'spring_birds',
  'summer_song',
  'sleigh_bells',
  'autumn_school'
]

season = 0

def draw():
    screen.clear()
    screen.fill(seasons[season])
    mysprite.draw()

def update():
    mysprite.left += 2
    mysprite.angle += 1
    if mysprite.left > WIDTH:
        mysprite.right = 0

def on_key_down(key):
    if key == keys.SPACE:
        change_season(season)

def change_season(current_season):
    global season
    season = (current_season + 1) % 4
    mysprite.image = sprites[season]
    music.play(our_music[season])

