'''
def main():
    # pygame initialization
    pygame.init()

    if DEBUG:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)     # sets screen

    screen.fill(BLUE)  # fills screen to blue

    # test player
    player_img = pygame.image.load("Resources/WhiteBox.png").convert()
    player = PlayerObject.PlayerObject(player_img, PLAYER_SPAWN_WIDTH, SCREEN_HEIGHT - PLAYER_HEIGHT -
                                       TEST_FLOOR_HEIGHT - PLAYER_SPAWN_HEIGHT, 0, 0)
    # test_player = pygame.draw.rect(screen, WHITE, [player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT])
    floor = pygame.draw.rect(screen, TEST, [0, SCREEN_HEIGHT - TEST_FLOOR_HEIGHT, SCREEN_WIDTH, TEST_FLOOR_HEIGHT])

    clock = pygame.time.Clock()
    running = True         # main game loop boolean

    player.setYVelocity(GRAVITY)

    # running game loop
    while running:
        clock.tick(CLOCK)                                                      # 60 FPS
        report_by_2seconds = DEBUG and pygame.time.get_ticks() % 200 == 0   # reports debug info every 2 seconds
        screen.fill(BLUE)

        # event handler of keys pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # running = False
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    player.moveUp()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.moveRight()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.moveLeft()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_DOWN:
                    player.setYVelocity(GRAVITY)

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or \
                        event.key == pygame.K_d or event.key == pygame.K_a:
                    player.setXVelocity(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseXPos = pygame.mouse.get_pos()[0]
                mouseYPos = pygame.mouse.get_pos()[1]

                if mouseXPos < player.xPos:
                    bullets.append(PlayerObject.Bullet())
                    print("bullet object created")
                    bullets[-1].rect.y = player.yPos + PLAYER_HEIGHT / 2
                    bullets[-1].rect.x = player.xPos + PLAYER_WIDTH / 2
                    bullets[-1].setXVelocity(-25)
                elif mouseXPos > player.xPos:
                    bullets.append(PlayerObject.Bullet())
                    print("bullet object created")
                    bullets[-1].rect.y = player.yPos + PLAYER_HEIGHT / 2
                    bullets[-1].rect.x = player.xPos + PLAYER_WIDTH / 2
                    bullets[-1].setXVelocity(25)


        if report_by_2seconds:
            print("Floor Collision: ", player.pos.colliderect(floor))
        pygame.draw.rect(screen, WHITE, [player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT])
        # pygame.draw.rect(screen, BLACK, [0, SCREEN_HEIGHT-TEST_FLOOR_HEIGHT
        #   , SCREEN_WIDTH, TEST_FLOOR_HEIGHT])
        pygame.draw.rect(screen, TEST, floor)

        # updates player movements
        player.update(floor)

        pygame.display.update()
        pygame.display.flip()                                           # must have at end!


if __name__ == "__main__":
    main()
'''