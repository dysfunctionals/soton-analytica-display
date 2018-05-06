import pygame, os, math, random

from display.constants import *


class Background:

    def __init__(self, screen):
        self.screen = screen

        self.building_scroller = Scroller(Building, 6)

    def render(self):

        self.building_scroller.update()

        self.screen.fill(BACKGROUND)

        logo = pygame.image.load(os.path.join("assets", "logos", "game.png"))
        logo = pygame.transform.scale(logo, (400, 300))
        self.screen.blit(logo, (0, 0))

        self.building_scroller.draw(self.screen)

        road = pygame.image.load(os.path.join("assets", "backgrounds", "city", "road_0.png"))
        road = pygame.transform.scale(road, (screen_width, 100))
        self.screen.blit(road, (0, screen_height - GROUND_HEIGHT))


class Scroller(pygame.sprite.Group):

    def __init__(self, cla, speed, spritewidth=200):
        super().__init__()

        self.sprite_class = cla

        self.speed = speed

        self.sprite_width = spritewidth

        self.sprite_amount = int(math.ceil(screen_width / self.sprite_width) * 2)

        for i in range(1, self.sprite_amount):
            self.add_new(i * self.sprite_width)

    def add_new(self, *args, **kwargs):

        sprite = self.sprite_class(*args, **kwargs)
        self.add(sprite)

    def update(self):
        super().update(self.speed)

        if len(self) < self.sprite_amount:
            q = -99999
            for building in self:
                if building.rect.x > q:
                    q = building.rect.x
            self.add_new(q + self.sprite_width)

class ScrollableSprite(pygame.sprite.Sprite):

    def update(self, speed):

        self.rect.x -= speed

        if self.rect.x < -self.width:
            self.kill()

class Building(ScrollableSprite):

    def __init__(self, xpos):

        super().__init__()

        self.image_name = random.choice(list(BGINFO["layers"]["city"]["scroll"].keys()))
        self.image_info = BGINFO["layers"]["city"]["scroll"][self.image_name]

        image = pygame.image.load(os.path.join("assets", "backgrounds", "city", "scroll", self.image_name))

        image = pygame.transform.flip(image, bool(random.getrandbits(1)), False)

        self.num_stories = random.randint(1, math.floor((self.image_info["height"] - self.image_info["offset"]) / self.image_info["offset"]))

        self.height = self.image_info["offset"] * PIXEL_MULTIPLIER + (self.image_info["unit"] * self.num_stories * PIXEL_MULTIPLIER) # Visible height, not image height!
        self.width = self.image_info["width"] * PIXEL_MULTIPLIER

        self.image = pygame.transform.scale(image, (self.width, self.image_info["height"] * PIXEL_MULTIPLIER))

        self.rect = self.image.get_rect()

        self.rect.y = screen_height - GROUND_HEIGHT - self.height
        self.rect.x = xpos
