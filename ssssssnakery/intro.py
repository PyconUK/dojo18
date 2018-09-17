alien = Actor('alien')
alien.topright = 0,10

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()
'''    
def on_key_down():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
'''
def on_key_down(key, mod, unicode):
    if key == RIGHT
        rocket.right += 2
        if rocket.left > WIDTH:
            rocket.right



def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'