import pygame

#NOTE: Each class that implements this class will have its own update() function
class Objects(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, xVel, yVel, image):
        super().__init__()  #Calling parent's constructor
        self.xPos = xPos    #sets all subsequent variables for objects
        self.yPos = yPos
        self.xVel = xVel
        self.yVel = yVel
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.xPos
        self.rect.y = self.yPos


    def getxPos(self):      #Getter function for xPos
        return self.xPos

    def setxPos(self, xPos):    #Setter function for xPos
        self.xPos = xPos

    def getyPos(self):      #Getter function for yPos
        return self.yPos

    def setyPos(self, yPos):    #Setter function for yPos
        self.yPos = yPos

    def getxVel(self):      #Getter function for xVel
        return self.xVel

    def setxVel(self, xVel):    #Setter function for xVel
        self.xVel = xVel

    def getyVel(self):      #Getter function for yVel
        return self.yVel

    def setyVel(self, yVel):    #Setter function for yVel
        self.yVel = yVel