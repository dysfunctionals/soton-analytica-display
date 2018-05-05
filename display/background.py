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



        self.sprites.update(self.speed)

        if len(self.sprites) < self.building_amount:
            q = -99999
            for buildong in self.sprites:
                if buildong.rect.x > q:
                    q = buildong.rect.x
            self.add_building(random.randint(100, 800), q + self.building_width, width=self.building_width)

        self.screen.fill(BACKGROUND)

        self.sprites.draw(self.screen)
        
        zucc = pygame.image.load(os.path.join("assets", "backgrounds", "city", "ground.png"))
        self.screen.blit(zucc, (0, screen_height - GROUND_HEIGHT))

    def generate_buildings(self):

        for i in range(1, self.building_amount):

            self.add_building(random.randint(100, 800), i * self.building_width, width=self.building_width)

    def add_building(self, *args, **kwargs):

        building = Building(*args, **kwargs)
        self.sprites.add(building)


class Building(pygame.sprite.Sprite):

    def __init__(self, height, xpos, width=100):

        super().__init__()

        self.height = height
        self.width = width

        self.image_name = random.choice(list(BGINFO["layers"]["city"]["scroll"].keys()))
        self.image_info = BGINFO["layers"]["city"]["scroll"][self.image_name]

        image = pygame.image.load(os.path.join("assets", "backgrounds", "city", "scroll", self.image_name))
        self.image = pygame.transform.scale(image, (200, 800))

        self.rect = self.image.get_rect()

        self.rect.y = screen_height - GROUND_HEIGHT - self.height
        self.rect.x = xpos

    def update(self, speed):

        self.rect.x -= speed

        if self.rect.x < -self.width:
            self.kill()