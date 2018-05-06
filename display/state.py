import pygame
from enum import Enum
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from comms.InputEvent import InputEvent
from threading import Thread

class State:
    def __init__(self, screen, keyboard):
        self.screen = screen
        self.keyboard = keyboard
        self.stateCode = StateCode.MENU
        # do menu
    
    def playIntro(self):
        if self.stateCode == StateCode.MENU:
            self.stateCode = StateCode.INTRO
            # do intro
        else:
            raise EnvironmentError

    def playGame(self):
        if self.stateCode == StateCode.INTRO:
            self.stateCode = StateCode.PLAYING
            sprites = pygame.sprite.Group()

            zucc = ZUCC()
            sprites.add(zucc)

            human = Human()
            sprites.add(human)

            bg = Background(self.screen)

            clock = pygame.time.Clock()

            game_playing = True

            if not self.keyboard:
                input_event = InputEvent(game_playing)
                input_thread = Thread(target = input_event.run)
                input_thread.start()

            while game_playing:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        game_playing = False

                    if self.keyboard:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_e:
                                zucc.evolve()

                if not self.keyboard:
                    if event.type == GETINPUT:
                        zucc.ySpeed = event.zucc
                        human.ySpeed = event.human
                else:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        zucc.ySpeed = -3
                    elif keys[pygame.K_DOWN]:
                        zucc.ySpeed = 3
                    else:
                        zucc.ySpeed = 0

                sprites.update()

                bg.render()

                sprites.draw(self.screen)

                pygame.display.flip()
                clock.tick(60)

            self.endGame()                
        else:
            raise EnvironmentError

    def endGame(self):
        if self.stateCode == StateCode.PLAYING:
            self.stateCode = StateCode.DONE
            pygame.quit()
        else:
            raise EnvironmentError

class StateCode(Enum):
    MENU = 1
    INTRO = 2
    PLAYING = 3
    DONE = 4