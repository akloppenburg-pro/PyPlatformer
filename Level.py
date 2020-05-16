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
from Constants import *

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        #self.image = pygame.Surface([width, height])
        #if width != FINISH_BLOCK_WIDTH:
            #self.image.fill(GREEN)
        #else:
            #self.image.fill(TEST)

        if height > PLATFORM_HEIGHT:
            self.image = pygame.Surface([width, height])
        else:
            self.image = pygame.image.load("Resources/deeper_grass.png")

        self.rect = self.image.get_rect()



class Level():

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        # How far this world has been scrolled left/right
        self.world_shift = 0

    # Update everything on this level
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):

        # Draw the background
        screen.fill(BLUE)
        screen.blit(pygame.image.load("Resources/clouds.png"), (0,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def reset_world(self):

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x -= self.world_shift

        for enemy in self.enemy_list:
            enemy.rect.x -= self.world_shift

        # resets world shift
        self.world_shift = 0


# Create platforms for the level
class Level_01(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with width, height, x, and y of platform
        level = [[TERRAIN_WIDTH, PLATFORM_HEIGHT, 200, GROUND_PLATFORM_Y],
                 [TERRAIN_WIDTH, PLATFORM_HEIGHT, 500, 500],
                 [TERRAIN_WIDTH, PLATFORM_HEIGHT, 800, 400],
                 [TERRAIN_WIDTH, PLATFORM_HEIGHT, 1120, 300],
                 [600, PLATFORM_HEIGHT, 1400, GROUND_PLATFORM_Y],
                 finish_block
                 ]


        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50
            #block = Platform(platform[0], platform[1])
            #block.rect.x = platform[2]
            #block.rect.y = platform[3]
            #block.player = self.player
            #self.platform_list.add(block)


# Create platforms for the level
class Level_02(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -1000
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with type of platform, and x, y location of the platform.
        level = [[TERRAIN_WIDTH, PLATFORM_HEIGHT, 200, SCREEN_HEIGHT-PLATFORM_HEIGHT],
                 [TERRAIN_WIDTH, PLATFORM_HEIGHT, 500, 500],
                 [PLAYER_WIDTH, PLATFORM_HEIGHT, 800, 400],
                 [TERRAIN_WIDTH, PLATFORM_HEIGHT, 1000, SCREEN_HEIGHT-PLATFORM_HEIGHT - 50],
                 [TERRAIN_WIDTH, PLATFORM_HEIGHT, 1300, 440],
                 [600, PLATFORM_HEIGHT, 1400, GROUND_PLATFORM_Y],
                 finish_block
                 ]

        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50
            #block = Platform(platform[0], platform[1])
            #block.rect.x = platform[2]
            #block.rect.y = platform[3]
            #block.player = self.player
            #self.platform_list.add(block)

# Create platforms for the level
class Level_03(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -500
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with type of platform, and x, y location of the platform.
        level = [[210, PLATFORM_HEIGHT, 200, GROUND_PLATFORM_Y],
                 [PLAYER_WIDTH, 30, 300, 420],
                 [PLAYER_WIDTH, 30, 400, 520],
                 [PLAYER_WIDTH, 30, 450, 325],
                 [TERRAIN_WIDTH, 30, 550, 225],
                 [PLAYER_WIDTH, 30, 730, 350],
                 [PLAYER_WIDTH, 500, 850, 0],
                 [700, 30, 850, GROUND_PLATFORM_Y],
                 finish_block
                 ]

        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50

# Create platforms for the level
class Level_04(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -500
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with type of platform, and x, y location of the platform.
        level = [[1000, PLATFORM_HEIGHT, 200, GROUND_PLATFORM_Y],
                 [PLAYER_WIDTH, 30, 1300, GROUND_PLATFORM_Y],
                 [PLAYER_WIDTH, 30, 400, GROUND_PLATFORM_Y],
                 finish_block
                 ]

        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50

# Create platforms for the level
class Level_05(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -500
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with type of platform, and x, y location of the platform.
        level = [[210, PLATFORM_HEIGHT, 200, GROUND_PLATFORM_Y],
                 [PLAYER_WIDTH, 30, 400, 500],
                 [PLAYER_WIDTH, 30, 500, 450],
                 [PLAYER_WIDTH, 30, 600, 400],
                 [PLAYER_WIDTH, 30, 700, 350],
                 [PLAYER_WIDTH, 30, 800, 250],
                 [PLAYER_WIDTH * 4, 30, 900, 150],
                 [PLAYER_WIDTH, 30, 1200, 400],
                 finish_block
                 ]

        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50

# Create platforms for the level
class Level_06(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -500
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with type of platform, and x, y location of the platform.
        level = [[210, PLATFORM_HEIGHT, 200, GROUND_PLATFORM_Y],
                 [PLAYER_WIDTH * 2, 30, 400, 500],
                 [PLAYER_WIDTH, 30, 400, 400],
                 [PLAYER_WIDTH, 30, 400, 300],
                 [PLAYER_WIDTH, 30, 400, 200],
                 [PLAYER_WIDTH, 30, 200, 500],
                 [PLAYER_WIDTH, 30, 100, 400],
                 [PLAYER_WIDTH, 30, 20, 300],
                 [PLAYER_WIDTH * 4, 30, 100, 200],
                 [950, 30, 550, 200]
                 ]

        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50

# Create platforms for the level
class Level_07(Level):

    def __init__(self, player):

        # Call the parent constructor
        Level.__init__(self, player)

        self.level_limit = -500
        finish_block = [FINISH_BLOCK_WIDTH, PLATFORM_HEIGHT, SCREEN_WIDTH - self.level_limit - 50, GROUND_PLATFORM_Y]

        # Array with type of platform, and x, y location of the platform.
        level = [[1300, PLATFORM_HEIGHT, 200, GROUND_PLATFORM_Y]
                 ]

        # Go through the array above and add platforms
        for platform in level:
            remaining_width = platform[0]
            curr_x_location = platform[2]
            while remaining_width > 0:
                block = Platform(remaining_width, platform[1])
                block.rect.x = curr_x_location
                block.rect.y = platform[3]
                block.player = self.player
                self.platform_list.add(block)
                remaining_width -= 50
                curr_x_location += 50