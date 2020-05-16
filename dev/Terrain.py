# Sources
# https://www.pygame.org/docs/
# https://www.pygame.org/tags/sidescroller <-- used as inspiration, not for coding help
# http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
# http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
# http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
# http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
# http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
# https://www.youtube.com/watch?v=QplXBw_NK5Y&feature=youtu.be

import pygame
from dev.OriginObjects import Objects as Parent
from Constants import *


class Terrain(Parent):
    def __init__(self, xPos, yPos, xVel, yVel):
        self.image = pygame.Surface([TERRAIN_WIDTH, TERRAIN_HEIGHT])
        self.image.fill(WHITE)
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        super().__init__(self.xPos, self.yPos, self.xVel, self.yVel, self.image)
