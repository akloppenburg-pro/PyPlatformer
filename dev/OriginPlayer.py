import pygame
from dev.OriginObjects import Objects as Parent
from Constants import *


class Player(Parent):
    def __init__(self, xPos, yPos, xVel, yVel):
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(WHITE)
        self.xPos = xPos
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        super().__init__(self.xPos, self.yPos, self.xVel, self.yVel, self.image)

    def update(self):
        self.xPos += self.xVel
        self.rect.x = self.xPos

    def move_right(self):
        self.xVel = PLAYER_X_VAL

    def move_left(self):
        self.xVel = - PLAYER_X_VAL

    def stop(self):
        self.xVel = 0