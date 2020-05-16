# Sources
# https://www.pygame.org/docs/
# https://www.pygame.org/tags/sidescroller <-- used as inspiration, not for coding help
# http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
# http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
# http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
# http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
# http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
# https://www.youtube.com/watch?v=QplXBw_NK5Y&feature=youtu.be

DEBUG = True
# background
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = round(SCREEN_WIDTH / 1.61803398875)  # golden ratio!
TEST_FLOOR_HEIGHT = 50

# colors
RED = (255, 0, 0)
BLUE = (0, 83, 186)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TEST = (102, 205, 170)

# player
PLAYER_HEIGHT = 50
PLAYER_WIDTH = round(PLAYER_HEIGHT / 1.61803398875)  # golden ratio!

PLAYER_Y_VAL = 5
PLAYER_X_VAL = 5

PLAYER_SPAWN_HEIGHT = PLAYER_Y_VAL * 10  # factor of y movement
PLAYER_SPAWN_WIDTH = PLAYER_X_VAL * 8  # factor of x movement

# gravity
GRAVITY = .5

# clock
CLOCK = 60

# level design
TERRAIN_WIDTH = 210
GRASS_SEG_WIDTH = 50
PLATFORM_HEIGHT = 30
GROUND_PLATFORM_Y =SCREEN_HEIGHT-PLATFORM_HEIGHT
FINISH_BLOCK_WIDTH = 69
