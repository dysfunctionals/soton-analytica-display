import pygame, os

from display.constants import *


class Background:

    @staticmethod
    def render(screen):

        screen.fill(BACKGROUND)

        zucc = pygame.image.load(os.path.join("assets", "backgrounds", "bad","ground.png"))

        screen.blit(zucc, (0, screen_height - 100))
