# Text Display class
# Originally from trickeydan/PythonScience, but reused with permission.
import pygame


class Text():
    """ An object to help display text in pygame """

    def __init__(self, pos, colour):
        self.pos = pos
        self.colour = colour
        self.font = self.make_font(['monospace'], 64)
        self.text = ""

    def render(self,screen):
        screen.blit(self.getSurface(),self.pos)

    def getSurface(self):
        return self.font.render(self.text, True, self.colour)

    def height(self):
        return self.getSurface().get_height()

    def width(self):
        return self.getSurface().get_width()

    def make_font(self, fonts, size):
        available = pygame.font.get_fonts()
        # get_fonts() returns a list of lowercase spaceless font names
        choices = map(lambda x: x.lower().replace(' ', ''), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
        return pygame.font.Font(None, size)