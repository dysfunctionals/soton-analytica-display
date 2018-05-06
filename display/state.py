import pygame
import random
import os
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from display.text import Text
from display.projectiles import Projectile
from display.menu import Menu
from display.statecode import StateCode
from display.projectilemaker import ProjectileMaker
from display.datamanager import DataManager
from display.particles import Particle
from comms.InputEvent import InputEvent
from threading import Thread
import random

import time


class StateMachine:
    def __init__(self):
        self.state = StateCode.LOGO  # Set initial state

    @staticmethod
    def playLogo(screen):

        screen.fill((0, 0, 0))

        logo = pygame.image.load(os.path.join("assets", "logos", "team.png"))

        logo = pygame.transform.scale(logo, (screen_width, screen_height))

        logo.set_alpha(20)

        screen.blit(logo, (0,0))

        pygame.display.flip()

        pygame.mixer.music.load(os.path.join("assets", "sounds", "theme.ogg"))
        pygame.mixer.music.set_endevent(MUSIC_DEATH)
        pygame.mixer.music.play()

        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return StateCode.END
                elif event.type == MUSIC_DEATH:
                    waiting = False

        return StateCode.MENU

    @staticmethod
    def playMenu(screen):

        pygame.mixer.music.load(os.path.join("assets", "sounds", "music.mp3"))
        pygame.mixer.music.play(-1)
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

        bg = Background(screen)

        clock = pygame.time.Clock()

        game_playing = True

        if not keyboard:
            input_event = InputEvent(game_playing)
            input_thread = Thread(target=input_event.run)
            input_thread.start()
        
        projectile_event = ProjectileMaker()
        projectile_thread = Thread(target=projectile_event.run)
        projectile_thread.start()

        data_manager = DataManager()

        while game_playing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_playing = False

                if event.type == SENDPROJECTILE:
                    proj = Projectile(icons[random.randint(0,len(icons) - 1)], random.randint(1,5), random.randint(25, 300), random.randint(2 ,20), 5, 'app')
                    sprites.add(proj)

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

            for sprite in sprites:
                if type(sprite).__name__ == "Projectile":
                    if sprite.type == 'app' and sprite.rect.colliderect(human.collision_rect):
                        sprite.kill()
                        personal_data = data_manager.drop()
                        data = Projectile('data', random.randrange(-4, -8, -1), random.randrange(50, 100), random.randrange(1, 9), 5, 'data', False, human.collision_rect.x, human.collision_rect.y, data=personal_data)
                        sprites.add(data)
                        if personal_data == None:
                            #zucc wins
                            pass
                    if sprite.type == 'data' and sprite.rect.colliderect(zucc.collision_rect):
                        sprite.kill()
                        data_manager.pickup(sprite.data)
                        if personal_data == None:
                            #zucc wins
                            pass
                    if sprite.type == 'power_size' and sprite.rect.colliderect(human.collision_rect):
                        sprite.kill()
                        Projectile.override = True
                        Projectile.override_value = 2
                        Projectile.override_frames = 500
                    if sprite.type == 'power_size' and sprite.rect.colliderect(zucc.collision_rect):
                        sprite.kill()
                        Projectile.override = True
                        Projectile.override_value = 8
                        Projectile.override_frames = 500

            if(Projectile.override):
                Projectile.override_frames-=1
                if(Projectile.override_frames == 0):
                    Projectile.override = False

            if(random.randrange(0, 1500) == 1):
                power = Projectile('power_size', random.choice( [random.randrange(-15, -5), random.randrange(5, 15)] ), random.randrange(50, 300), random.randrange(2, 12), 4, 'power_size', False, screen_width / 2, screen_height / 2)
                sprites.add(power)
                for p in Particle.makeParticleFamily(25, screen_width / 2, screen_height / 2, 'gold'):
                    sprites.add(p)

            for p in Particle.makeParticleFamily(5, human.collision_rect.x + human.collision_rect.width/2 - 20, human.collision_rect.y + human.collision_rect.height, 'orange'):
                sprites.add(p)
            for p in Particle.makeParticleFamily(5, zucc.collision_rect.x + zucc.collision_rect.width/2 - 20, zucc.collision_rect.y + zucc.collision_rect.height, 'facebook'):
                sprites.add(p)

            sprites.update()

            bg.render()

            sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        return StateCode.END

    @staticmethod
    def projectilesOnScreen(projectiles):
        if len(projectiles) == 0:
            return False;
        for projectile in projectiles:
            if projectile.onScreen():
                return True;
        return False;
