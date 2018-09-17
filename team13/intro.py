WIDTH = 800
HEIGHT = 600

tree = Actor('tree')
tree.pos = 405, 352


def draw():
    screen.fill((0, 200, 255))
    tree.draw()


