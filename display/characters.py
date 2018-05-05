import pygame
import os


class Character(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.setupImage()
        self.rect = self.image.get_rect()

        # Initial Position
        self.rect.x = 0
        self.rect.y = 0

        # Initial Speed
        self.xSpeed = 0
        self.ySpeed = 0

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
        self.rect.y += amount


class ZUCC(Character):

    def __init__(self):

        self.stages = os.listdir("assets/zucc/")
        self.stages.sort()

        self.currentStage = 0

        super().__init__()

    def setupImage(self):
        self.drawImage()

    def drawImage(self):

        if self.currentStage < len(self.stages):
            zucc = pygame.image.load(os.path.join("assets", "zucc", self.stages[self.currentStage]))
            self.image = pygame.transform.scale(zucc, (320, 480))

    def evolve(self):

        self.currentStage += 1
        self.drawImage()
