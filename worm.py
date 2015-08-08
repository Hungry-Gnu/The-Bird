import pygame
import random
from colors import *
from constants import *
def get_worm_image():
    image = pygame.Surface(WORM_SIZE)
    image.fill(COLOR_WHITE)
    image.set_colorkey(COLOR_WHITE)
    w, h = WORM_SIZE
    rect1 = 0, 0, 3*w/4, 2*h
    rect2 = w/4, -h, 3*w/4, 2*h
    pygame.draw.arc(image, COLOR_WORM, rect1, 0, 3.14, 4)
    pygame.draw.arc(image, COLOR_WORM, rect2, 3.14, 0, 4)
    #pygame.draw.rect(image, COLOR_BLUE, (0,0,w,h), 2)
    return image
class Worm(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.offset_x = 20
        self.x = random.randint(self.offset_x, RESOLUTION[0] - self.offset_x)
        self.y = TUPLE_Y_LEVELS[0] - WORM_SIZE[1]
        self.image = get_worm_image()
        self.rect = pygame.Rect(pygame.Surface.get_rect(self.image))
        self.rect.center = self.x, self.y
        self.time_living = random.randint(WORM_TIME_MIN, WORM_TIME_MAX)
    def update(self):
        self.time_living -=1
        if self.time_living <= 0:
            self.kill()
            del self




