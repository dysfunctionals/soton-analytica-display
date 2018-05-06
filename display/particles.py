import pygame
import os
import random
from display.constants import *

class Particle(pygame.sprite.Sprite):

    def __init__(self, x, y, colour):
        super().__init__()
        self.colour = colour
        self.draw_image()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xv = random.randrange(-5, 5)
        self.yv = random.randrange(-3, 10)

    def draw_image(self):
        if self.colour == 'blue':
            ifile = pygame.image.load(os.path.join("assets", "particles", self.colour +  str(random.randrange(0, 6)) + ".png"))
        if self.colour == 'gold':
            ifile = pygame.image.load(os.path.join("assets", "particles", self.colour + str(random.randrange(0, 4)) + ".png"))
        if self.colour == 'orange':
            ifile = pygame.image.load(os.path.join("assets", "particles", self.colour + str(random.randrange(0, 5))) + ".png")
        if self.colour == 'facebook':
            ifile = pygame.image.load(os.path.join("assets", "particles", "fb.png"))
        self.image = pygame.transform.scale(ifile, (30, 30))

    def update(self):
        if self.rect.y > screen_height + 10:
            self.kill()

        self.rect.x += self.xv
        self.rect.y += self.yv
        self.yv += 2

    @staticmethod
    def makeParticleFamily(numParticles, x, y, colour):
        particles = []
        for i in range(0, numParticles):
            particles.append( Particle( random.randrange(x-50, x+50), random.randrange(y-50, y+50), colour ) )
        return particles