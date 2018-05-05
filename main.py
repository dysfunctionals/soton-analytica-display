import pygame
from display.colours import *
from display.characters import ZUCC, Human
from comms.CrowdInput import CrowdInput


pygame.init()

screen_width = 1920
screen_height = 1080
game_title = "Soton Analytica"

input_valid_time_seconds = 3
input_type = "democracy"

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

game_playing = True

sprites = pygame.sprite.Group()

ZUCC = ZUCC()
sprites.add(ZUCC)

human = Human()
sprites.add(human)

input_source = CrowdInput(CrowdInput.standardAddress())

while game_playing:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ZUCC.ySpeed = 3
            elif event.key == pygame.K_e:
                ZUCC.evolve()
    
    movement = input_source.democracy(input_valid_time_seconds)
    #move the ZUCC
    ZUCC.ySpeed = movement['zucc']
    #move the human
    human.ySpeed = movement['user']

    sprites.update()

    screen.fill(BACKGROUND)

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
