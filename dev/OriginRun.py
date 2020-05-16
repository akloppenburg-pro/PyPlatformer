import pygame
from dev.OriginPlayer import Player
from dev.Terrain import Terrain
from Constants import *

class Run:
    def main():
        pygame.init()

        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("CS Gang")

        player = Player(0, 0, 0, 0)
        floor = pygame.draw.rect(screen, TEST, [0, SCREEN_HEIGHT - TEST_FLOOR_HEIGHT, SCREEN_WIDTH, TEST_FLOOR_HEIGHT])

        clock = pygame.time.Clock()

        screen.fill(BLUE)

        terrain = Terrain(100, 100, 0, 0)

        done = False
        while not done:
            screen.fill(BLUE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            pygame.draw.rect(screen, WHITE, [player.xPos, player.yPos, PLAYER_WIDTH, PLAYER_HEIGHT])
            pygame.draw.rect(screen, WHITE, [terrain.xPos, terrain.yPos, TERRAIN_WIDTH, TERRAIN_HEIGHT])

            pygame.draw.rect(screen, TEST, floor)

            clock.tick(CLOCK)
            pygame.display.flip()

        pygame.quit()

    def __init__(self):
        self.done = False

        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)

        self.testSpritesGroup = pygame.sprite.Group()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        pass

    def update(self):
        self.testSpritesGroup.update()
        pass

    def draw(self):
        self.screen.fill(BLUE)
        self.testSpritesGroup.draw(self.screen)

        done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    pygame.quit()
                    return
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.move_left()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or \
                     event.key == pygame.K_d or event.key == pygame.K_a:
                    player.stop()

        player.update()

        pygame.draw.rect(screen, WHITE, player.rect)
        pygame.draw.rect(screen, WHITE, terrain.rect)

        pygame.draw.rect(screen, TEST, floor)


        clock.tick(CLOCK)
        pygame.display.flip()
        pass

    if __name__ == "__main__":
        main()