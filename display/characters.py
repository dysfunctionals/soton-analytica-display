import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface([30, 30]) # Temporary until we have art

        self.image.fill((255, 51, 51)) # Make red rectangle because

        self.rect = self.image.get_rect()

    def update(self):

        pass
