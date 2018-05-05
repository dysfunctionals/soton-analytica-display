import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.setupImage()
        self.rect = self.image.get_rect()

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

        super().__init__()

        self.stages = [
            ""
        ]

        self.currentStage = self.stages[0]

    def evolve(self):

        raise NotImplementedError
