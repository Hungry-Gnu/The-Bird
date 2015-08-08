import pygame
from constants import *
from colors import *
############################
###CLASS Nest###############
class Flag(pygame.sprite.Sprite):
    ############################
    ###INITIALISATION###########
    def __init__(self, nest):
        super().__init__()
        #SURFACE WHERE DRAW NEST SURFACE
        self.nest = nest
        #DEFINE NEST RECTANGLE
        self.rect = pygame.Rect(0, 0, nest.rect.width//3, nest.rect.height)
        #GET NEST SURFACE
        self.image = pygame.Surface(self.rect.size)
        self.image.set_colorkey(COLOR_WHITE)
        self.create_image()
        self.rect.bottomleft = self.nest.rect.midright

    def create_image(self):
            self.image.fill(COLOR_WHITE)
            pygame.draw.line(self.image,COLOR_BLACK,self.rect.bottomleft,self.rect.topleft,3)
            pygame.draw.polygon(self.image,COLOR_RED,(self.rect.midleft,self.rect.topleft,self.rect.midright))
           

    def blit(self):
        self.nest.screen.blit(self.image, self.rect)
