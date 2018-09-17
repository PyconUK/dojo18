"""
pgzero - training ground for pygame


"""
WIDTH = 300
HEIGHT = 300

# SUMMER = ()


def get_closer_color(src_color, target_color):
    """
    e.g. is src is (128, 0, 0) and target is (64, 64, 0), will output (127, 1, 0)
    movin all rgb components closer to target
    """

    result_color = list(src_color)
    for i in range(3):
        if result_color[i] == target_color[i]:
            continue
        elif result_color[i] > target_color[i]:
            result_color[i] -= 1
        else:
            result_color[i] += 1

    return tuple(result_color)


SPRING = (0, 0, 255)
SUMMER = (255, 0, 0)
AUTUMN = (0, 255, 0)
WINTER = (255, 255, 255)
season_colors = [
    SPRING, SUMMER, AUTUMN, WINTER
]

ci = 0
current_color = season_colors[0]
target_color = season_colors[1]

def draw():
    def move_colors():
        def move_it():
            global ci
            global current_color
            global target_color

            if current_color == target_color:
                ci = (ci + 1) % len(season_colors)
                print('ci = {}'.format(ci))
                current_color = season_colors[ci]
                target_color = season_colors[(ci + 1) % len(season_colors)]

            current_color = get_closer_color(current_color, target_color)
            print(current_color, target_color)
            screen.fill(current_color)

            clock.schedule_unique(move_it, 0.1)

        move_it()

    move_colors()