import pygame
from fonts import *
from colors import *

class Label():
    def __init__(self, text, font, font_size, color = COLOR_BLACK):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.SysFont(font, font_size)
        self.image = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(self.image.get_rect())
