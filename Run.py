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
import datetime, sys
from Level import *
from Player import *
from Constants import *

#main program to be run
def main():
    pygame.init()                                   #initializes pygame
    running = True                                  #game loop boolean
    clock = pygame.time.Clock()                     #clock initialization for the game
    font = pygame.font.SysFont("Times New Roman", 40)
    final_time = -1
    level_deaths = [1, 1, 1, 1, 1, 1, 1]

    # Set the height and width of the screen
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    pygame.display.set_caption("Platformer")

    # Create the player
    player = Player()

    #level initialization
    level_list = []
    level_list.append(Level_01(player))
    level_list.append(Level_02(player))
    level_list.append(Level_03(player))
    level_list.append(Level_04(player))
    level_list.append(Level_05(player))
    level_list.append(Level_06(player))
    level_list.append(Level_07(player))


    # places player in given index of level array
    current_level_no = 0
    current_level = level_list[current_level_no]

    # creates a sprite group for updating
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    #sets current location of the player object
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height - PLATFORM_HEIGHT
    active_sprite_list.add(player)                      #adds player to the sprite group

    #create different control schemes to be tests during user tests
    #TODO: create different control schemes of the form [left movement, right movement, jump]
    traditional_arrow = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP]
    traditional_wasd = [pygame.K_a, pygame.K_d, pygame.K_w]
    mouse = [pygame.K_LEFT, pygame.K_RIGHT, pygame.MOUSEBUTTONDOWN]
    wasd_space = [pygame.K_a, pygame.K_d, pygame.K_SPACE]
    arrow_space = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SPACE]
    control_scheme = [traditional_arrow, traditional_wasd, mouse, wasd_space, arrow_space]

    displayStartScreen(screen)

    # game loop
    while running:
        attempts = "Attempts: {}".format(level_deaths[current_level_no])
        attempts_text = font.render(attempts, True, (255, 255, 255))
        time_string = "Time: {}".format(int(pygame.time.get_ticks() / 1000))
        time_string_text = font.render(time_string, True, (255, 255, 255))
        # EVENT OPERATIONS ------------------------------------------------------
        # check for exit button being pressed to terminate program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # executes a given action based on a button press
            if event.type == pygame.KEYDOWN:
                if event.key == control_scheme[0][0] or event.key == control_scheme[1][0] or event.key == control_scheme[2][0] or event.key == control_scheme[3][0] or event.key == control_scheme[4][0]:
                    player.go_left()
                if event.key == control_scheme[0][1] or event.key == control_scheme[1][1] or event.key == control_scheme[2][1] or event.key == control_scheme[3][1] or event.key == control_scheme[4][1]:
                    player.go_right()
                if event.key == control_scheme[0][2] or event.key == control_scheme[1][2] or event.key == control_scheme[3][2] or event.key == control_scheme[4][2]:
                    player.jump()
                if event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6:
                    player.rect.x = 340
                    if event.key == pygame.K_0:
                        current_level_no = 0
                    elif event.key == pygame.K_1:
                        current_level_no = 1
                    elif event.key == pygame.K_2:
                        current_level_no = 2
                    elif event.key == pygame.K_3:
                        current_level_no = 3
                    elif event.key == pygame.K_4:
                        current_level_no = 4
                    elif event.key == pygame.K_5:
                        current_level_no = 5
                    elif event.key == pygame.K_6:
                        current_level_no = 6
                    current_level = level_list[current_level_no]
                    current_level.reset_world()
                    player.level = current_level

            # resets the player's velocity when a left or right key is released (mostly for arial movement)
            if event.type == pygame.KEYUP:
                if (event.key == control_scheme[0][0] or event.key == control_scheme[1][0] or event.key == control_scheme[2][0]) and player.change_x < 0:
                    player.stop()
                if (event.key == control_scheme[0][1] or event.key == control_scheme[1][1] or event.key == control_scheme[2][1]) and player.change_x > 0:
                    player.stop()

            # mouse clicks are of their own type in pygame, and thus they require different input
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.jump()
            if event.type == pygame.MOUSEBUTTONUP:
                player.stop()

        # updates player sprite
        active_sprite_list.update()

        # updates level sprites
        current_level.update()

        # resets level on death
        if player.rect.y >= SCREEN_HEIGHT - player.rect.height:
            player.rect.x = 340
            player.rect.y = SCREEN_HEIGHT - player.rect.height - PLATFORM_HEIGHT
            level_deaths[current_level_no] += 1
            current_level.reset_world()

        # LEVEL-PLAYER MANIPULATION ---------------------------------------------
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 340
            current_level.reset_world()
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                final_time = int(pygame.time.get_ticks() / 1000)
                running = False         #ends game at end of levels

        # SPRITE DRAWING SECTION ------------------------------------------------
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        screen.blit(attempts_text, (20, 20))
        screen.blit(time_string_text, (810, 20))

        # END OF DRAWING SECTION ------------------------------------------------

        # initialize to 60fps
        clock.tick(60)

        # updates screen
        pygame.display.flip()

    displayEndScreen(screen)

    recordStats(level_deaths, final_time)

    print(level_deaths, final_time)
    #exits once game loop is finished
    pygame.quit()


def displayStartScreen(screen):
    titleScreen = pygame.image.load("Resources/title_screen.png").convert()
    screen.blit(titleScreen, (0, 0))
    pygame.display.update()
    pygame.display.flip()

    # Title Screen
    spacebarPressed = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spacebarPressed = True
                    break
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        if spacebarPressed:
            break

def displayEndScreen(screen):
    font = pygame.font.SysFont("Times New Roman", 40)

    winnerString = "Thanks for playing!"

    winnerText = font.render(winnerString, True, (255, 255, 255))

    screen.blit(winnerText, (490, 400))
    pygame.display.update()
    pygame.display.flip()

def recordStats(totalAttempts, finalTime):
    date = datetime.datetime.now()
    date.strftime("%Y-%m-%d %H:%M:%S")
    fp = open("test_data.txt", "a+")
    fp.write(date.strftime("%Y-%m-%d %H:%M:%S\n"))

    level_num = 1
    for attempt in totalAttempts:
        level_string = "Level " + str(level_num) + ": " + str(attempt) + " attempt(s)\n"
        fp.write(level_string)
        level_num += 1
    fp.write("Completion Time: ")
    fp.write(str(finalTime))
    fp.write(" seconds\n----------------------------------\n\n")
    fp.close()

if __name__ == "__main__":
    main()