import pygame
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from comms.CrowdInput import CrowdInput

pygame.init()

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))

sprites = pygame.sprite.Group()

ZUCC = ZUCC()
sprites.add(ZUCC)

human = Human()
sprites.add(human)

bg = Background(screen)

clock = pygame.time.Clock()

game_playing = True

input_source = CrowdInput(default_address)

while game_playing:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                ZUCC.evolve()
    
    movement = input_source.democracy(input_valid_time_seconds)
    #move the ZUCC
    ZUCC.ySpeed = movement['zucc']
    #move the human
    human.ySpeed = movement['user']

    sprites.update()

    bg.render()

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
