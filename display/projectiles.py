import pygame
import os
from display.constants import *
import random
import math

class Projectile(pygame.sprite.Sprite):
  
    override = False
    override_value = 5
    override_frames = 0

    def __init__(self, icon, velocity, oscillate_height = 0, oscillate_rate = 1, pixel_scale = 5, type = 'passive', random_start = True, start_x = 0, start_y = 0, data = None):
        super().__init__()

        self.pixel_scale = pixel_scale
        self.icon = icon
        self.draw_image()
        self.rect = self.image.get_rect()

        if random_start:
            clearance = math.floor((screen_height - oscillate_height) / 2)
            self.rect.y = random.randrange(clearance, screen_height - clearance)

            if velocity < 0:
                self.rect.x = screen_width
            else:
                self.rect.x = 0
        else:
            self.rect.y = start_y
            self.rect.x = start_x

        self.velocity = velocity
        self.oscillate_height = oscillate_height
        self.oscillate_rate = oscillate_rate
        self.default_y = self.rect.y
        self.type = type

        self.data = data

    def draw_image(self):
        ifile = pygame.image.load(os.path.join("assets", "items", self.icon + ".png"))
        if Projectile.override:
            self.image = pygame.transform.scale(ifile, (15 * Projectile.override_value, 15 * Projectile.override_value))
        else:
            self.image = pygame.transform.scale(ifile, (15 * self.pixel_scale, 15 * self.pixel_scale))

    def update(self):
        self.rect.x += self.velocity

        if self.oscillate_height != 0:
            self.rect.y = self.default_y + math.floor(math.sin((self.rect.x * self.oscillate_rate / screen_width) * 2 * math.pi) * self.oscillate_height)

        if self.rect.x < -500 or self.rect.x > screen_width+500:
            self.kill()
