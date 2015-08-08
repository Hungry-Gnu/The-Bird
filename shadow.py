import pygame
from colors import *
from constants import *

#CLASS SHADOW
class Shadow (pygame.sprite.Sprite):
    def __init__(self, body):
        super().__init__()
        self.body = body
        self.size = body.shadow_size
        self.rect = pygame.Rect((0,0), self.size)
        self.rect.center = self.body.rect.midbottom
        self.get_image()

    def get_image(self):

        self.image = pygame.Surface(self.size)
        self.image.fill(COLOR_WHITE)
        self.image.set_colorkey(COLOR_WHITE)
        
        pygame.draw.ellipse(self.image, COLOR_GRAY, (0,0,self.rect.w,self.rect.h) )
        
        self.image.set_alpha(50)

    def update(self):
        #print(self.rect)
        if self.body.alive():
            self.rect.centerx = self.body.rect.centerx

        else:
            self.kill()
            del self
