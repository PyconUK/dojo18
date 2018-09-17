WIDTH = 800
HEIGHT = 600

tree = Actor('tree')
tree.pos = 405, 352

leaf = Actor('leaf')
leaf.pos = 10, 10
POS = [10, 10]


def draw():
    screen.fill((0, 200, 255))
    tree.draw()
    leaf.draw()

def update():
    leaf.pos = POS[0] + 5, POS[1] + 5
    POS[0] += 5
    POS[1] += 5
    leaf.draw()


