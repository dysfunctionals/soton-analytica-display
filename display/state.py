import pygame
from enum import Enum
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from comms.InputEvent import InputEvent
from threading import Thread


class StateMachine:

    def __init__(self):

        self.state = StateCode.MENU  # Set initial state

    @staticmethod
    def playMenu(screen):

        bg = Background(screen, show_logo=False)

        clock = pygame.time.Clock()

        bg.render()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return StateCode.END

            pygame.display.flip()
            clock.tick(60)

        return StateCode.INTRO

    @staticmethod
    def playIntro(screen):
        return StateCode.PLAYING

    @staticmethod
    def playGame(screen, keyboard):

        sprites = pygame.sprite.Group()

        zucc = ZUCC()
        sprites.add(zucc)

        human = Human()
        sprites.add(human)

        bg = Background(screen)

        clock = pygame.time.Clock()

        game_playing = True

        if not keyboard:
            input_event = InputEvent(game_playing)
            input_thread = Thread(target=input_event.run)
            input_thread.start()

        while game_playing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_playing = False

                if keyboard:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e:
                            zucc.evolve()
                else:
                    if event.type == GETINPUT:
                        zucc.ySpeed = event.zucc
                        human.ySpeed = event.human

            if keyboard:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    zucc.ySpeed = -3
                elif keys[pygame.K_DOWN]:
                    zucc.ySpeed = 3
                else:
                    zucc.ySpeed = 0

            sprites.update()

            bg.render()

            sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        return StateCode.END


class StateCode(Enum):
    MENU = 1
    INTRO = 2
    PLAYING = 3
    END = 4