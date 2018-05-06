import pygame
import os
from display.constants import *
import random
import math

class Projectile(pygame.sprite.Sprite):

    def __init__(self, icon, velocity, oscillate_height = 0, oscillate_rate = 1):

        super().__init__()

        self.icon = icon
        self.draw_image()
        self.rect = self.image.get_rect()

        clearance = math.floor((screen_height-oscillate_height)/2)
        self.rect.y = random.randrange(clearance, screen_height - clearance)

        if velocity < 0:
            self.rect.x = screen_width
        else:
            self.rect.x = 0

        self.velocity = velocity
        self.oscillate_height = oscillate_height
        self.oscillate_rate = oscillate_rate
        self.default_y = self.rect.y

    def draw_image(self):
        ifile = pygame.image.load(os.path.join("assets", "items", self.icon + ".png"))
        self.image = pygame.transform.scale(ifile, (150, 150))

    def update(self):
        self.rect.x += self.velocity

        if self.oscillate_height != 0:
            self.rect.y = self.default_y + math.floor(math.sin((self.rect.x * self.oscillate_rate / screen_width) * 2 * math.pi) * self.oscillate_height)