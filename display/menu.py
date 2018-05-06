import os
import pygame

from display.background import Background
from display.statecode import StateCode
from display.constants import *
from display.text import Text


class Menu:

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        text = Text((0, 0), (0, 0, 0))
        text.text = "Press any key to begin..."
        text.render(self.screen)

        bg = Background(self.screen, show_logo=False)

        clock = pygame.time.Clock()

        bg.render()

        self.draw_logo()

        text.pos = ((screen_width - text.width()) / 2, 800 - text.height() - 20)
        text.render(self.screen)

        menu_loop = True
        while menu_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return StateCode.END
                elif event.type == pygame.KEYDOWN:
                    menu_loop = False

            pygame.display.flip()
            clock.tick(60)

        return StateCode.INTRO

    def draw_logo(self):

        rect = pygame.Surface((1000, 800))
        rect.set_alpha(200)
        rect.fill((200, 200, 200))

        self.screen.blit(rect, ((screen_width - 1000) / 2, 50))

        logo = pygame.image.load(os.path.join("assets", "logos", "game.png"))

        self.screen.blit(logo, ((screen_width - 800) / 2, 100))