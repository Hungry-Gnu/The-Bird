import pygame
from colors import *
class Bar:
    def __init__(self, screen, xy, size = 100):
        self.screen = screen
        self.size = size
        self.rect = pygame.Rect(xy, size)
        self.rect_parameter = pygame.Rect((0, 0), size)
        self.image = pygame.Surface(size)
    def update(self, parameter = 100):
        '''update(parameter), parameter could be 0 to 100.'''
        self.image.fill(COLOR_WHITE)
        self.rect_parameter.width = parameter * self.size[0] // 100
        pygame.draw.rect(self.image, COLOR_RED, self.rect_parameter)
    def blit(self):
        self.screen.blit(self.image, self.rect)

        
        
