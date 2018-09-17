WIDTH = 800
HEIGHT = 800


colours = {
    'sky': (38, 110, 226),
    'soil': (112, 74, 3),
}


sprites = [
    Actor('autumn'),
    Actor('flower'),
    Actor('bud'),
    Actor('snowflake'),
]


def draw():
    screen.fill(colours['sky'])
    soil_box = Rect((0, 550), (600, 600))
    screen.draw.filled_rect(soil_box, colours['soil'])

    screen.clear()
    screen.fill((128, 128, 128))

    def branch_end(beg, way=1):
        beg[0] += (angle * way)
        beg[1] -= height
        return beg

    line_color = (0, 0, 0)
    height = 50
    angle = 20
    beg_left = [400, 700]
    beg_right = [400, 700]
    left_pos, right_pos = beg_left[:], beg_right[:]
    for i in range(5):

        left_pos = branch_end(left_pos, way=1)
        right_pos = branch_end(right_pos, way=-1)

        screen.draw.line(beg_left, left_pos, line_color)
        screen.draw.line(beg_right, right_pos, line_color)

        beg_right = right_pos[:]
        beg_left = left_pos[:]
