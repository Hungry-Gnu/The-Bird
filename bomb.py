import pygame
from colors import *
from constants import *
from sound import *

def get_image_bomb():
    image = pygame.Surface((BOMB_WIDTH, BOMB_HEIGHT))
    image.fill(COLOR_WHITE)
    image.set_colorkey(COLOR_WHITE)
    pygame.draw.ellipse(image, COLOR_BLACK, (0, 0, BOMB_WIDTH, BOMB_HEIGHT))
    return image

############################
###CLASS Bomb###############
class Bomb(pygame.sprite.Sprite):
    ############################
    ###INITIALISATION###########
    def __init__(self, bird):
        super().__init__()
        #SURFACE WHERE DRAW BOMB
        self.bird = bird
        self.image = get_image_bomb()
        rect = pygame.Surface.get_rect(self.image)
        self.rect = pygame.Rect(rect)
        xy = bird.rect.midbottom
        self.rect.center = xy

        self.speed_x = self.bird.speed_x
        self.speed_y = GRAVITATION
        self.bomb_drop = pygame.mixer.Sound(file_bomb_drop)
        pygame.mixer.Sound.play(self.bomb_drop)

    def update(self):
        if not self.alive():
            del self
            return
        
        self.rect.move_ip(self.speed_x, int(self.speed_y))
        self.speed_y *= GRAVITATION
        if self.rect.y > TUPLE_Y_LEVELS[0]:
            self.kill()
            del self

    '''
    def blit(self):
        self.screen.blit(self.image, self.rect)
    '''

