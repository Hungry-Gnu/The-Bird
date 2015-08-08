import pygame
from fonts import *
from colors import *
class Score_label:
    def __init__(self, x, y, text_before, text_after, font_size = FONT_SIZE_COORD, font_name = FONT_MAIN, color = COLOR_BLACK):
        """Constructor"""
        self.x = x
        self.y = y
        self.text_before = text_before
        self.text_after = text_after
        self.font_size = font_size
        self.font_name = font_name
        self.color = color

    def make_image(self, score):
        text = self.text_before + str(score) + self.text_after
        font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def update(self, score):
        self.make_image(score)
    def draw(self, screen):
        screen.blit(self.image,self.rect)

