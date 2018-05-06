import pygame
from time import sleep
from display.constants import SENDPROJECTILE

class ProjectileMaker:
    def run(self):
        while True:
            projectileEvent = pygame.event.Event(SENDPROJECTILE)
            pygame.event.post(projectileEvent)
            sleep(5)