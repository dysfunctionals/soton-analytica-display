import pygame, os, math, random

from display.constants import *


class Background:

    def __init__(self, screen):
        self.screen = screen
        self.sprites = pygame.sprite.Group()

        self.speed = 12

        self.building_width = 200

        self.building_amount = math.ceil(screen_width / self.building_width) * 2

        self.generate_buildings()

    def render(self):

        self.screen.fill(BACKGROUND)

        zucc = pygame.image.load(os.path.join("assets", "backgrounds", "bad", "ground.png"))

        self.screen.blit(zucc, (0, screen_height - GROUND_HEIGHT))

        self.sprites.update(self.speed)


        if len(self.sprites) < self.building_amount:
            self.generate_building()

        self.sprites.draw(self.screen)

    def generate_buildings(self):

        for i in range(1, self.building_amount):

            self.add_building(random.randint(100, 800), i * self.building_width, width=self.building_width)

    def generate_building(self):
        q = -99999
        for buildong in self.sprites:
            if buildong.rect.x > q:
                q = buildong.rect.x
        self.add_building(random.randint(100, 800), q+self.building_width, width=self.building_width)

    def add_building(self, *args, **kwargs):

        building = Building(*args, **kwargs)
        self.sprites.add(building)


class Building(pygame.sprite.Sprite):

    def __init__(self, height, xpos, width=100):

        super().__init__()

        self.height = height
        self.width = width

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((51, 51, 51))
        self.rect = self.image.get_rect()

        self.rect.y = screen_height - GROUND_HEIGHT - self.height
        self.rect.x = xpos

    def update(self, speed):

        self.rect.x -= speed

        if self.rect.x < -self.width:
            self.kill()