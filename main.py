import pygame
from display.colours import *


pygame.init()

screen_width = 1920
screen_height = 1080
game_title = "Soton Analytica"

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

game_playing = True


while game_playing:

    screen.fill(BACKGROUND)

    pygame.display.flip()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_playing = False

pygame.quit()
