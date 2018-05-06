import pygame
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from display.text import Text
from display.projectiles import Projectile
from display.menu import Menu
from display.statecode import StateCode
from comms.InputEvent import InputEvent
from threading import Thread


class StateMachine:

    def __init__(self):

        self.state = StateCode.MENU  # Set initial state

    @staticmethod
    def playMenu(screen):

        menu = Menu(screen)

        return menu.run()

    @staticmethod
    def playIntro(screen):
        welcomeText = Text((550,400), (255,255,255))
        welcomeText.text = "zucc"
        welcomeText.font = welcomeText.make_font(['Lucida Console'], 128)
        introRunning = True
        bg = Background(screen)
        clock = pygame.time.Clock()
        sprites = pygame.sprite.Group()
        zucc = ZUCC()
        sprites.add(zucc)
        groundLevel = zucc.rect.y
        zucc.rect.y = -500

        while introRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return StateCode.END

            zucc.moveY(3)
        
            if zucc.rect.y >= groundLevel - 3:
                introRunning = False

            bg.render()
            sprites.update()
            welcomeText.render(screen)

            sprites.draw(screen)
            pygame.display.flip()
            clock.tick(60)

        return StateCode.PLAYING

    @staticmethod
    def playGame(screen, keyboard):

        sprites = pygame.sprite.Group()

        zucc = ZUCC()
        sprites.add(zucc)

        human = Human()
        sprites.add(human)

        i_like_this = Projectile('like', -6, 250, 2)
        sprites.add(i_like_this)

        b = Projectile('wa', 4, 117, 20)
        sprites.add(b)

        q = Projectile('ig', -8, 300, 7)
        sprites.add(q)

        z = Projectile('fb', 5, 27, 9)
        sprites.add(z)

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
