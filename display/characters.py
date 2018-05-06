import pygame
import os
from display.constants import *


class Character(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.currentStage = 0
        self.setupImage()
        self.rect = self.image.get_rect()

        # Initial Position
        self.rect.x = 0
        self.rect.y = screen_height - self.getSize()[1] - GROUND_HEIGHT + 10

        # Initial Speed
        self.xSpeed = 0
        self.ySpeed = 0

        self.collision_rect = pygame.Rect(self.rect.x, self.rect.y, 320, 480)

    def setupImage(self):

        """ The basic image setup. Override in subclasses"""

        self.image = pygame.Surface([30, 30])
        self.image.fill((255, 51, 51))

    def update(self):

        self.moveX(self.xSpeed)
        self.moveY(self.ySpeed)

    def getSize(self):
        return self.image.get_size()

    def moveX(self, amount):
        self.rect.x += amount

    def moveY(self, amount):
        if not ((amount < 0 and self.rect.y < 10) or (amount > 0 and self.rect.y > screen_height - self.getSize()[1] - 10)):
            self.rect.y += amount

    def makeCollisionBoxHaveRightWidthAndHeightAndXCoordinateAndYCoordinate(self):
        currentChar_state = CHARSTATES['chars'][type(self).__name__]['states'][self.currentStage]

        self.collision_rect.y = self.rect.y + (480 - currentChar_state['height']*PIXEL_MULTIPLIER)
        self.collision_rect.x = self.rect.x + (160 - currentChar_state['width']*(PIXEL_MULTIPLIER/2))
        self.collision_rect.width = currentChar_state['width']
        self.collision_rect.height = currentChar_state['height']

class ZUCC(Character):

    def __init__(self):

        self.stages = os.listdir("assets/zucc/")
        self.stages.sort()

        super().__init__()

        # Set x position

        self.rect.x = 50

        self.makeCollisionBoxHaveRightWidthAndHeightAndXCoordinateAndYCoordinate()

    def setupImage(self):
        self.drawImage()

    def drawImage(self):

        if self.currentStage < len(self.stages):
            zucc = pygame.image.load(os.path.join("assets", "zucc", self.stages[self.currentStage]))
            self.image = pygame.transform.scale(zucc, (320, 480))

    def evolve(self):

        self.currentStage += 1
        self.makeCollisionBoxHaveRightWidthAndHeightAndXCoordinateAndYCoordinate()
        self.drawImage()

class Human(Character):

    def __init__(self):

        super().__init__()

        # Set x position

        self.rect.x = screen_width - self.getSize()[0]
        self.makeCollisionBoxHaveRightWidthAndHeightAndXCoordinateAndYCoordinate()

    def setupImage(self):
        human = pygame.image.load(os.path.join("assets", "human.png"))
        self.image = pygame.transform.scale(human, (320, 480))