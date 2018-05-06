import pygame
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from comms.InputEvent import InputEvent
from threading import Thread

import argparse

parser = argparse.ArgumentParser(description="Z U C C will consume Y O U.")
parser.add_argument("--keyboard", help="Use the keyboard to control Z U C C", action='store_true')
args = parser.parse_args()

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

input_event = InputEvent(game_playing)
input_thread = Thread(target = input_event.run)
input_thread.start()

while game_playing:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_playing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                ZUCC.evolve()
        elif event.type == GETINPUT:
            ZUCC.ySpeed = event.zucc
            human.ySpeed = event.human

        if args.keyboard:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    ZUCC.evolve()

    if not args.keyboard:
        movement = input_source.democracy(input_valid_time_seconds)
        ZUCC.ySpeed = movement['zucc']
        human.ySpeed = movement['user']
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            ZUCC.ySpeed = -3
        elif keys[pygame.K_DOWN]:
            ZUCC.ySpeed = 3
        else:
            ZUCC.ySpeed = 0

    sprites.update()

    bg.render()

    sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
