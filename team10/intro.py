from pygame.transform import scale
from pygame import BLEND_ADD
from functools import partial
import random

TREE_TOP = 33
TREE_LEFT = 80
TREE_RIGHT = 400
TREE_BOTTOM = 250
TREE_TRUNK = 250

# alien = Actor('alien')
tree = Actor('tree')
# alien.topright = 0, 10

WIDTH = tree.width
HEIGHT = tree.height

leaves = []
b = 0

def draw():
   tree.draw()
   for leaf in leaves:
       leaf.draw()


def create_leaf(coords):
   leaf = Actor('leaf')
   leaf._surf = scale(leaf._surf, (20,20))
   leaf.topleft = coords
   return leaf


def autumn():
   clock.schedule_interval(brown, 0.1)

def brown():
   global b
   for leaf in leaves:
       leaf._surf.fill((b, 0, 0, 100), special_flags=BLEND_ADD)
   b += 10
   if b == 100:
       clock.unschedule(brown)
       leaves_fall(leaves)


def leaves_fall(leaves):
   for leaf in leaves:
       leaf_fall(leaf)


def leaf_fall(leaf):
   animate(leaf, pos=(leaf.center[0], 550), tween='accelerate')


for i in range(100):
   x = random.randint(TREE_LEFT, TREE_RIGHT)
   y = random.randint(TREE_TOP, TREE_BOTTOM)
   coords = (x, y)
   # print(coords)
   leaves.append(create_leaf(coords))

autumn()
