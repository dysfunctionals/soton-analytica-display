import pygame

from display.background import Background
from display.statecode import StateCode


class Menu:

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        bg = Background(self.screen, show_logo=False)

        clock = pygame.time.Clock()

        bg.render()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return StateCode.END

            pygame.display.flip()
            clock.tick(60)

        return StateCode.INTRO