alien = Actor('alien')
alien.pos = 250, 200

SPRING, SUMMER, AUTUMN, WINTER = 45, 135, 225, 315

backdrop = Actor('wheel_in_time')
backdrop.pos = 250, 400
backdrop.angle = SUMMER -25
WIDTH = 500
HEIGHT = 250

rain = Actor('rain')
rain.pos = 0, -500
snow = Actor('snow')
snow.pos = 0, -200
sun = Actor('sun')
sun.pos = WIDTH - sun.width / 2 - 10, sun.height / 2 + 10

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    backdrop.draw()
    if SPRING <= backdrop.angle <= SUMMER or AUTUMN <= backdrop.angle <= WINTER:
        rain.draw()
    if WINTER <= backdrop.angle or backdrop.angle <= SPRING:
        snow.draw()
    if SUMMER <= backdrop.angle <= AUTUMN:
        sun.draw()
    alien.draw()


def update():
    backdrop.angle += 0.155
    if backdrop.angle > 360:
        backdrop.angle %= 360
    rain.top += 2
    snow.top += 1
    if rain.top > HEIGHT:
        rain.bottom = -100
    if snow.top > HEIGHT:
        snow.bottom = -100
