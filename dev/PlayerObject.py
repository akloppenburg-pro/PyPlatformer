import pygame
from Constants import *
class PlayerObject:

    def __init__(self, image, x, y, xVel, yVel):
        self.image = image
        self.xPos = x
        self.yPos = y
        self.pos = image.get_rect().move(x, y)
        self.xVel = xVel
        self.yVel = yVel

    # TODO: eventually make to update with list of rectangles
    def update(self, floorRect):
        if not (self.yPos > SCREEN_HEIGHT - TEST_FLOOR_HEIGHT - PLAYER_HEIGHT - 1 and self.yVel > 0
                and self.xPos <= 0 and self.xVel < 0):                                 # checks if in bottom left corner

            if self.yPos > SCREEN_HEIGHT - TEST_FLOOR_HEIGHT - PLAYER_HEIGHT - 1 and self.yVel > 0:  # checks for collision with floor
                # print("floor")
                self.xPos += self.xVel
            elif self.xPos <= 0 and self.xVel < 0:                             # checks collision on left side of screen
                # print("left wall")
                self.yPos += self.yVel
            else:                                                                      # checks for moving through floor
                self.xPos += self.xVel
                self.yPos += self.yVel
        self.pos = self.image.get_rect().move(self.xPos, self.yPos)  # update position

    def resetPosition(self, x, y):
        self.xPos = x
        self.yPos = y
        self.pos = self.image.get_rect().move(x, y)

    def setXVelocity(self, xVel):
        self.xVel = xVel

    def setYVelocity(self, yVel):
        self.yVel = yVel

    def moveRight(self):
        self.xVel = 5

    def moveLeft(self):
        self.xVel = -5

    def moveUp(self):
        self.yVel = -5

    def moveDown(self):
        self.yVel = 5

