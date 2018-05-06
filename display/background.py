import pygame, os, math, random


from display.constants import *

class Background:

    def __init__(self, screen):
        self.screen = screen
        self.sprites = pygame.sprite.Group()

        self.speed = 6

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
            self.add_building(q + self.building_width)

        self.screen.fill(BACKGROUND)

        self.sprites.draw(self.screen)

        zucc = pygame.image.load(os.path.join("assets", "backgrounds", "city", "ground.png"))
        self.screen.blit(zucc, (0, screen_height - GROUND_HEIGHT))

    def generate_buildings(self):

        for i in range(1, self.building_amount):

            self.add_building(i * self.building_width)

    def add_building(self, *args, **kwargs):

        building = Building(*args, **kwargs)
        self.sprites.add(building)


class Building(pygame.sprite.Sprite):

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

    def update(self, speed):

        self.rect.x -= speed

        if self.rect.x < -self.width:
            self.kill()