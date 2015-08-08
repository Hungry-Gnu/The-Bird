import pygame
from constants import *
from colors import *
############################
###CLASS Nest###############
class Nest(pygame.sprite.Sprite):
    ############################
    ###INITIALISATION###########
    def __init__(self, screen, xy_midbottom):
        super().__init__()
        #SURFACE WHERE DRAW NEST SURFACE
        self.screen = screen
        #DEFINE NEST RECTANGLE
        self.rect = pygame.Rect(0, 0, NEST_WIDTH, NEST_HEIGHT)
        #GET NEST SURFACE
        self.surface = pygame.Surface(self.rect.size)
        self.surface.set_colorkey(COLOR_WHITE)
        self.create_image()
        self.rect.midbottom = xy_midbottom

    def create_image(self):
        self.surface.fill(COLOR_WHITE)
        pygame.draw.ellipse(self.surface,COLOR_NEST_1,self.rect)
        pygame.draw.ellipse(self.surface,COLOR_NEST_2,self.rect.inflate(-20,-10))
           

    def blit(self):
        self.screen.blit(self.surface, self.rect.topleft)

