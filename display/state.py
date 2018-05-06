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

        start_ticks = pygame.time.get_ticks()
        day_past = 0

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

            sprites.update()

            bg.render()

            # Show player data
            data = {
                'name': True,
                'DOB': True,
                'address': True,
                'contact': True
            }

            x = 400
            zucc_label = Text((x, 0), (37,55,140))
            zucc_label.text = "zucc has your data:"
            zucc_label.font = zucc_label.make_font(['Lucida Console'], 36)
            zucc_label.render(screen)
            y = 38
            for data_name, is_good in data.items():
                if not is_good:
                    zucc_data = Text((x, y), (255,255,255))
                    zucc_data.text = data_name
                    zucc_data.font = zucc_data.make_font(['Lucida Console'], 36)
                    zucc_data.render(screen)
                    y += 38

            x = screen_width - 200
            user_label = Text((x, 0), (54,125,33))
            user_label.text = "user data:"
            user_label.font = zucc_label.make_font(['Lucida Console'], 36)
            user_label.render(screen)
            y = 38
            for data_name, is_good in data.items():
                if is_good:
                    user_data = Text((x, y), (255, 255, 255))
                    user_data.text = data_name
                    user_data.font = user_data.make_font(['Lucida Console'], 36)
                    user_data.render(screen)
                    y += 38

            # Show countdown to GDPR
            if day_past < 20:
                day_past = (pygame.time.get_ticks() - start_ticks) / 4500
            countdown_gdpr = Text((screen_width / 2 - 100, 0), (255,255,255))
            countdown_gdpr.text = '{:02d} days till GDPR'.format(int(20 - day_past))
            countdown_gdpr.font = countdown_gdpr.make_font(['Lucida Console'], 36)
            countdown_gdpr.render(screen)

            # Show progress bar
            pygame.draw.rect(screen, (75,102,173), pygame.Rect(screen_width / 2 - 200,48,400,10))
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(screen_width / 2 - 200,48, 400 * (day_past/20),10))

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
