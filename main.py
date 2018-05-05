import pygame
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background

pygame.init()

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

game_playing = True

sprites = pygame.sprite.Group()

ZUCC = ZUCC()
sprites.add(ZUCC)

human = Human()
sprites.add(human)

while game_playing:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ZUCC.ySpeed = -3
            elif event.key == pygame.K_DOWN:
                ZUCC.ySpeed = 3
            elif event.key == pygame.K_e:
                ZUCC.evolve()
        elif event.type == pygame.KEYUP:
            ZUCC.ySpeed = 0

    sprites.update()

    Background.render(screen)

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
